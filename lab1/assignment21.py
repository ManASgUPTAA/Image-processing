from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def show_image_with_histogram(image, title):
    plt.figure(figsize=(10, 6))

    # Display image
    plt.subplot(2, 2, 1)
    plt.imshow(image)
    plt.title(title)

    # Display histograms for each RGB channel
    for i in range(3):
        plt.subplot(2, 2, i + 2)
        plt.hist(image[:, :, i].ravel(), bins=256, color=f'C{i}', alpha=0.7)
        plt.title(f'Channel {i} Histogram')

    plt.tight_layout()
    plt.show()

def histogram_equalization(image):
    equalized_image = image.copy()

    # Apply histogram equalization on each RGB channel
    for i in range(3):
        hist, bins = np.histogram(image[:, :, i].ravel(), bins=256, range=[0,256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()
        equalized_image[:, :, i] = np.interp(image[:, :, i], bins[:-1], cdf_normalized)

    return equalized_image

def main():
    # Read the input image
    input_image_path = 'Fig1.jpg'  
    input_image = Image.open(input_image_path)

    # Convert PIL Image to numpy array
    input_image = np.array(input_image)

    # Convert RGB to BGR
    input_image = input_image[...,::-1]

    # Display input image and histogram
    show_image_with_histogram(input_image, 'Input Image and Histograms')

    # Apply histogram equalization
    equalized_image = histogram_equalization(input_image)

    # Display output image and histogram
    show_image_with_histogram(equalized_image, 'Equalized Image and Histograms')

if __name__ == "__main__":
    main()
