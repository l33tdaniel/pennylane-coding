# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

num_wires = 2
dev = qp.device("default.qubit", wires=num_wires)


@qp.qnode(dev)
def two_qubit_QFT(basis_id):
    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1])

    U = 0.5 * np.array(
        [
            [1, 1, 1, 1],
            [1, 1j, -1, -1j],
            [1, -1, 1, -1],
            [1, -1j, -1, 1j],
        ]
    )
    qp.QubitUnitary(U, wires=[0, 1])

    return qp.state()


if __name__ == "__main__":
    for basis_id in range(2**num_wires):
        print(basis_id, two_qubit_QFT(basis_id))
