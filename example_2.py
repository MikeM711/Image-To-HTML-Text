"""
This file only reads walmart.jpg from within the "input_images" directory.

We show that the current image provided is not good enough - so we manipulated
the image into pure black and white to achieve the desired outcome.

We will then create an HTML file of the results.
"""

from ImageOCR import ImageOCR

if __name__ == "__main__":
    # EXAMPLE #2
    img_name_2 = 'walmart.jpg'  # This will be a user input

    input_image_2 = ImageOCR(img_name_2)
    output_text_2 = input_image_2.read_image()
    print(input_image_2)  # Output is "yet to be determined"?

    # Let's try manipulating the image then, in hopes that we can now read
    # the image

    # Create a black and white image
    input_image_2.create_black_and_white(inverted=True)
    output_text_2_bw = input_image_2.read_image()
    print(input_image_2)

    # It works! We have output text after creating the manipulated image

    # Create HTML
    input_image_2.create_html_from_text(img_width=50)
