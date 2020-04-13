from typing import List, Union


from shor.layers import _BaseLayer, Qubits
from shor.operations import Measure


class Circuit(object):
    def __init__(self):
        self.layers: List[_BaseLayer] = []

    def add(self, layer_or_circuit: Union[_BaseLayer, 'Circuit']):

        if isinstance(layer_or_circuit, _BaseLayer):
            self.layers.append(layer_or_circuit)
        elif isinstance(layer_or_circuit, Circuit):
            self.layers.extend(layer_or_circuit.layers)
        else:
            raise TypeError("Circuit class cannot add the type: {}".format(type(layer_or_circuit)))

        return self

    def initial_state(self):
        initial_qubits = []
        for qbit_layer in filter(lambda l: type(l) == Qubits, self.layers):
            initial_qubits.extend([qbit_layer.state] * qbit_layer.num)

        return initial_qubits

    def to_gates(self):
        gates = []
        for l in self.layers:
            gates.extend(l.to_gates())
        return gates

    def measure_bits(self):
        measure_bits = []
        for m in filter(lambda l: type(l) == Measure, self.layers):
            measure_bits.extend(m.bits)
        return measure_bits
