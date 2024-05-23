from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def log_transform_bmp(image):
    # Convert BMP image to numpy array
    img_array = np.array(image)

    # Add a small constant to avoid taking the log of zero
    transformed_array = np.log1p(img_array)

    # Normalize to the range [0, 255]
    transformed_array = (transformed_array / np.max(transformed_array)) * 255.0

    # Convert back to uint8
    transformed_array = transformed_array.astype(np.uint8)

    # Create a new Image object from the transformed array
    transformed_image = Image.fromarray(transformed_array)

    return transformed_image

def main_bmp():
    # Replace 'input.bmp' with the path to your BMP file
    bmp_input_path = 'boats.bmp'

    # Read BMP file
    bmp_image = Image.open(bmp_input_path)

    # Apply log transform to BMP
    transformed_bmp = log_transform_bmp(bmp_image)
    transformed_bmp.save('transformed_bmp_log.bmp')

    # Display original and transformed BMP using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(bmp_image, cmap='gray')
    plt.title('Original BMP')

    plt.subplot(1, 2, 2)
    plt.imshow(transformed_bmp, cmap='gray')
    plt.title('Transformed BMP (Log)')

    plt.show()

if __name__ == "__main__":
    main_bmp()
