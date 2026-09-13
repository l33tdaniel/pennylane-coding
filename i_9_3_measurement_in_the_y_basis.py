# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

from i_9_2_y_basis_rotation import prepare_psi, y_basis_rotation

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def measure_in_y_basis():
    prepare_psi()

    qp.adjoint(y_basis_rotation)()

    return qp.probs(wires=0)


if __name__ == "__main__":
    print(measure_in_y_basis())
