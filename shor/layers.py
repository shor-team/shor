class _BaseLayer:
    """Abstract base quantum layer class"""

    def __init__(self, **kwargs):
        pass


class _Layer(_BaseLayer):
    """Abstract base quantum layer class

    # Properties
    inputs = indices of qubits, to be used as inputs.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_gates(self):
        pass


class Qubits(_Layer):
    def __init__(self, num):
        super().__init__(output_shape=(num,))
