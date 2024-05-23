import cv2
import numpy as np

def gaussian_kernel(size, sigma):
    """
    Generates a Gaussian kernel.

    Parameters:
        size (int): Size of the kernel (should be odd).
        sigma (float): Standard deviation of the Gaussian distribution.

    Returns:
        np.ndarray: Gaussian kernel.
    """
    # Ensure that the size is odd for symmetry
    if size % 2 == 0:
        size += 1

    # Create a grid of points centered at the kernel
    x, y = np.mgrid[-(size // 2):(size // 2) + 1, -(size // 2):(size // 2) + 1]

    # Calculate Gaussian values using the 2D Gaussian formula
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    
    # Normalize the kernel so that the sum of all elements equals 1
    kernel /= np.sum(kernel)
    
    return kernel

def visualize_kernel(kernel):
    """
    Visualizes the kernel as an image.

    Parameters:
        kernel (np.ndarray): Input kernel.

    Returns:
        np.ndarray: Visualization of the kernel as an image.
    """
    # Normalize kernel values to range [0, 255] for visualization
    normalized_kernel = cv2.normalize(kernel, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return normalized_kernel

def main():
    # Define the size and sigma for the Gaussian filter
    size = 1001  # Adjust the size as needed
    sigma = 250.0  # Adjust the sigma value as needed

    # Generate the Gaussian kernel
    gaussian_mask = gaussian_kernel(size, sigma)

    # Visualize the Gaussian filter mask as an image
    mask_image = visualize_kernel(gaussian_mask)

    # Display the Gaussian filter mask image
    cv2.imshow('Gaussian Filter Mask', mask_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
