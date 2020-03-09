from shor.layers import _BaseLayer


class _Operation(_BaseLayer):
    """Abstract base quantum computing operation class
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_gates(self):
        return []


class Measure(_Operation):
    def __init__(self, *bits, axis='z', **kwargs):
        if not bits:
            bits = [0]
        self.bits = bits

        super().__init__(**kwargs, axis=axis)
