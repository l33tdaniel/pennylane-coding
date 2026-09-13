# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def circuit():
    qp.RX(np.pi / 4, wires=0)
    qp.Hadamard(wires=0)
    qp.PauliZ(wires=0)

    return qp.expval(qp.PauliY(0))


if __name__ == "__main__":
    print(circuit())
