from typing import List, Union

import numpy as np

from shor.gates import _Gate
from shor.layers import _Layer, Qbits
from shor.operations import Measure, _Operation


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

    def to_gates(self, include_operations=False) -> List[_Gate]:
        gates = []
        for layer in self.layers:
            operation_or_gates = [layer] if include_operations and isinstance(layer, _Operation) else layer.to_gates()

            gates.extend(operation_or_gates)
        return gates

    def measure_bits(self):
        measure_bits = []
        for m in filter(lambda l: type(l) == Measure, self.layers):
            measure_bits.extend(m.qbits)
        return measure_bits

    def __add__(self, other):
        return self.add(other)

    def run(self, num_shots: int,  provider: 'Provider' = None, **kwargs):
        if provider is None:
            from shor.providers.ShorSimulator import ShorSimulator
            provider = ShorSimulator()

        return provider.run(self, num_shots)


# Aliases
Circuit = QC = QuantumCircuit
