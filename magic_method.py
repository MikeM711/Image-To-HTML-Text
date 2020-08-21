"""
This file tests out the additon "magic method" of ImageOCR
We will instantiate 2 tester1.png images and "add" the instances together.
"""

from ImageOCR import ImageOCR

if __name__ == "__main__":
    # EXAMPLE #1

    img_name_1 = 'tester1.png'
    input_image_1 = ImageOCR(img_name_1)
    input_image_1.read_image()

    img_name_2 = 'tester1.png'
    input_image_2 = ImageOCR(img_name_2)
    input_image_2.read_image()

    # magic method
    magic_method = input_image_1 + input_image_2

    print(f"Magic Method: {magic_method}")
