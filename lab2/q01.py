import matplotlib.pyplot as plt
import numpy as np

def histogram_equalization(image):
    # Flatten the image for each RGB channel
    r_channel = image[:,:,0].flatten()
    g_channel = image[:,:,1].flatten()
    b_channel = image[:,:,2].flatten()

    # Apply histogram equalization to each channel
    r_eq = histogram_equalization_channel(r_channel)
    g_eq = histogram_equalization_channel(g_channel)
    b_eq = histogram_equalization_channel(b_channel)

    # Reshape the equalized channels to the original shape
    equalized_image = np.zeros_like(image)
    equalized_image[:,:,0] = r_eq.reshape(image.shape[:2])
    equalized_image[:,:,1] = g_eq.reshape(image.shape[:2])
    equalized_image[:,:,2] = b_eq.reshape(image.shape[:2])

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
    input_image = plt.imread('Fig2.jpg')

    # Display the input image
    plt.subplot(2, 2, 1)
    plt.imshow(input_image)
    plt.title('Input Image')

    # Display the input image histograms for each channel
    plt.subplot(2, 2, 2)
    plt.hist(input_image[:,:,0].flatten(), bins=256, range=[0, 256], color='red', alpha=0.5, label='Red')
    plt.hist(input_image[:,:,1].flatten(), bins=256, range=[0, 256], color='green', alpha=0.5, label='Green')
    plt.hist(input_image[:,:,2].flatten(), bins=256, range=[0, 256], color='blue', alpha=0.5, label='Blue')
    plt.title('Input Image Histograms')
    plt.legend()

    # Apply histogram equalization to the input image
    equalized_image = histogram_equalization(input_image)

    # Display the equalized image
    plt.subplot(2, 2, 3)
    plt.imshow(equalized_image)
    plt.title('Equalized Image')

    # Display the equalized image histograms for each channel
    plt.subplot(2, 2, 4)
    plt.hist(equalized_image[:,:,0].flatten(), bins=256, range=[0, 256], color='red', alpha=0.5, label='Red')
    plt.hist(equalized_image[:,:,1].flatten(), bins=256, range=[0, 256], color='green', alpha=0.5, label='Green')
    plt.hist(equalized_image[:,:,2].flatten(), bins=256, range=[0, 256], color='blue', alpha=0.5, label='Blue')
    plt.title('Equalized Image Histograms')
    plt.legend()

    # Show the plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
