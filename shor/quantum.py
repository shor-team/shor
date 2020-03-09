from typing import List

from shor.layers import _BaseLayer, Qubits
from shor.operations import Measure


class Circuit:
    def __init__(self):
        self.layers: List[_BaseLayer] = []

    def add(self, layer: _BaseLayer):
        self.layers.append(layer)

        return self

    def initial_state(self):
        initial_qubits = []
        for ql in filter(lambda l: type(l) == Qubits, self.layers):
            initial_qubits.extend([ql.state] * ql.num)

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