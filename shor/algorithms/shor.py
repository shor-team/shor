from shor.gates import Hadamard, X, CNOT
from shor.layers import Qubits
from shor.operations import Measure
from shor.quantum import Circuit


def factor(N):
    pass



def find_period(a, N):
    """ Quantum subroutine for shor's algorithm.
    Finds the period of a function of the form:
    f(x) = a^x % N

    This uses the quantum fourier transform.
    """

    circuit = Circuit()
    circuit.add(Qubits(4))
    circuit.add(X(2))
    circuit.add(CNOT(2, 1))
    circuit.add(CNOT(1, 2))
    circuit.add(CNOT(2, 1))
    circuit.add(CNOT(1, 0))
    circuit.add(CNOT(0, 1))
    circuit.add(CNOT(1, 0))
    circuit.add(CNOT(3, 0))
    circuit.add(CNOT(0, 3))
    circuit.add(CNOT(3, 0))
    circuit.add(Measure(0, 1, 2, 3))

    from shor.backends import QuantumSimulator, QSession

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)


def amod(a, qbits=4):

# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)

# Construct unitary based on a
	if a == 2:
		qc.cswap(qr[4],qr[3],qr[2])
		qc.cswap(qr[4],qr[2],qr[1])
		qc.cswap(qr[4],qr[1],qr[0])
	if a == 4 or a == 11 or a == 14:
		qc.cswap(qr[4],qr[2],qr[0])
		qc.cswap(qr[4],qr[3],qr[1])
		qc.cx(qr[4],qr[3])
		qc.cx(qr[4],qr[2])
		qc.cx(qr[4],qr[1])
		qc.cx(qr[4],qr[0])
	if a == 7:
		qc.cswap(qr[4],qr[1],qr[0])
		qc.cswap(qr[4],qr[2],qr[1])
		qc.cswap(qr[4],qr[3],qr[2])
		qc.cx(qr[4],qr[3])
		qc.cx(qr[4],qr[2])
		qc.cx(qr[4],qr[1])
		qc.cx(qr[4],qr[0])
	if a == 8:
		qc.cswap(qr[4],qr[1],qr[0])
		qc.cswap(qr[4],qr[2],qr[1])
		qc.cswap(qr[4],qr[3],qr[2])
	if a == 13:
		qc.cswap(qr[4],qr[3],qr[2])
		qc.cswap(qr[4],qr[2],qr[1])
		qc.cswap(qr[4],qr[1],qr[0])
		qc.cx(qr[4],qr[3])
		qc.cx(qr[4],qr[2])
		qc.cx(qr[4],qr[1])
		qc.cx(qr[4],qr[0])