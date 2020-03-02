class _Gate:
    """Abstract base quantum gate class

    # Properties
    inputs = indices of qubits, to be used as inputs.
    """

    def __init__(self, **kwargs):
        self.inputs = kwargs.get('inputs', None)
        self.output_shape =  kwargs.get('output_shape', [0])

    def to_matrix(self, input_shape):
        pass


class CNOT(_Gate):
    pass


class Hadamard(_Gate):
    pass


class PauliX(_Gate):
    pass
