from shor.quantum import Circuit


class _QuantumBackend:
    pass


class QuantumSimulator(_QuantumBackend):
    pass


class QSession:
    def __init__(self, **kwargs):
        self.backend = kwargs.get('backend', QuantumSimulator)

    def run(self, circuit: Circuit):
        pass
