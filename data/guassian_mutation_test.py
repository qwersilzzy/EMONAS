import random

def bit_flipping_mutation(genotype):
    num_bits = len(genotype)
    flipped_bits = random.sample(range(num_bits), k=3)  # Flip 3 random bits
    new_genotype = ""
    for i, bit in enumerate(genotype):
        if i in flipped_bits:
            new_genotype += str(random.choice([0, 1]))
        else:
            new_genotype += bit
    return new_genotype

# Example usage
original_genotype = "11011010"
new_genotype = bit_flipping_mutation(original_genotype)
print(new_genotype)  # Output: 11101100

import numpy as np
def gaussian_noise(x, sigma=0.1):
    return x + np.random.normal(scale=sigma, size=len(x))

def height(x):
    return np.sin(x[0]) + np.cos(x[1])

import numpy as np

def gaussian_mutation(genotype, sigma):
    """
    Mutate the genotype by adding Gaussian noise.

    Args:
        genotype (np.ndarray): The genotype to mutate, represented as an integer array.
        sigma (float): The standard deviation of the Gaussian distribution.

    Returns:
        np.ndarray: The mutated genotype, also represented as an integer array.
    """
    # Convert the genotype to a floating-point array
    float_genotype = np.array(genotype, dtype=np.float32)

    # Add Gaussian noise to the floatting-point genotype
    noisy_genotype = float_genotype + np.random.normal(scale=sigma, size=float_genotype.shape)

    # Clip any negative values to 0
    clipped_genotype = np.maximum(noisy_genotype, 0)

    # If any values are exactly 0, set them to 1
    clipped_genotype[clipped_genotype == 0] = 1

    return clipped_genotype.astype(np.int32)



genotype = np.array([1, 2, 3])
mutated_genotype = gaussian_mutation(genotype, 20)
print(mutated_genotype)