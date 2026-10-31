# /// script
# requires-python = ">=3.11"
# dependencies = ["pennylane"]
# ///

from pennylane import numpy as np

from f_1_1_converting_to_value_representation import coefficients_to_values
from f_1_2_coverting_to_coefficient_representation import values_to_coefficients
from f_1_3_the_nearest_power_of_2 import nearest_power_of_2


def fft_multiplication(poly_a, poly_b):
    num_values = len(poly_a) + len(poly_b) - 1

    num_values_power_of_2 = nearest_power_of_2(num_values)

    poly_a = np.pad(poly_a, (0, num_values_power_of_2 - len(poly_a)))
    poly_b = np.pad(poly_b, (0, num_values_power_of_2 - len(poly_b)))

    values_a = coefficients_to_values(poly_a)
    values_b = coefficients_to_values(poly_b)

    values_product = values_a * values_b

    return values_to_coefficients(values_product)


if __name__ == "__main__":
    print(fft_multiplication([1, 2, 3], [4, 5]))
