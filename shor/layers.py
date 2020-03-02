
class _Layer:
    """Abstract base quantum layer class

    # Properties
    inputs = indices of qubits, to be used as inputs.
    """

    def __init__(self, **kwargs):
        self.inputs = kwargs.get('inputs', None)
        self.output_shape = kwargs.get('output_shape', [0])

    def to_gates(self):
        pass


class Qubits(_Layer):
    def __init__(self, num):
        super().__init__(output_shape=(num,))
