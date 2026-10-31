# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np


def values_to_coefficients(values):
    return np.fft.ifft(values)


if __name__ == "__main__":
    A = [10.0 + 0.0j, 2.0 - 2.0j, 2.0 + 0.0j, 2.0 + 2.0j]
    print(values_to_coefficients(A))
