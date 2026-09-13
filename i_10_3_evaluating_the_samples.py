# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1, shots=100000)


@qp.qnode(dev)
def circuit():
    qp.RX(np.pi / 4, wires=0)
    qp.Hadamard(wires=0)
    qp.PauliZ(wires=0)

    return qp.sample(qp.PauliY(0))


def compute_expval_from_samples(samples):
    estimated_expval = 0

    n_plus = np.count_nonzero(samples == 1)
    n_minus = np.count_nonzero(samples == -1)
    estimated_expval = (n_plus - n_minus) / len(samples)

    return estimated_expval


if __name__ == "__main__":
    samples = circuit()
    print(compute_expval_from_samples(samples))
