from collections import deque
from typing import Deque, List

import numpy as np


def get_entangled_initial_state(initial_state, new_qubit_order):
    states_to_entangle: Deque[np.ndarray] = deque()

    states = list(map(lambda s: np.asarray([1 if s == 0 else 0, 1 if s == 1 else 0], dtype="complex64"), initial_state))

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
    result = int_from_bit_string("".join(bit_string[b] for b in new_bit_order))
    return result


def int_to_bits(num: int, sig_bits: int) -> str:
    return format(num, "#0%sb" % np.power(2, sig_bits))


def int_from_bit_string(bits: str) -> int:
    return int(bits, 2) if bits.startswith("0b") else int("0b" + bits, 2)


def int_to_bit_string(i: int, sig_bits: int) -> str:
    return "{0:b}".format(i).zfill(sig_bits)


def has_common_qbits(gate1, gate2):
    return len(set(gate1.qubits).intersection(set(gate2.qubits))) > 0
