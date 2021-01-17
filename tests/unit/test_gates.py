import math

import numpy as np

from tests.util import is_square, is_unitary


def test_cnot_init():
    from shor.gates import CNOT

    CNOT()


def test_hadamard_init():
    from shor.gates import H, Hadamard

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


def test_pauliy_init():
    from shor.gates import PauliY, Y

    gate1 = Y()
    gate2 = PauliY()
    assert gate1.__class__ == gate2.__class__
    # Try with parameter
    Y(0)


def test_pauliz_init():
    from shor.gates import PauliZ, Z

    gate1 = Z()
    gate2 = PauliZ()
    assert gate1.__class__ == gate2.__class__
    # Try with parameter
    Z(0)


def test_qft_init():
    from shor.gates import QFT

    QFT(0, 1)


def test_swap_init():
    from shor.gates import SWAP

    SWAP()

    # Try with parameters
    SWAP(1, 0)


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

    gate1 = CSWAP()
    gate2 = Fredkin()

    assert gate1.__class__ == gate2.__class__

    assert is_square(gate1.to_matrix())
    assert is_unitary(gate1.to_matrix())

    expected = np.eye(8)
    expected[:, [5, 6]] = expected[:, [6, 5]]
    assert np.array_equal(gate1.to_matrix(), expected)

    # Try with parameter
    CSWAP(2, 0, 1)


def test_hadamard_matrix():
    from shor.gates import H, Hadamard

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


def test_qft_matrix():
    from shor.gates import QFT

    g = QFT(0, 1)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(), np.multiply(1 / 2, np.array([[1, 1, 1, 1], [1, 1j, -1, -1j], [1, -1, 1, -1], [1, -1j, -1, 1j]]))
    )


def test_swap_matrix():
    from shor.gates import SWAP

    g = SWAP(0, 1)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]))


def test_ccnot_matrix():
    from shor.gates import CCNOT

    g = CCNOT(0, 1, 2)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(),
        np.array(
            [
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
            ]
        ),
    )


def test_crz_matrix():
    from shor.gates import CRZ

    angle = np.pi / 3
    g = CRZ(0, 1, angle=np.pi / 3)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(),
        np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.exp(-1j * angle / 2), 0], [0, 0, 0, np.exp(1j * angle / 2)]]),
    )


def test_ch_matrix():
    from shor.gates import CH

    g = CH(0, 1)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(),
        np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1 / np.sqrt(2), 1 / np.sqrt(2)],
                [0, 0, 1 / np.sqrt(2), -1 / np.sqrt(2)],
            ]
        ),
    )


def test_s_matrix():
    from shor.gates import S

    g = S(0)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0], [0, 1j]]))


def test_sdg_matrix():
    from shor.gates import Sdg

    g = Sdg(0)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0], [0, -1j]]))


def test_t_matrix():
    from shor.gates import T

    g = T(0)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.allclose(g.to_matrix(), np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]]))


def test_tdg_matrix():
    from shor.gates import Tdg

    g = Tdg(0)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.allclose(g.to_matrix(), np.array([[1, 0], [0, np.exp(-1j * np.pi / 4)]]))


def test_ID_matrix():
    from shor.gates import ID

    g = ID(0)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0], [0, 1]]))


def test_u1_matrix():
    from shor.gates import U1

    angle = math.pi / 8
    g = U1(0, angle=math.pi / 8)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0], [0, np.exp(1j * angle)]]))


def test_cx_matrix():
    from shor.gates import Cx

    g = Cx(0, 1)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]))


def test_cz_matrix():
    from shor.gates import Cz

    g = Cz(0, 1)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]]))


def test_rx():
    from shor.gates import Rx

    angle = math.pi / 8
    g = Rx(0, angle=math.pi / 8)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())

    assert np.array_equal(
        g.to_matrix(),
        np.array([[math.cos(angle / 2), -math.sin(angle / 2) * 1j], [-math.sin(angle / 2) * 1j, math.cos(angle / 2)]]),
    )


def test_ry():
    from shor.gates import Ry

    angle = math.pi / 8
    g = Ry(0, angle=math.pi / 8)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())

    assert np.array_equal(
        g.to_matrix(),
        np.array([[math.cos(angle / 2), -math.sin(angle / 2)], [math.sin(angle / 2), math.cos(angle / 2)]]),
    )


def test_rz_matrix():
    from shor.gates import Rz

    angle = math.pi / 4
    g = Rz(0, angle=math.pi / 4)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(), np.array([[np.exp(-(1 / 2) * 1j * angle), 0], [0, np.exp((1 / 2) * 1j * angle)]])
    )


def test_u3_matrix():
    from shor.gates import U3

    theta = np.pi / 2
    phi = -np.pi / 3
    lam = np.pi / 2

    g = U3(0, theta=np.pi / 2, phi=-np.pi / 3, lam=np.pi / 2)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(),
        np.array(
            [
                [np.cos(theta / 2), -np.exp(1j * lam) * math.sin(theta / 2)],
                [np.exp(1j * phi) * math.sin(theta / 2), np.exp(1j * (phi + lam)) * math.cos(theta / 2)],
            ]
        ),
    )


def test_u2_matrix():
    from shor.gates import U2

    phi = -np.pi / 3
    lam = np.pi / 2
    theta = np.pi / 2

    g = U2(0, phi=-np.pi / 3, lam=np.pi / 2)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(),
        np.array(
            [
                [np.cos(theta / 2), -np.exp(1j * lam) * math.sin(theta / 2)],
                [np.exp(1j * phi) * math.sin(theta / 2), np.exp(1j * (phi + lam)) * math.cos(theta / 2)],
            ]
        ),
    )
    assert np.allclose(
        g.to_matrix(),
        (1 / np.sqrt(2)) * np.array([[1, -np.exp(1j * lam)], [np.exp(1j * phi), np.exp(1j * (phi + lam))]]),
    )


def test_cr_matrix():
    from shor.gates import Cr

    angle = np.pi / 2
    g = Cr(0, 1, angle=np.pi / 2)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(), np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, np.exp(1j * angle)]])
    )


def test_crk_matrix():
    from shor.gates import CRk

    k = 2
    g = CRk(0, 1, k=2)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(
        g.to_matrix(),
        np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, np.exp((2 * np.pi * 1j) / (2 ** k))]]),
    )


def test_cy_matrix():
    from shor.gates import CY

    g = CY(0, 1)

    assert is_square(g.to_matrix())
    assert is_unitary(g.to_matrix())
    assert np.array_equal(g.to_matrix(), np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1j], [0, 0, 1j, 0]]))
