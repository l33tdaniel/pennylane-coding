# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np


def coefficients_to_values(coefficients):
    return np.fft.fft(coefficients)


if __name__ == "__main__":
    A = [4, 3, 2, 1]
    print(coefficients_to_values(A))
