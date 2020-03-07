
class _Operation:
    """Abstract base quantum computing operation class
    """

    def __init__(self, **kwargs):
        pass


class Measure(_Operation):
    def __init__(self, axis='z'):
        super().__init__(axis=axis)
