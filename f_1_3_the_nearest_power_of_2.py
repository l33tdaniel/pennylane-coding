# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np


def nearest_power_of_2(x):
    return 2 ** int(np.ceil(np.log2(x)))


if __name__ == "__main__":
    for x in [1, 5, 15, 16, 17]:
        print(x, nearest_power_of_2(x))
