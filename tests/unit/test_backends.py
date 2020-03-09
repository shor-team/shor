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
