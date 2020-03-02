def test_circuit_init():
    from shor.quantum import Circuit
    Circuit()


def test_circuit_add_layer():
    from shor.quantum import Circuit
    from shor.layers import _Layer
    circuit = Circuit()
    prev_num_layers = len(circuit.layers)
    circuit.add(_Layer())

    assert len(circuit.layers) == prev_num_layers + 1


def test_circuit_add_gate():
    from shor.quantum import Circuit
    from shor.gates import _Gate
    circuit = Circuit()
    prev_num_gates = len(circuit.gates)
    circuit.add(_Gate())

    assert len(circuit.gates) == prev_num_gates + 1


def test_qsession_init():
    from shor.quantum import QSession
    QSession()
