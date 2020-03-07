import numpy as np

from shor.layers import _BaseLayer


class _Gate(_BaseLayer):
    """Abstract base quantum gate class

    # Properties
    inputs = indices of qubits, to be used as inputs.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_matrix(self):
        pass


class CNOT(_Gate):
    def to_matrix(self):
        return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


class Hadamard(_Gate):
    def to_matrix(self):
        return np.multiply(np.divide(1, np.sqrt(2)), np.array([[1, 1], [1, -1]]))


class PauliX(_Gate):
    def to_matrix(self):
        return np.array([[0, 1], [1, 0]])


# Aliases
H = Hadamard
X = PauliX
