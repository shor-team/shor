import random

from shor.algorithms.shor import factor, quantum_amod_15
from shor.layers import Qbits
from shor.operations import Measure
from shor.quantum import Circuit

# Seed for tests
random.seed(0)


def test_shor_factoring():
    N = 3 * 5

    a, b = factor(N)

    assert a == 3 or a == 5
    assert b == N / a

    N = 3 * 7

    a, b = factor(N)

    assert a == 3 or a == 7
    assert b == N / a


def test_modulus_circuit():
    circuit = Circuit()
    circuit.add(Qbits(5))
    circuit.add(quantum_amod_15(4))
    circuit.add(Measure([0, 1]))

    job = circuit.run(1024)
    result = job.result

    print(result)