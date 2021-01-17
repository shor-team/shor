from typing import List

from qiskit import Aer, QuantumCircuit, execute

from shor.operations import _Operation
from shor.providers.base import Job, Provider, Result
from shor.quantum import QC
from shor.utils.qbits import int_from_bit_string

DEFAULT_BACKEND = Aer.get_backend("qasm_simulator")


class IBMQResult(Result):
    def __init__(self, ibmq_result):
        self.ibmq_result = ibmq_result

    @property
    def counts(self):
        return {int_from_bit_string(k.split(" ")[0]): v for k, v in self.ibmq_result.get_counts().items()}

    @property
    def sig_bits(self):
        measurement_bases = list(self.ibmq_result.get_counts().keys())
        return len(measurement_bases[0]) if measurement_bases else 0


class IBMQJob(Job):
    def __init__(self, ibmq_job):
        self.ibmq_job = ibmq_job

    @property
    def status(self):
        return self.ibmq_job.status()

    @property
    def result(self) -> IBMQResult:
        return IBMQResult(self.ibmq_job.result())


class IBMQProvider(Provider):
    def __init__(self, **config):
        self.backend = config.get("backend", DEFAULT_BACKEND)
        # register(config['APItoken'], config['url'])

    @property
    def jobs(self) -> List[Job]:
        return list(map(lambda j: IBMQJob(j), self.backend.get_jobs()))

    def run(self, circuit: QC, times: int) -> IBMQJob:
        job = execute(self._to_qiskit_circuit(circuit), self.backend, shots=times)

        return IBMQJob(job)

    @staticmethod
    def _to_qiskit_circuit(quantum_circuit: QC) -> QuantumCircuit:
        qiskit_circuit = QuantumCircuit(
            len(quantum_circuit.initial_state()),
            len(quantum_circuit.measure_bits()),
        )

        for gate_or_op in quantum_circuit.to_gates(include_operations=True):
            transpile_gate(qiskit_circuit, gate_or_op)

        return qiskit_circuit


def ibmq_symbol(shor_gate):
    return shor_gate.symbol.lower()


def transpile_gate(qiskit_circuit, shor_gate):
    symbol = ibmq_symbol(shor_gate)

    if isinstance(shor_gate, _Operation):
        if symbol == "measure":
            if len(shor_gate.qbits) == len(shor_gate.bits) == qiskit_circuit.size():
                qiskit_circuit.measure_active()
            else:
                for qbit, bit in zip(shor_gate.qbits, shor_gate.bits):
                    qiskit_circuit.measure(qbit, bit)

        return

    args = []
    kwargs = {}

    if symbol in ["crx", "cry", "crz", "cu1", "rx", "ry", "rz", "u1"]:
        args.append(shor_gate.angle)
    if symbol == "u3":
        args.append(shor_gate.theta)
    if symbol in ["u2", "u3"]:
        args.append(shor_gate.phi)
        args.append(shor_gate.lam)

    args.extend(shor_gate.qbits)
    qiskit_circuit.__getattribute__(symbol)(*args, **kwargs)
