import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def histogram_specification(image, specification_data):
    lut = []
    for channel in cv2.split(image):
        histogram, _ = np.histogram(channel.flatten(), 256, [0, 256])
        cdf = histogram.cumsum()
        cdf = 255 * cdf / cdf[-1]
        lut.append(np.interp(channel.flatten(), range(256), cdf).reshape(channel.shape))
    result_image = cv2.merge(lut).astype(np.uint8)
    return result_image

def plot_histogram(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

def main():
    # Read input image
    input_image = cv2.imread('moon.jpg')

    # Convert input image to grayscale
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Compute average grayscale image
    avg_gray_value = np.mean(gray_image)
    avg_gray_image = np.full_like(gray_image, avg_gray_value, dtype=np.uint8)

    # Read histogram specification data
    specification_data = pd.read_excel('HistogramSpecificationData.xlsx')

    # Apply histogram specification on average grayscale image
    specified_image = histogram_specification(avg_gray_image, specification_data)

    # Plot histograms for input and processed images
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Input Image')
    plt.subplot(2, 2, 2)
    plot_histogram(input_image)
    plt.title('Input Image Histogram')

    plt.subplot(2, 2, 3)
    plt.imshow(specified_image, cmap='gray')
    plt.title('Specified Image')
    plt.subplot(2, 2, 4)
    plot_histogram(specified_image)
    plt.title('Specified Image Histogram')

    plt.show()

if __name__ == "__main__":
    main()
