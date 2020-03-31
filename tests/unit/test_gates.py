import numpy as np


def is_square(m):
    return m.shape[0] == m.shape[1] and len(m.shape) == 2


def is_unitary(m):
    return np.allclose(np.eye(m.shape[0]), m.dot(m.conj().T))


def test_cnot_init():
    from shor.gates import CNOT
    CNOT()


def test_hadamard_init():
    from shor.gates import Hadamard, H
    gate1 = H()
    gate2 = Hadamard()

    assert gate1.__class__ == gate2.__class__

    # Try with parameter
    H(0)


def test_paulix_init():
    from shor.gates import PauliX, X
    gate1 = X()
    gate2 = PauliX()
    assert gate1.__class__ == gate2.__class__
    # Try with parameter
    X(0)


def test_cnot_matrix():
    from shor.gates import CNOT
    g = CNOT()

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]))

    # Try with parameter
    CNOT(1, 0)


def test_cswap_matrix():
    from shor.gates import CSWAP, Fredkin
    g = CSWAP()

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())

    expected = np.eye(8)
    expected[:, [5, 6]] = expected[:, [6, 5]]
    assert np.array_equal(g.to_matrix(), expected)

    # Try with parameter
    CSWAP(2, 0, 1)


def test_hadamard_matrix():
    from shor.gates import Hadamard, H
    gates = [Hadamard(), H()]

    for g in gates:
        assert is_square(g.to_matrix())
        assert is_unitary(g.to_matrix())
        assert np.array_equal(g.to_matrix(), np.multiply(np.divide(1, np.sqrt(2)), np.array([[1, 1], [1, -1]])))


def test_paulix_matrix():
    from shor.gates import PauliX, X
    gates = [PauliX(), X()]

    for g in gates:
        assert is_square(g.to_matrix())
        assert is_unitary(g.to_matrix())
        assert np.array_equal(g.to_matrix(), np.array([[0, 1], [1, 0]]))
