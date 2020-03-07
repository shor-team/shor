def test_circuit_init():
    from shor.quantum import Circuit
    Circuit()


def test_circuit_add_base_layer():
    from shor.quantum import Circuit
    from shor.layers import _BaseLayer
    circuit = Circuit()
    prev_num_layers = len(circuit.layers)
    circuit.add(_BaseLayer())

    assert len(circuit.layers) == prev_num_layers + 1


def test_circuit_add_returns_self():
    from shor.quantum import Circuit
    from shor.layers import _BaseLayer

    circuit1 = Circuit()
    circuit2 = circuit1.add(_BaseLayer())

    assert circuit1 == circuit2

