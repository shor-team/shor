from shor.layers import _Layer


class _Operation(_Layer):
    """Abstract base quantum computing operation class
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_gates(self):
        return []


class Measure(_Operation):
    symbol = 'measure'

    def __init__(self, qbits=None, bits=None, axis='z', **kwargs):
        if not qbits:
            qbits = [0]
        if not bits:
            bits = qbits[:]

        self.qbits = qbits
        self.bits = bits

        super().__init__(**kwargs, axis=axis)


# Aliases
M = m = Measure
