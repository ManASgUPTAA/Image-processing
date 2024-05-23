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

def main():
    # Define the size and sigma for the Gaussian filter
    size = 11  # Adjust the size as needed
    sigma = 3.0  # Adjust the sigma value as needed

    # Generate the Gaussian kernel
    gaussian_mask = gaussian_kernel(size, sigma)

    # Print the Gaussian kernel
    print("Gaussian low-pass filter kernel:")
    print(gaussian_mask)

if __name__ == "__main__":
    main()
