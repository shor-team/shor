def test_quantum_backend_init():
    from shor.backends import _QuantumBackend
    _QuantumBackend()


def test_quantum_simulator_init():
    from shor.backends import QuantumSimulator
    QuantumSimulator()


def test_qsession_init():
    from shor.backends import QSession
    QSession()
