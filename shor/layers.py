class _BaseLayer(object):
    """Abstract base quantum layer class"""

    def __init__(self, **kwargs):
        pass

    def to_gates(self):
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


class Qubits(_BaseLayer):
    def __init__(self, num, state=0, **kwargs):
        self.num = num
        self.state = state

        super().__init__(**kwargs)

    def to_gates(self):
        return []


# Aliasing class
Qbits = Qubits
