from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def read_bmp(file_path):
    image = Image.open(file_path)
    return image

def intensity_averaging(image):
    return image.convert('L')

def intensity_inversion(image):
    return Image.fromarray(255 - np.array(image))

def sub_sampling(image, factor):
    width, height = image.size
    new_width, new_height = width // factor, height // factor
    return image.resize((new_width, new_height))

def main():
    # Replace 'input.bmp' with the path to your BMP file
    file_path = 'MRIspineFracture.bmp'

    # Read the BMP file
    original_image = read_bmp(file_path)

    # Perform intensity averaging
    averaged_image = intensity_averaging(original_image)

    # Perform intensity inversion
    inverted_image = intensity_inversion(original_image)

    # Perform sub-sampling with factor 2
    subsampled_image = sub_sampling(original_image, factor=2)

    # Display the images
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 3, 1)
    plt.imshow(original_image)
    plt.title('Original Image')

    plt.subplot(2, 3, 2)
    plt.imshow(averaged_image, cmap='gray')
    plt.title('Intensity Averaging')

    plt.subplot(2, 3, 3)
    plt.imshow(inverted_image, cmap='gray')
    plt.title('Intensity Inversion')

    plt.subplot(2, 3, 4)
    plt.imshow(original_image)
    plt.title('Original Image')

    plt.subplot(2, 3, 5)
    plt.imshow(subsampled_image)
    plt.title('Sub-sampling (Factor 2)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()