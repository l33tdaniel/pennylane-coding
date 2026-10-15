# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=3)


@qp.qnode(dev)
def controlled_rotations(theta, phi, omega):
    qp.Hadamard(wires=0)
    qp.CRX(theta, wires=[0, 1])
    qp.CRY(phi, wires=[1, 2])
    qp.CRZ(omega, wires=[2, 0])

    return qp.probs(wires=[0, 1, 2])


if __name__ == "__main__":
    theta, phi, omega = 0.1, 0.2, 0.3
    print(controlled_rotations(theta, phi, omega))
