from shor.gates import H
from shor.layers import Qbits
from shor.operations import Measure
from shor.quantum import QuantumCircuit


def test_apis():
    qbits = Qbits(4)
    # Qbit
    # id
    # name

    # Implements iterable, so we get all of the nice
    # python indexing functionality
    # even = qbits[::2]  # Get the even indexed qbits
    # odd = qbits[1::2]  # Get the odd indexed qbits

    # TODO: Support multiple qbits, and this test.
    # TODO: Add empty circuit test
    # TODO: Infer qbits used from ciruit rather than from Qbits layer
    # H(even) does not work.

    qc = QuantumCircuit()
    qc += Qbits(1)
    # qc += H(even)
    # qc += X(odd)
    qc += H(0)
    qc.add(Measure([qbits]))

    job = qc.run(100)
    result = job.result

    assert result["1111"] == 0
    # Any single qbit should accept
    # A single qbit
    H(qbits[1])
    # TODO: An iterable / list of qbits
    # H(qbits[0:5])

    # Control(H(qbits[1]), qbits[0])


#
# qc2 = QuantumCircuit() + H(qbits[0]) + X(qbits[1])
#
# qbits = Qbits(4)
# qc = H(qbits) * QFT(qbits)
#
# qc += QFT(qbits[0:3])
# qc += qc2
#
# qc.add(H())
#
# qc = H(qc[0:3])
# qc = Z(qc[1])
#
# qbits = Qbits(4)
# cbits = Cbits(4)
#
# qc = QuantumCircuit(qbits=qbits, cbits=cbits)
# -> err
# qc += Hadamard(qbits[0]) + Z(qbits[1])
#
# qc.add(Measure([qbits[0]]))
# qc += Measure(qbits[0])
#
# qc.add(Measure(qbits), name='Output')
