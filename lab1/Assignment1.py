import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def contrast_stretching(image_array):
    # Minimum and maximum pixel values
    min_val = np.min(image_array)
    max_val = np.max(image_array)

    # Apply contrast stretching formula
    stretched_array = ((image_array - min_val) / (max_val - min_val)) * 255.0

    # Clip values to ensure they are within the valid range
    stretched_array = np.clip(stretched_array, 0, 255)

    return stretched_array

def main():
    # Replace 'input.bmp' and 'input.pgm' with the paths to your BMP and PGM files
    bmp_input_path = 'boats.bmp'
    pgm_input_path = 'lungs.pgm'

    # Read BMP file
    bmp_image = mpimg.imread(bmp_input_path)

    # Apply contrast stretching to BMP
    enhanced_bmp = contrast_stretching(bmp_image)

    # Save enhanced BMP using Matplotlib
    plt.imsave('enhanced_bmp_matplotlib.bmp', enhanced_bmp.astype(np.uint8), cmap='gray')

    # Display original and enhanced BMP using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(bmp_image, cmap='gray')
    plt.title('Original BMP')

    plt.subplot(1, 2, 2)
    plt.imshow(enhanced_bmp, cmap='gray')
    plt.title('Enhanced BMP')

    plt.show()

    # Read PGM file
    pgm_image = np.loadtxt(pgm_input_path, skiprows=3)

    # Apply contrast stretching to PGM
    enhanced_pgm = contrast_stretching(pgm_image)

    # Save enhanced PGM using Matplotlib
    plt.imsave('enhanced_pgm_matplotlib.pgm', enhanced_pgm.astype(np.uint8), cmap='gray', format='pgm')

    # Display original and enhanced PGM using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(pgm_image, cmap='gray')
    plt.title('Original PGM')

    plt.subplot(1, 2, 2)
    plt.imshow(enhanced_pgm, cmap='gray')
    plt.title('Enhanced PGM')

    plt.show()

if __name__ == "__main__":
    main()
