# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=2)

phi, theta, omega = 1.2, 2.3, 3.4


def prepare_states(phi, theta, omega):
    qp.RX(phi, wires=0)
    qp.RY(theta, wires=0)
    qp.RY(omega, wires=1)
    qp.RZ(theta, wires=1)


@qp.qnode(dev)
def apply_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.SWAP(wires=[0, 1])

    return qp.state()


@qp.qnode(dev)
def apply_swap_with_cnots(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.CNOT(wires=[0, 1])
    qp.CNOT(wires=[1, 0])
    qp.CNOT(wires=[0, 1])

    return qp.state()


if __name__ == "__main__":
    print(f"Regular SWAP state = {apply_swap(phi, theta, omega)}")
    print(f"CNOT SWAP state = {apply_swap_with_cnots(phi, theta, omega)}")
