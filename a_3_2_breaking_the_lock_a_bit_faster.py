# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np

from a_3_1_the_oracle_in_the_circuit import n_bits, pair_circuit


def secret_combo(n_bits):
    return [int(bit) for bit in np.random.randint(2, size=n_bits)]


def pair_lock_picker(trials):
    x_tilde_strs = [np.binary_repr(n, n_bits - 1) for n in range(2 ** (n_bits - 1))]
    x_tildes = [[int(s) for s in x_tilde_str] for x_tilde_str in x_tilde_strs]

    test_numbers = []

    for trial in range(trials):
        combo = secret_combo(n_bits)
        counter = 0
        for x_tilde in x_tildes:
            counter += 1

            if np.isclose(pair_circuit(x_tilde, combo)[1], 1):
                break

        test_numbers.append(counter)
    return sum(test_numbers) / trials


if __name__ == "__main__":
    trials = 500
    output = pair_lock_picker(trials)

    print(f"For {n_bits} bits, it takes", output, "pair tests on average.")
