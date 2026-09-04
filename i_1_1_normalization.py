# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Codercise I.1.1 — Normalization of quantum states.

Given an unnormalized state |psi> = alpha|0> + beta|1>, produce the equivalent
normalized state |psi'> = alpha'|0> + beta'|1> with |alpha'|^2 + |beta'|^2 = 1.
"""

import numpy as np

# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])


def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.

    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.

    Returns:
        np.array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """
    # CREATE A VECTOR [a', b'] BASED ON alpha AND beta SUCH THAT |a'|^2 + |b'|^2 = 1
    state = alpha * ket_0 + beta * ket_1
    norm = np.sqrt(np.abs(alpha) ** 2 + np.abs(beta) ** 2)

    # RETURN A VECTOR
    return state / norm


if __name__ == "__main__":
    alpha, beta = 2.0 + 1.0j, -0.3 + 0.4j
    psi = normalize_state(alpha, beta)
    print(f"normalize_state({alpha}, {beta}) = {psi}")
    print(f"|alpha'|^2 + |beta'|^2 = {np.sum(np.abs(psi) ** 2):.10f}")
