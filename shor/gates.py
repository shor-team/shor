import numpy as np

from shor.layers import _BaseLayer


class _Gate(_BaseLayer):
    """Abstract base quantum gate class

    # Properties
    input_length = valid length of input qubits
    qubits = indices of qubits, to be used as input to gate.
    """

    def __init__(self, *qubits: int, **kwargs):
        super().__init__(**kwargs)
        self.dimension = kwargs.get('dimension', 1)
        self.qubits = qubits if qubits else [0]

        assert all(map(lambda q: type(q) == int, self.qubits))
        assert len(self.qubits) == self.dimension

    def to_gates(self):
        return [self]


class CNOT(_Gate):
    def __init__(self, *qubits, **kwargs):
        kwargs['dimension'] = 2
        if not qubits:
            qubits = [0, 1]

        super().__init__(*qubits, **kwargs)

    @staticmethod
    def to_matrix() -> np.ndarray:
        return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


class CSWAP(_Gate):
    def __init__(self, *qubits, **kwargs):
        kwargs['dimension'] = 3
        if not qubits:
            qubits = [0, 1, 2]

        super().__init__(*qubits, **kwargs)

    @staticmethod
    def to_matrix() -> np.ndarray:
        cswap_matrix = np.eye(8)
        cswap_matrix[:, [5, 6]] = cswap_matrix[:, [6, 5]]
        return cswap_matrix



class Hadamard(_Gate):
    def __init__(self, *qubits, **kwargs):
        kwargs['dimension'] = 1
        if not qubits:
            qubits = [0]

        super().__init__(*qubits, **kwargs)

    @staticmethod
    def to_matrix() -> np.ndarray:
        return np.multiply(np.divide(1, np.sqrt(2)), np.array([[1, 1], [1, -1]]))


class PauliX(_Gate):
    def __init__(self, *qubits, **kwargs):
        kwargs['dimension'] = 1
        if not qubits:
            qubits = [0]

        super().__init__(*qubits, **kwargs)

    @staticmethod
    def to_matrix() -> np.ndarray:
        return np.array([[0, 1], [1, 0]])


# Aliases
H = h = Hadamard
X = x = PauliX
CX = cx = CNOT
Fredkin = cswap = CSWAP
