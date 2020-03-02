def test_single_qubit():
    from shor.quantum import Circuit
    from shor.gates import Hadamard

    circuit = Circuit(qbits=[0])
    circuit.add(Hadamard)

    from shor.backends import QuantumSimulator
    from shor.quantum import QSession

    sess = QSession(backend=QuantumSimulator)
    result = sess.run(circuit, num_shots=1024)

    # Accounting for random noise, results won't be exact
    assert result.counts[0] > 450
    assert result.counts[1] > 450


def test_entanglement():
    from shor.quantum import Circuit
    from shor.gates import CNOT, Hadamard
    from shor.layers import Qubits
    from shor.operations import Measure

    circuit = Circuit()
    circuit.add(Qubits(2))
    circuit.add(Hadamard(0))
    circuit.add(CNOT(0, 1))
    circuit.add(Measure(0, 1))

    from shor.backends import QuantumSimulator
    from shor.quantum import QSession

    sess = QSession(backend=QuantumSimulator)
    result = sess.run(circuit, num_shots=1024)

    # Accounting for random noise, results won't be exact
    # For result index:
    #     - int('10',2)
    #     - 0b10
    #     - 2
    # are all equivalant ways to get the index for '|10>'
    assert result.counts[0b01] == 0
    assert result.counts[0b10] == 0
    assert result.counts[0b00] > 450
    assert result.counts[0b11] > 450
