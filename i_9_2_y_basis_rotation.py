# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np


def prepare_psi():
    qp.StatePrep(np.array([1 / 2, 1j * np.sqrt(3) / 2]), wires=0)


def y_basis_rotation():
    qp.Hadamard(wires=0)
    qp.S(wires=0)


if __name__ == "__main__":
    dev = qp.device("default.qubit", wires=1)

    @qp.qnode(dev)
    def psi():
        prepare_psi()
        return qp.state()

    print(psi())
    print(qp.matrix(y_basis_rotation, wire_order=[0])())
