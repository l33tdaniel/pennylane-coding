# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

num_wires = 3
dev = qp.device("default.qubit", wires=num_wires)


@qp.qnode(dev)
def three_qubit_QFT(basis_id):
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1, 2])

    qp.Hadamard(wires=0)
    qp.ctrl(qp.S, control=1)(wires=0)
    qp.ctrl(qp.T, control=2)(wires=0)
    qp.Hadamard(wires=1)
    qp.ctrl(qp.S, control=2)(wires=1)
    qp.Hadamard(wires=2)
    qp.SWAP(wires=[0, 2])

    return qp.state()


if __name__ == "__main__":
    for basis_id in range(2**num_wires):
        print(basis_id, three_qubit_QFT(basis_id))
