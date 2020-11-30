"""
Created on Wed Jul  8 10:36:57 2020

@author: zevunderwood
"""
import numpy as np

from shor.gates import Ry
from shor.layers import Qubits
from shor.operations import Measure
from shor.quantum import Circuit


def test_ry_int():
    circuit = Circuit()
    circuit.add(Qubits(1))
    circuit.add(Ry(0, angle=np.pi / 2))
    circuit.add(Measure([0]))
    job = circuit.run(1000)
    result = job.result
    assert result["0"] > 450
    assert result["1"] > 450
