# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

from f_3_2_swapping_qubits import swap_bits

dev = qp.device("default.qubit", wires=4)


def qft_rotations(n_qubits):
    for target in range(n_qubits):
        qp.Hadamard(wires=target)
        for control in range(target + 1, n_qubits):
            k = control - target + 1
            qp.ControlledPhaseShift(2 * np.pi / 2**k, wires=[control, target])


@qp.qnode(dev)
def qft_node(basis_id, n_qubits):
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))
    qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qp.state()


if __name__ == "__main__":
    print(qp.draw(qft_node)(3, 4))
    print(qft_node(3, 4))
