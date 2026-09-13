# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

num_wires = 3
dev = qp.device("default.qubit", wires=num_wires)


@qp.qnode(dev)
def make_basis_state(basis_id):
    bits = [int(b) for b in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=range(num_wires))

    return qp.state()


if __name__ == "__main__":
    basis_id = 3
    print(f"Output state = {make_basis_state(basis_id)}")
