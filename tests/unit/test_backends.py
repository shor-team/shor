from shor.gates import H
from shor.layers import Qbits


def test_quantum_backend_init():
    from shor.backends import _QuantumBackend
    _QuantumBackend()


def test_quantum_simulator_init():
    from shor.backends import QuantumSimulator
    QuantumSimulator()


def test_qsession_init():
    from shor.backends import QSession
    QSession()


def test_qsession_run():
    from shor.backends import QSession
    sess = QSession()

    from shor.quantum import Circuit
    sess.run(Circuit().add(Qbits(1)).add(H()), num_shots=10)


def test_qresult_str_representation():
    from shor.backends import QResult

    result = QResult({0: 20, 7: 34}, 5)

    assert str(result) == repr(result) == "{'00000': 20, '00111': 34}"


def test_qresult_get():
    from shor.backends import QResult

    result = QResult({0: 20, 7: 34}, 5)

    assert 20 == result['00000'] == result['0'] == result[0] == result[0b00000] == result.get(0)
    assert 34 == result['00111'] == result['111'] == result[7] == result[0b00111] == result[0b111] == result.get(7)
