import math
import random
from typing import List, Tuple

from shor.gates import X, CNOT, CSWAP, H, Rx, QFT
from shor.layers import Qubits
from shor.operations import Measure
from shor.quantum import Circuit


def factor(N: int) -> Tuple[int, int]:
    """ WIP not currently functioning.

    The classical part seems to be correct, but the quantum period finding function is incorrect
    at the moment.
    """
    while True:
        a = random.randint(2, N - 1)
        common_divisor = gcd(a, N)
        if common_divisor > 1:
            # Lucky guess
            return common_divisor, N / common_divisor

        # r = shor.quantum.shor.period(a, N)
        r = find_period(a, N)

        a_pow_r_o_2 = a ^ (r / 2)

        # if r is odd or
        if r & 1 == 1 or a_pow_r_o_2 == (-1 % N):
            continue

        factor = max(gcd(a_pow_r_o_2 + 1, N), gcd(a_pow_r_o_2 - 1, N))
        return factor, N / factor


def find_period(a, N):
    """ WIP: Quantum subroutine for shor's algorithm.
    Finds the period of a function of the form:
    f(x) = a^x % N

    This uses the quantum fourier transform.
    """

    circuit = Circuit()
    circuit.add(Qubits(5))
    circuit.add(QFT(0, 1, 2, 3))
    circuit.add(quantum_amod_15(a))
    circuit.add(QFT(3, 2, 1, 0))  # Inverse Quantum Fourier transform

    from shor.backends import QuantumSimulator, QSession

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)
    return result


def quantum_amod_15(a: int) -> Circuit:
    qc = Circuit()

    if a == 2:
        qc.add(CSWAP(4, 3, 2))
        qc.add(CSWAP(4, 2, 1))
        qc.add(CSWAP(4, 1, 0))
    if a == 4 or a == 11 or a == 14:
        qc.add(CSWAP(4, 2, 0))
        qc.add(CSWAP(4, 3, 1))
        qc.add(CNOT(4, 3))
        qc.add(CNOT(4, 2))
        qc.add(CNOT(4, 1))
        qc.add(CNOT(4, 0))
    if a == 7:
        qc.add(CSWAP(4, 1, 0))
        qc.add(CSWAP(4, 2, 1))
        qc.add(CSWAP(4, 3, 2))
        qc.add(CNOT(4, 3))
        qc.add(CNOT(4, 2))
        qc.add(CNOT(4, 1))
        qc.add(CNOT(4, 0))
    if a == 8:
        qc.add(CSWAP(4, 1, 0))
        qc.add(CSWAP(4, 2, 1))
        qc.add(CSWAP(4, 3, 2))
    if a == 13:
        qc.add(CSWAP(4, 3, 2))
        qc.add(CSWAP(4, 2, 1))
        qc.add(CSWAP(4, 1, 0))
        qc.add(CNOT(4, 3))
        qc.add(CNOT(4, 2))
        qc.add(CNOT(4, 1))
        qc.add(CNOT(4, 0))

    return qc


def qft(qubits: List[int]) -> Circuit:
    qc = Circuit()
    for i in range(len(qubits)):
        for k in range(i):
            qc.add(Rx(qubits[i], qubits[k], angle=math.pi/float(2**(i-k))))
        qc.add(H(qubits[i]))
    return qc


def gcd(a: int, b: int) -> int:
    """Finds greatest common divisor between positive integers a and b
    Efficient, using Euclidean algorithm.

    Example:
    >>> greatest_common_divisor(15, 25)
    5
    """
    assert a > 0 and b > 0, 'Inputs should be positive integers'

    to_divide, remainder = max(a, b), min(a, b)  # initial divisor
    divisor = 1

    while remainder != 0:
        divisor = remainder
        remainder = to_divide
        while remainder >= divisor:
            remainder -= divisor
        to_divide = divisor

    return divisor
