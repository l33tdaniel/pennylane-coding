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


@qp.qnode(device=dev)
def true_cz(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.CZ(wires=[0, 1])

    return qp.state()


@qp.qnode(dev)
def imposter_cz(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.Hadamard(wires=1)
    qp.CNOT(wires=[0, 1])
    qp.Hadamard(wires=1)

    return qp.state()


if __name__ == "__main__":
    print(f"True CZ output state {true_cz(phi, theta, omega)}")
    print(f"Imposter CZ output state {imposter_cz(phi, theta, omega)}")
