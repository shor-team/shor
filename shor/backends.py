from collections import deque, Counter
from functools import lru_cache
from typing import List, Deque, NamedTuple, Tuple, Dict

import numpy as np

from shor.gates import _Gate
from shor.quantum import Circuit


class _GateTuple(NamedTuple):
    qubits: List[int]
    matrix: np.ndarray
    order: int


class _QuantumBackend(object):
    def run(self, initial_state: List[int], gates: List[_Gate], measure_bits: List[int], num_shots, **kwargs):
        pass


class QuantumSimulator(_QuantumBackend):

    @staticmethod
    @lru_cache(maxsize=10)
    def combine_gates(gates: Tuple[_Gate]) -> _GateTuple:
        to_combine: Deque[_GateTuple] = deque(_GateTuple(g.qbits, g.to_matrix(), i) for i, g in enumerate(gates))
        combined: Deque[_GateTuple] = deque()

        while len(to_combine) > 1:
            while len(to_combine) > 1:
                left_gate = to_combine.popleft()
                right_gate = to_combine.popleft()

                # Swap if out of order
                if right_gate.order < left_gate.order:
                    left_gate, right_gate = right_gate, left_gate

                can_combine_no_tensor = set(left_gate.qubits) == set(right_gate.qubits)
                can_combine_with_tensor = not has_common_qbits(left_gate, right_gate)

                if can_combine_no_tensor:
                    combined.append(_GateTuple(
                        left_gate.qubits,
                        change_qubit_order(right_gate.matrix, right_gate.qubits, left_gate.qubits).dot(left_gate.matrix),
                        left_gate.order
                    ))
                elif can_combine_with_tensor:
                    combined.append(_GateTuple(
                        left_gate.qubits + right_gate.qubits,
                        np.kron(
                            left_gate.matrix,
                            right_gate.matrix
                        ),
                        right_gate.order
                    ))
                else:
                    common_qubits = tuple(q for q in left_gate.qubits if q in right_gate.qubits)
                    left_only_qbits = tuple(q for q in left_gate.qubits if q not in common_qubits)
                    right_only_qbits = tuple(q for q in right_gate.qubits if q not in common_qubits)
                    all_qubits = left_only_qbits + common_qubits + right_only_qbits

                    new_left_qbit_order = left_only_qbits + common_qubits
                    new_left_gate = change_qubit_order(left_gate.matrix, left_gate.qubits, new_left_qbit_order)

                    # Tensor product with I to fill missing qbits
                    qbits_to_add = len(all_qubits) - len(left_gate.qubits)
                    if qbits_to_add > 0:
                        new_left_gate = np.kron(new_left_gate, np.eye(np.power(2, qbits_to_add)))

                    new_right_qbit_order = common_qubits + right_only_qbits
                    new_right_gate = change_qubit_order(right_gate.matrix, right_gate.qubits, new_right_qbit_order)

                    # Tensor product with I to fill missing qbits
                    qbits_to_add = len(all_qubits) - len(right_gate.qubits)
                    if qbits_to_add > 0:
                        new_right_gate = np.kron(np.eye(np.power(2, qbits_to_add)), new_right_gate)

                    combined.append(_GateTuple(
                        all_qubits,
                        new_right_gate.dot(new_left_gate),
                        right_gate.order
                    ))

            to_combine += combined
            combined = deque()

        return to_combine.pop()

    def run(self, initial_state: List[int], gates: List[_Gate], measure_bits: List[int], num_shots, **kwargs):
        combined = self.combine_gates(tuple(gates))
        new_qubit_order = combined.qubits
        state_vector = get_entangled_initial_state(initial_state, new_qubit_order)

        probabilities = np.square(np.absolute(combined.matrix.dot(state_vector))).real
        probabilities /= np.sum(probabilities)

        measured = Counter([np.random.choice(state_vector.shape[0], p=probabilities) for m in range(num_shots)])
        return measured


class QSession(object):
    def __init__(self, **kwargs):
        self.backend = kwargs.get('backend', QuantumSimulator())

    def run(self, circuit: Circuit, **kwargs):
        num_shots = kwargs.get('num_shots', 1024)

        initial_state = circuit.initial_state()
        gates = circuit.to_gates()
        measure_bits = circuit.measure_bits()

        counts = self.backend.run(initial_state, gates, measure_bits, num_shots)

        return QResult(counts, sig_bits=len(circuit.initial_state()))


class QResult(object):
    def __init__(self, counts: Dict[int, int], sig_bits: int):
        self.counts: Dict[int, int] = counts
        self.sig_bits: int = sig_bits

    def get(self, key, default=0):
        if isinstance(key, str):
            idx = int_from_bit_string(key)
        else:
            idx = key

        return self.counts.get(idx, default)

    def __getitem__(self, item):
        return self.get(item)

    def __repr__(self):
        return repr({int_to_bit_string(k, self.sig_bits): v for k, v in self.counts.items()})


def get_entangled_initial_state(initial_state, new_qubit_order):
    states_to_entangle: Deque[np.ndarray] = deque()

    states = list(map(lambda s: np.asarray([1 if s == 0 else 0, 1 if s == 1 else 0], dtype='complex64'), initial_state))

    for q in new_qubit_order:
        states_to_entangle.append(states[q])

    while len(states_to_entangle) > 1:
        entangled_states: Deque[np.ndarray] = deque()
        while len(states_to_entangle) > 1:
            entangled_states.append(np.kron(states_to_entangle.popleft(), states_to_entangle.popleft()))
        if len(states_to_entangle) == 1:
            entangled_states.append(states_to_entangle.popleft())
        states_to_entangle = entangled_states

    return states_to_entangle.pop()


def change_qubit_order(matrix: np.ndarray, old_order, new_order) -> np.ndarray:
    reorder_qubits = [new_order.index(q2) for q2 in old_order]
    initial_row_order = [i for i in range(np.power(2, len(old_order)))]

    reorder_rows = list(map(lambda i: rearrange_bits(i, reorder_qubits), initial_row_order))

    return matrix[reorder_rows][:, reorder_rows]


def rearrange_bits(num: int, new_bit_order: List[int]):
    sig_bits = len(new_bit_order)
    bit_string = int_to_bit_string(num, sig_bits)
    result = int_from_bit_string(''.join(bit_string[b] for b in new_bit_order))
    return result


def int_to_bits(num: int, sig_bits: int) -> str:
    return format(num, '#0%sb' % np.power(2, sig_bits))


def int_from_bit_string(bits: str) -> int:
    return int(bits, 2) if bits.startswith('0b') else int('0b' + bits, 2)


def int_to_bit_string(i: int, sig_bits: int) -> str:
    return '{0:b}'.format(i).zfill(sig_bits)


def has_common_qbits(gate1, gate2):
    return len(set(gate1.qubits).intersection(set(gate2.qubits))) > 0
