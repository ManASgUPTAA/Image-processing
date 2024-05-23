import matplotlib.pyplot as plt
import numpy as np

def average_grayscale(image):
    # Convert the RGB image to grayscale using average method
    return np.mean(image, axis=-1)

def histogram_equalization(image):
    # Flatten the grayscale image
    flattened_image = image.flatten()

    # Apply histogram equalization
    equalized_image = histogram_equalization_channel(flattened_image)

    # Reshape the equalized image to the original shape
    equalized_image = equalized_image.reshape(image.shape)

    return equalized_image

def histogram_equalization_channel(channel):
    # Compute histogram
    hist, bins = np.histogram(channel, bins=256, range=[0, 256])

    # Compute cumulative distribution function (CDF)
    cdf = hist.cumsum()

    # Normalize the CDF
    cdf_normalized = cdf / cdf[-1]

    # Map the pixel values using the CDF
    equalized_channel = np.interp(channel, bins[:-1], cdf_normalized * 255)

    return equalized_channel

def main():
    # Read the input image
    input_image = plt.imread('Fig4.jpg')

    # Convert the RGB image to average grayscale
    grayscale_image = average_grayscale(input_image)

    # Display the input image
    plt.subplot(2, 2, 1)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Input Grayscale Image')

    # Display the input image histogram
    plt.subplot(2, 2, 2)
    plt.hist(grayscale_image.flatten(), bins=256, range=[0, 256], color='gray', alpha=0.5)
    plt.title('Input Grayscale Image Histogram')

    # Apply histogram equalization to the average grayscale image
    equalized_image = histogram_equalization(grayscale_image)

    # Display the equalized image
    plt.subplot(2, 2, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Grayscale Image')

    # Display the equalized image histogram
    plt.subplot(2, 2, 4)
    plt.hist(equalized_image.flatten(), bins=256, range=[0, 256], color='gray', alpha=0.5)
    plt.title('Equalized Grayscale Image Histogram')

    # Show the plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
