from typing import List

from shor.providers.base import Provider, Job, Result

from qiskit import execute, Aer, QuantumCircuit

from shor.quantum import QC
from shor.utils.qbits import int_from_bit_string

DEFAULT_BACKEND = Aer.get_backend('qasm_simulator')


class IBMQResult(Result):
    def __init__(self, ibmq_result):
        self.ibmq_result = ibmq_result

    @property
    def counts(self):
        return {int_from_bit_string(k) for k,v in self.ibmq_result.get_counts()}

    @property
    def sig_bits(self):
        return len(self.ibmq_result.get_counts.keys().get(0, ''))


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
        self.backend = config.get('backend', DEFAULT_BACKEND)
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
            len(quantum_circuit.initial_state()),  # Measuring all here, it appears that bit order is reversed (sig bit on left)
        )

        for gate in quantum_circuit.to_gates():
            qiskit_circuit.__getattribute__(gate.symbol)(*gate.qbits)

        qiskit_circuit.measure_all()

        return qiskit_circuit
