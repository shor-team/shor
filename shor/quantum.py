from typing import List

from shor.layers import _BaseLayer


class Circuit:
    def __init__(self):
        self.layers: List[_BaseLayer] = []

    def add(self, layer: _BaseLayer):
        self.layers.append(layer)
