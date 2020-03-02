def test_circuit_init():
    from shor.quantum import Circuit
    circuit = Circuit()


def test_circuit_add():
    from shor.quantum import Circuit
    from shor.layers import Qubits
    circuit = Circuit()
    circuit.add(Qubits(3))


def test_qsession_init():
    from shor.quantum import QSession
    QSession()
