# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def prepare_state():
    qp.Hadamard(wires=0)
    qp.RZ(5 * np.pi / 4, wires=0)

    return qp.state()


if __name__ == "__main__":
    print(prepare_state())
