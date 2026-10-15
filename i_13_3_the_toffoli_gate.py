# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=3)

phi, theta, omega = 1.2, 2.3, 3.4


def prepare_states(phi, theta, omega):
    qp.PauliX(wires=0)
    qp.RX(phi, wires=1)
    qp.RY(theta, wires=1)
    qp.RY(omega, wires=2)
    qp.RZ(theta, wires=2)


@qp.qnode(dev)
def no_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)
    return qp.state()


@qp.qnode(dev)
def controlled_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.Toffoli(wires=[0, 1, 2])
    qp.Toffoli(wires=[0, 2, 1])
    qp.Toffoli(wires=[0, 1, 2])

    return qp.state()


if __name__ == "__main__":
    print(no_swap(phi, theta, omega))
    print(controlled_swap(phi, theta, omega))
