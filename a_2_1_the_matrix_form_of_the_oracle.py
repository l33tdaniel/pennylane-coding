# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np


def oracle_matrix(combo):
    index = np.ravel_multi_index(combo, [2] * len(combo))
    my_array = np.identity(2 ** len(combo))

    my_array[index, index] = -1

    return my_array


if __name__ == "__main__":
    print(np.diag(oracle_matrix([0, 1, 1, 0])))
