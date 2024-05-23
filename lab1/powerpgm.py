import matplotlib.pyplot as plt
import numpy as np

def power_law_transform_pgm(image_array, gamma):
    # Normalize pixel values to the range [0, 1]
    normalized_array = image_array / np.max(image_array)

    # Apply power-law transform
    transformed_array = np.power(normalized_array, gamma)

    # Scale back to the range [0, 255]
    transformed_array = (transformed_array * 255).astype(np.uint8)

    return transformed_array

def main_pgm():
    # Replace 'input.pgm' with the path to your PGM file
    pgm_input_path = 'lungs.pgm'

    # Read PGM file
    pgm_image = np.loadtxt('lungs.pgm', )

    # Set the gamma value (adjust as needed)
    gamma = 0.7

    # Apply power-law transform to PGM
    transformed_pgm = power_law_transform_pgm(pgm_image, gamma)

    # Save transformed PGM using Matplotlib
    plt.imsave(f'transformed_pgm_power_law_gamma_{gamma}.pgm', transformed_pgm.astype(np.uint8), cmap='gray', format='pgm')

    # Display original and transformed PGM using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(pgm_image, cmap='gray')
    plt.title('Original PGM')

    plt.subplot(1, 2, 2)
    plt.imshow(transformed_pgm, cmap='gray')
    plt.title(f'Transformed PGM (Gamma={gamma})')

    plt.show()

if __name__ == "__main__":
    main_pgm()
