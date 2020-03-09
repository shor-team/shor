from shor.quantum import Circuit

import os
import pydot


def plot_circuit(circuit: Circuit, to_file='model.png'):
    """ Converts a Quantum Circuit into a diagram, and saves to a file

    Args:
        circuit: A quantum :func:`Circuit() <shor.quantum.Circuit>` object
        to_file: File name of the plot image.

    Returns:
        A Jupyter notebook Image object if Jupyter is installed.
        This enables in-line display of the circuit diagram in notebooks.
    """
    pass


def circuit_to_dot(circuit: Circuit):
    """ Converts a Quantum Circuit into Dot format
    See: pydot

    Args:
        circuit: A shor.quantum.Circuit object
    """
    pass