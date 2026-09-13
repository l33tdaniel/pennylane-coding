# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

v = np.array([0.52889389 - 0.14956775j, 0.67262317 + 0.49545818j])

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def prepare_state(state=v):
    qp.StatePrep(state, wires=0)
    return qp.state()


if __name__ == "__main__":
    print(prepare_state(v))
    print()
    print(qp.draw(prepare_state, level="device")(v))
