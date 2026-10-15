# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def prepare_psi_plus():
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])

    return qp.state()


@qp.qnode(dev)
def prepare_psi_minus():
    qp.PauliX(wires=0)
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])

    return qp.state()


@qp.qnode(dev)
def prepare_phi_plus():
    qp.Hadamard(wires=0)
    qp.PauliX(wires=1)
    qp.CNOT(wires=[0, 1])

    return qp.state()


@qp.qnode(dev)
def prepare_phi_minus():
    qp.PauliX(wires=0)
    qp.Hadamard(wires=0)
    qp.PauliX(wires=1)
    qp.CNOT(wires=[0, 1])

    return qp.state()


if __name__ == "__main__":
    psi_plus = prepare_psi_plus()
    psi_minus = prepare_psi_minus()
    phi_plus = prepare_phi_plus()
    phi_minus = prepare_phi_minus()

    print(f"|ψ_+> = {psi_plus}")
    print(f"|ψ_-> = {psi_minus}")
    print(f"|ϕ_+> = {phi_plus}")
    print(f"|ϕ_-> = {phi_minus}")
