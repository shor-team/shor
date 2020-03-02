from typing import List

from shor.gates import _Gate


class Circuit:
    def __init__(self):
        self.layers: List[_Gate] = []

    def add(self, layer: _Gate):
        self.layers.append(layer)


class QSession:
    def __init__(self):
        pass
