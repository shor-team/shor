from shor.gates import H, CNOT
from shor.layers import Qbits
from shor.operations import Measure
from shor.providers import IBMQProvider
from shor.quantum import QC


def test_ibmq_backend_simulator():
    qc = QC()
    qc.add(Qbits(3))
    qc.add(H(1))
    qc.add(CNOT(1, 0))
    qc.add(Measure(0, 1))

    ibm_provider = IBMQProvider()
    job = qc.run(1024, ibm_provider)
    result = job.result
    counts = result.counts

    print(counts)
