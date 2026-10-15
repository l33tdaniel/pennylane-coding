# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=4)


@qp.qnode(dev)
def four_qubit_mcx():
    qp.Hadamard(wires=0)
    qp.Hadamard(wires=1)
    qp.Hadamard(wires=2)
    qp.MultiControlledX(wires=[0, 1, 2, 3], control_values=[0, 0, 1])

    return qp.state()


if __name__ == "__main__":
    print(four_qubit_mcx())
