# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

import pennylane as qp
from pennylane import numpy as np


def U_power_2k(unitary, k):
    return np.linalg.matrix_power(unitary, 2**k)


if __name__ == "__main__":
    U = qp.T.compute_matrix()
    print(U)

    print(U_power_2k(U, 2))
