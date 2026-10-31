# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=4)


def swap_bits(n_qubits):
    for wire in range(n_qubits // 2):
        qp.SWAP(wires=[wire, n_qubits - wire - 1])


@qp.qnode(dev)
def qft_node(basis_id, n_qubits):
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))
    # qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qp.state()


if __name__ == "__main__":
    print(qp.draw(qft_node)(1, 4))
    print(qft_node(1, 4))
