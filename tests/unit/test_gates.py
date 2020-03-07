import numpy as np


def is_square(m):
    return m.shape[0] == m.shape[1] and len(m.shape) == 2


def is_unitary(m):
    return np.allclose(np.eye(m.shape[0]), m.dot(m.conj().T))


def test_cnot_init():
    from shor.gates import CNOT
    CNOT()


def test_hadamard_init():
    from shor.gates import Hadamard
    Hadamard()


def test_paulix_init():
    from shor.gates import PauliX
    PauliX()


def test_cnot_matrix():
    from shor.gates import CNOT
    g = CNOT()

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]))


def test_hadamard_matrix():
    from shor.gates import Hadamard
    g = Hadamard()

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.multiply(np.divide(1, np.sqrt(2)), np.array([[1, 1], [1, -1]])))


def test_paulix_matrix():
    from shor.gates import PauliX
    g = PauliX()

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[0, 1], [1, 0]]))
