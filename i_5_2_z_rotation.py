# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def fake_z():
    qp.Hadamard(wires=0)

    qp.RZ(np.pi, wires=0)

    return qp.state()


if __name__ == "__main__":
    print(fake_z())
