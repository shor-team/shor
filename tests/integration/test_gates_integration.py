#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:39:44 2020

@author: zevunderwood
"""

from shor.gates import Hadamard, PauliX, CCNOT, SWAP, CRZ,CH
from shor.layers import Qubits
from shor.operations import Measure
from shor.quantum import Circuit
from shor.backends import QuantumSimulator, QSession
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


def test_ccnot_integration():
    circuit = Circuit()
    circuit.add(Qubits(3))
    circuit.add(PauliX(0))
    circuit.add(PauliX(1))
    circuit.add(CCNOT(0, 1, 2))
    circuit.add(Measure(0, 1, 2))

    sess = QSession(backend=QuantumSimulator())
    result = sess.run(circuit, num_shots=1024)

    assert result['000'] == 0
    assert result['001'] == 0
    assert result['010'] == 0
    assert result['100'] == 0
    assert result['110'] == 0
    assert result['101'] == 0
    assert result['011'] == 0
    assert result['111'] == 1024