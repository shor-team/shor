import pytest

from shor.quantum import Circuit
from shor.layers import _BaseLayer


def test_circuit_init():
    Circuit()


def test_circuit_add_base_layer():
    circuit = Circuit()
    prev_num_layers = len(circuit.layers)
    circuit.add(_BaseLayer())

    assert len(circuit.layers) == prev_num_layers + 1


def test_circuit_add_returns_self():

    circuit1 = Circuit()
    circuit2 = circuit1.add(_BaseLayer())

    assert circuit1 == circuit2


def test_circuit_add_circuit():
    circuit = Circuit().add(_BaseLayer()).add(_BaseLayer())

    circuit_to_add = Circuit()
    circuit_to_add.add(_BaseLayer()).add(_BaseLayer()).add(_BaseLayer())

    assert len(circuit.layers) == 2
    circuit.add(circuit_to_add)

    assert len(circuit.layers) == 5


def test_circuit_add_wrong_type():
    class SomeClass(object):
        def __init__(self):
            pass

    with pytest.raises(TypeError) as type_error:
        circuit = Circuit().add(SomeClass())