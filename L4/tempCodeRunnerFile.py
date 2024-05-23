import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_filter(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define Laplacian kernel
    kernel = np.array([[0, 1, 0],
                       [1, -10, 1],
                       [0, 1, 0]])

    # Apply convolution using the defined kernel
    filtered_image = cv2.filter2D(gray_image, -1, kernel)

    # Convert back to uint8
    filtered_image = np.uint8(np.absolute(filtered_image))

    return filtered_image

def main():
    # Read input image
    input_image = cv2.imread('download.jpeg')

    # Apply Laplacian filter
    filtered_image = laplacian_filter(input_image)

    # Display input and filtered images using matplotlib
    plt.figure(figsize=(10, 5))

    # Input image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Input Image')
    plt.axis('off')

    # Filtered image
    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image (Laplacian Filter)')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
