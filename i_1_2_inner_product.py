# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Codercise I.1.2 — Inner product and orthonormal bases.

Compute <state_1 | state_2>, then verify that |0> and |1> form an orthonormal
basis: each is normalized (<0|0> = <1|1> = 1) and they are mutually orthogonal
(<0|1> = <1|0> = 0).
"""

import numpy as np


def inner_product(state_1, state_2):
    """Compute the inner product between two states.

    Args:
        state_1 (np.array[complex]): A normalized quantum state vector
        state_2 (np.array[complex]): A second normalized quantum state vector

    Returns:
        complex: The value of the inner product <state_1 | state_2>.
    """
    # COMPUTE AND RETURN THE INNER PRODUCT
    # The bra <state_1| is the conjugate transpose of the ket |state_1>.
    return np.dot(np.conj(state_1), state_2)


if __name__ == "__main__":
    # Test your results with this code
    ket_0 = np.array([1, 0])
    ket_1 = np.array([0, 1])

    print(f"<0|0> = {inner_product(ket_0, ket_0)}")
    print(f"<0|1> = {inner_product(ket_0, ket_1)}")
    print(f"<1|0> = {inner_product(ket_1, ket_0)}")
    print(f"<1|1> = {inner_product(ket_1, ket_1)}")
