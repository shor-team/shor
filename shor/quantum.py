from typing import List

from shor.backends import QuantumSimulator
from shor.gates import _Gate
from shor.layers import _Layer


class Circuit:
    def __init__(self):
        self.gates: List[_Gate] = []
        self.layers: List[_Layer] = []

    def add(self, layer: _Gate):
        self.layers.append(layer)


class QSession:
    def __init__(self, **kwargs):
        self.backend = kwargs.get('backend', QuantumSimulator)

    def run(self, circuit: Circuit):
        pass
