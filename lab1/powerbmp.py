from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def power_law_transform_bmp(image, gamma):
    # Convert BMP image to numpy array
    img_array = np.array(image)

    # Normalize pixel values to the range [0, 1]
    normalized_array = img_array / 255.0

    # Apply power-law transform
    transformed_array = np.power(normalized_array, gamma)

    # Scale back to the range [0, 255]
    transformed_array = (transformed_array * 255).astype(np.uint8)

    # Create a new Image object from the transformed array
    transformed_image = Image.fromarray(transformed_array)

    return transformed_image

def main_bmp():
    # Replace 'input.bmp' with the path to your BMP file
    bmp_input_path = 'MRIspineFracture.bmp'

    # Read BMP file
    bmp_image = Image.open('MRIspineFracture.bmp')

    # Set the gamma value (adjust as needed)
    gamma = 1.5

    # Apply power-law transform to BMP
    transformed_bmp = power_law_transform_bmp(bmp_image, gamma)
    transformed_bmp.save(f'transformed_bmp_power_law_gamma_{gamma}.bmp')

    # Display original and transformed BMP using Matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(bmp_image, cmap='gray')
    plt.title('Original BMP')

    plt.subplot(1, 2, 2)
    plt.imshow(transformed_bmp, cmap='gray')
    plt.title(f'Transformed BMP (Gamma={gamma})')

    plt.show()

if __name__ == "__main__":
    main_bmp()
