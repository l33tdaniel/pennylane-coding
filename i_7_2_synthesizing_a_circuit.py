# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def convert_to_rz_rx():
    qp.RZ(-np.pi / 2, wires=0)
    qp.RX(np.pi / 2, wires=0)
    qp.RZ(-3 * np.pi / 4, wires=0)

    return qp.state()


if __name__ == "__main__":
    print(convert_to_rz_rx())
