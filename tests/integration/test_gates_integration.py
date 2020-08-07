from shor.gates import Hadamard, PauliX, CCNOT, SWAP, CRZ, CH, S, Sdg, T, Tdg, PauliY, PauliZ, ID, Cx, U1, U3, U2, Rx, Cz, Ry, Rz
from shor.layers import Qubits
from shor.operations import Measure
from shor.quantum import Circuit
from shor.backends import QuantumSimulator, QSession
import numpy as np
import math


def test_ch_integration():
    circuit = Circuit()
    circuit.add(Qubits(2))
    circuit.add(PauliX(0))
    circuit.add(CH(0, 1))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    assert result['11'] > 450
    assert result['00'] == 0
    assert result['10'] > 450
    assert result['01'] == 0


def test_crz_integration():
    circuit = Circuit()
    circuit.add(Qubits(2))
    circuit.add(CRZ(0, 1, angle=math.pi/3))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    assert result['11'] == 0
    assert result['00'] == 1024
    assert result['10'] == 0
    assert result['01'] == 0


def test_dblpx_integration():
    circuit = Circuit()
    circuit.add(Qubits(2))
    circuit.add(PauliX(0))
    circuit.add(PauliX(1))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    assert result['11'] == 1024
    assert result['00'] == 0
    assert result['10'] == 0
    assert result['01'] == 0


def test_swap_integration(): #
    circuit = Circuit()
    circuit.add(Qubits(2))
    circuit.add(PauliX(0))
    circuit.add(SWAP(0,1))
    circuit.add(Measure(0,1))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    assert result['11'] == 0
    assert result['00'] == 0
    assert result['10'] == 0
    assert result['01'] == 1024


#def test_ccnot_integration():
#    circuit = Circuit()
#    circuit.add(Qubits(3))
#    circuit.add(PauliX(0))
#    circuit.add(PauliX(1))
#    circuit.add(CCNOT(0, 1, 2))
#    circuit.add(Measure(0, 1, 2))
#
#    sess = QSession(backend=QuantumSimulator())
#    result = sess.run(circuit, num_shots=1024)
#
#    assert result['000'] == 0
#    assert result['001'] == 0
#    assert result['010'] == 0
#    assert result['100'] == 0
#    assert result['110'] == 0
#    assert result['101'] == 0
#    assert result['011'] == 0
#    assert result['111'] == 1024


def test_s_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(S(0))  # Can also use H()
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    
    assert result['0'] == 1024
    assert result['1'] == 0


def test_sdg_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(PauliX(0))
    circuit.add(Sdg(0))  # Can also use H()
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    
    assert result['1'] == 1024
    assert result['0'] == 0
    

def test_t_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(T(0))  # Can also use H()
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    
    assert result['0'] == 1024
    assert result['1'] == 0


def test_tdg_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(PauliX(0))
    circuit.add(Tdg(0))
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    
    assert result['1'] == 1024
    assert result['0'] == 0


def test_paulix_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(PauliX(0))  # Can also use H()
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    # Accounting for random noise, results won't be exact
    assert result['0'] == 0
    assert result['1'] == 1024


def test_pauliy_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(PauliY(0))  # Can also use H()
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    # Accounting for random noise, results won't be exact
    assert result['0'] == 0
    assert result['1'] == 1024
    

def test_pauliz_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(Hadamard(0))
    circuit.add(PauliZ(0))  # Can also use H()
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    # Accounting for random noise, results won't be exact
    assert result['0'] > 450
    assert result['1'] > 450


def test_ID_qubit():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(ID(0)) 
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    # Accounting for random noise, results won't be exact
    assert result['1'] == 0
    assert result['0'] == 1024


def test_u1_integration():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(PauliX(0))
    circuit.add(U1(0))  
    circuit.add(Measure())

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    assert result['0'] == 0
    assert result['1'] == 1024


def test_cx_int():
    circuit_1 = Circuit()
    circuit_1.add(Qubits(2))
    circuit_1.add(Hadamard(0))
    circuit_1.add(Cx(0, 1))
    circuit_1.add(Measure(0, 1))
    
    circuit_2 = Circuit()
    circuit_2.add(Qubits(2))
    circuit_2.add(Hadamard(1))
    circuit_2.add(Cx(0, 1))
    circuit_2.add(Measure(0, 1))    

    sess = QSession(backend=QuantumSimulator())
    result_1 = sess.run(circuit_1, num_shots=1024)
    result_2 = sess.run(circuit_2, num_shots=1024)
    
    assert result_1['01'] == 0
    assert result_1['10'] > 450
    assert result_1['00'] > 450
    assert result_1['11'] == 0

    assert result_2['01'] == 0
    assert result_2['10'] == 0 
    assert result_2['00'] > 450
    assert result_2['11'] > 450


def test_Cz_int():
    circuit = Circuit()
    circuit.add(Qubits(2))
    circuit.add(Hadamard(0))
    circuit.add(Hadamard(1))
    circuit.add(Cz(0, 1))
    circuit.add(Measure(0, 1))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1000)

    assert result['00'] > 210
    assert result['01'] > 210
    assert result['10'] > 210
    assert result['11'] > 210


def test_ry_int():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(Ry(0, angle=np.pi / 2))
    circuit.add(Measure(0))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1000)

    assert result['0'] > 450
    assert result['1'] > 450


def test_rz_int():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(Rz(0, angle=np.pi / 2))
    circuit.add(Measure(0))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1000)

    assert result['0'] == 1000
    assert result['1'] == 0


def test_U3_int():
    circuit_1 = Circuit()
    circuit_1.add(Qubits(1))
    circuit_1.add(U3(0, theta=np.pi / 2, phi=-np.pi / 2, alpha=np.pi / 2))
    circuit_1.add(Measure(0))

    circuit_2 = Circuit()
    circuit_2.add(Qubits(1))
    circuit_2.add(Rx(theta=np.pi))
    circuit_2.add(Measure(0))

    sess = QSession(backend=QuantumSimulator())
    result_1 = sess.run(circuit_1, num_shots=1024)
    result_2 = sess.run(circuit_2, num_shots=1024)

    assert result_1['0'] > 450
    assert result_1['1'] > 450
    assert result_2['0'] > 450
    assert result_2['1'] > 450


def test_U2_int():
    circuit_1 = Circuit()
    circuit_1.add(Qubits(1))
    circuit_1.add(U2(0, phi=-np.pi / 2, alpha=np.pi / 2))
    circuit_1.add(Measure(0))

    sess = QSession(backend=QuantumSimulator())
    result_1 = sess.run(circuit_1, num_shots=1024)

    assert result_1['0'] > 450
    assert result_1['1'] > 450

