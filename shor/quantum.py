from typing import List, Union

import numpy as np

from shor.layers import _Layer, Qbits
from shor.operations import Measure


class QuantumCircuit(object):
    def __init__(self):
        self.layers: List[_Layer] = []

    def add(self, layer_or_circuit: Union[_Layer, 'QuantumCircuit']):
        if isinstance(layer_or_circuit, _Layer):
            self.layers.append(layer_or_circuit)
        elif isinstance(layer_or_circuit, QuantumCircuit):
            self.layers.extend(layer_or_circuit.layers)
        else:
            raise TypeError("QuantumCircuit class cannot add the type: {}".format(type(layer_or_circuit)))

        return self

    def initial_state(self) -> np.ndarray:
        initial_qubits = []
        for qbit_layer in filter(lambda layer: type(layer) == Qbits, self.layers):
            initial_qubits.extend([qbit_layer.state] * qbit_layer.num)

        return initial_qubits

    def to_gates(self):
        gates = []
        for layer in self.layers:
            gates.extend(layer.to_gates())
        return gates

    def measure_bits(self):
        measure_bits = []
        for m in filter(lambda l: type(l) == Measure, self.layers):
            measure_bits.extend(m.bits)
        return measure_bits

    def __add__(self, other):
        return self.add(other)

    def run(self, num_shots: int,  backend: '_QuantumBackend' = None, **kwargs):
        if backend is None:
            from shor.backends import QuantumSimulator
            backend = QuantumSimulator()

        return backend.run(self.initial_state(), self.to_gates(), self.measure_bits(), num_shots, **kwargs)


# Aliases
Circuit = QC = QuantumCircuit
