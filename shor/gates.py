from shor.layers import _BaseLayer


class _Gate(_BaseLayer):
    """Abstract base quantum gate class

    # Properties
    inputs = indices of qubits, to be used as inputs.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_matrix(self, input_shape):
        pass


class CNOT(_Gate):
    pass


class Hadamard(_Gate):
    pass


class PauliX(_Gate):
    pass
