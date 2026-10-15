# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp

dev = qp.device("default.qubit", wires=2)


@qp.qnode(dev)
def apply_h_cnot():
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])

    return qp.state()


state_status = "entangled"

if __name__ == "__main__":
    print(apply_h_cnot())
