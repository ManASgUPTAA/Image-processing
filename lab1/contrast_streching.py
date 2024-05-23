from PIL import Image
import numpy as np

def contrast_stretching(image):
    # Convert to numpy array for easier manipulation
    img_array = np.array(image)

    # Minimum and maximum pixel values
    min_val = np.min(img_array)
    max_val = np.max(img_array)

    # Apply contrast stretching formula
    stretched_array = ((img_array - min_val) / (max_val - min_val)) * 255.0

    # Convert back to uint8
    stretched_array = stretched_array.astype(np.uint8)

    # Create a new Image object from the enhanced array
    enhanced_image = Image.fromarray(stretched_array)

    return enhanced_image

def main():
    # Replace 'input.bmp' and 'input.pgm' with the paths to your BMP and PGM files
    bmp_input_path = 'boats.bmp'
    pgm_input_path = 'lungs.pgm'

    # Read BMP file
    bmp_image = Image.open(bmp_input_path)

    # Apply contrast stretching to BMP
    enhanced_bmp = contrast_stretching(bmp_image)
    enhanced_bmp.save('enhanced_bmp.bmp')

    # Read PGM file
    pgm_image = Image.open(pgm_input_path)

    # Apply contrast stretching to PGM
    enhanced_pgm = contrast_stretching(pgm_image)
    enhanced_pgm.save('enhanced_pgm.pgm')

if __name__ == "__main__":
    main()
