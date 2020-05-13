from shor.gates import CNOT, Hadamard
from shor.layers import Qubits
from shor.operations import Measure
from shor.quantum import Circuit
from shor.backends import QuantumSimulator, QSession


def test_single_qubit():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(Hadamard())  # Can also use H()
    circuit.add(Measure())

    from shor.backends import QuantumSimulator, QSession

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    # Accounting for random noise, results won't be exact
    assert result[bin(0)] > 450
    assert result[bin(1)] > 450


def test_entanglement():
    circuit = Circuit()
    circuit.add(Qubits(2))
    circuit.add(Hadamard(0))
    circuit.add(CNOT(0, 1))
    circuit.add(Measure(0, 1))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    assert result['01'] == 0
    assert result['10'] == 0
    assert result['00'] > 450
    assert result['11'] > 450


def test_unitary_symmetry_does_nothing():
    symmetric_circuit_1 = Circuit()
    symmetric_circuit_1.add(Qubits(2))
    symmetric_circuit_1.add(Hadamard(0))
    symmetric_circuit_1.add(Hadamard(0))
    symmetric_circuit_1.add(CNOT(0, 1))
    symmetric_circuit_1.add(CNOT(0, 1))
    symmetric_circuit_1.add(Measure(0, 1))

    symmetric_circuit_2 = Circuit()
    symmetric_circuit_2.add(Qubits(2, state=1))
    symmetric_circuit_2.add(Hadamard(0))
    symmetric_circuit_2.add(CNOT(0, 1))
    symmetric_circuit_2.add(CNOT(0, 1))
    symmetric_circuit_2.add(Hadamard(0))
    symmetric_circuit_2.add(Measure(0, 1))

    sess = QSession(backend=QuantumSimulator())
    result_1 = sess.run(symmetric_circuit_1, num_shots=1024)
    result_2 = sess.run(symmetric_circuit_2, num_shots=1024)

    assert result_1.counts.get(0) == 1024
    assert result_2.counts.get(3) == 1024
