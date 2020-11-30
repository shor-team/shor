from collections import Counter, deque
from functools import lru_cache
from typing import Deque, Dict, List, NamedTuple, Tuple

import numpy as np

from shor.gates import _Gate
from shor.providers import Job, Provider, Result
from shor.providers.base import JobStatusCode
from shor.quantum import QuantumCircuit
from shor.utils.qbits import change_qubit_order, get_entangled_initial_state, has_common_qbits


class _GateTuple(NamedTuple):
    qubits: List[int]
    matrix: np.ndarray
    order: int


class ShorSimulatorResult(Result):
    def __init__(self, counts: Dict[int, int], sig_bits: int):
        self._counts = counts
        self._sig_bits: int = sig_bits

    @property
    def counts(self):
        return self._counts

    @property
    def sig_bits(self):
        return self._sig_bits


class ShorSimulatorJob(Job):
    def __init__(self, status: JobStatusCode, result: Result):
        self._status = status
        self._result = result

    @property
    def status(self):
        return self._status

    @property
    def result(self):
        return self._result


class ShorSimulator(Provider):
    @property
    def jobs(self) -> List[Job]:
        self._jobs

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
                    combined.append(
                        _GateTuple(
                            left_gate.qubits,
                            change_qubit_order(right_gate.matrix, right_gate.qubits, left_gate.qubits).dot(
                                left_gate.matrix
                            ),
                            left_gate.order,
                        )
                    )
                elif can_combine_with_tensor:
                    combined.append(
                        _GateTuple(
                            left_gate.qubits + right_gate.qubits,
                            np.kron(left_gate.matrix, right_gate.matrix),
                            right_gate.order,
                        )
                    )
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

                    combined.append(_GateTuple(all_qubits, new_right_gate.dot(new_left_gate), right_gate.order))

            to_combine += combined
            combined = deque()

        return to_combine.pop()

    def run(self, qc: QuantumCircuit, times):
        combined = self.combine_gates(tuple(qc.to_gates()))
        new_qubit_order = combined.qubits
        state_vector = get_entangled_initial_state(qc.initial_state(), new_qubit_order)

        probabilities = np.square(np.absolute(combined.matrix.dot(state_vector))).real
        probabilities /= np.sum(probabilities)

        measured = Counter([np.random.choice(state_vector.shape[0], p=probabilities) for m in range(times)])

        return ShorSimulatorJob(JobStatusCode.COMPLETED, ShorSimulatorResult(measured, len(new_qubit_order)))
