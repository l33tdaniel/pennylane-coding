# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def apply_rx_pi(state):
    if state == 1:
        qp.PauliX(wires=0)

    qp.RX(np.pi, wires=0)

    return qp.state()


if __name__ == "__main__":
    print(apply_rx_pi(0))
    print(apply_rx_pi(1))
