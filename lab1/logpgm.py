import matplotlib.pyplot as plt
import numpy as np

def log_transform_pgm(image_array):
    # Add a small constant to avoid taking the log of zero
    transformed_array = np.log1p(image_array)

    # Normalize to the range [0, 255]
    transformed_array = (transformed_array / np.max(transformed_array)) * 255.0

    return transformed_array

def main_pgm():
    # Replace 'input.pgm' with the path to your PGM file
    pgm_input_path = 'lungs.pgm'

    # Read PGM file
    pgm_image = np.loadtxt(pgm_input_path, )

    # Apply log transform to PGM
    transformed_pgm = log_transform_pgm(pgm_image)

    # Save transformed PGM using Matplotlib
    plt.imsave('transformed_pgm_log.pgm', transformed_pgm.astype(np.uint8), cmap='gray', format='pgm')

    # Display original and transformed PGM using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(pgm_image, cmap='gray')
    plt.title('Original PGM')

    plt.subplot(1, 2, 2)
    plt.imshow(transformed_pgm, cmap='gray')
    plt.title('Transformed PGM (Log)')

    plt.show()

if __name__ == "__main__":
    main_pgm()
