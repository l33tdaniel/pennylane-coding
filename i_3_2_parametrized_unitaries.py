# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def apply_u_as_rot(phi, theta, omega):
    qp.Rot(phi, theta, omega, wires=0)

    return qp.state()


if __name__ == "__main__":
    print(apply_u_as_rot(0.1, 0.2, 0.3))
