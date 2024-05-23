import cv2
import numpy as np
import matplotlib.pyplot as plt

def median_filter(image, kernel_size):
    # Define padded array
    padded_image = np.pad(image, ((kernel_size//2, kernel_size//2), (kernel_size//2, kernel_size//2)), mode='constant')

    # Create an empty result array
    result_image = np.zeros_like(image)

    # Apply median filter
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            patch = padded_image[i:i+kernel_size, j:j+kernel_size]
            result_image[i, j] = np.median(patch)

    return result_image

def main():
    # Read input image
    input_image = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)

    # Define kernel size for median filter
    kernel_size = 3  # Adjust this value as needed

    # Apply median filter
    filtered_image = median_filter(input_image, kernel_size)

    # Display input and filtered images using matplotlib
    plt.figure(figsize=(10, 5))

    # Input image
    plt.subplot(1, 2, 1)
    plt.imshow(input_image, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')

    # Filtered image
    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image (Median Filter)')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
