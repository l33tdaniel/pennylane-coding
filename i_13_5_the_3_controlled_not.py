# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=5)


@qp.qnode(dev)
def four_qubit_mcx_only_tofs():
    qp.PauliX(wires=0)
    qp.PauliX(wires=1)
    qp.PauliX(wires=2)

    qp.Toffoli(wires=[0, 1, 3])
    qp.Toffoli(wires=[2, 3, 4])
    qp.Toffoli(wires=[0, 1, 3])

    return qp.state()


if __name__ == "__main__":
    print(four_qubit_mcx_only_tofs())
