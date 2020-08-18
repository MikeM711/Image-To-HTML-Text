''''
What if you call create_black_and_white twice???
'''

from ImageOCR import ImageOCR

if __name__ == "__main__":

    # This will be a user input from inside "input_images" directory
    img_name_1 = 'walmart.jpg'

    # instantiate ImageOCR object
    input_image_1 = ImageOCR(img_name_1)

    input_image_1.create_black_and_white(inverted=True)
    input_image_1.create_black_and_white(inverted=True)

    # Read the image
    input_image_1.read_image()
    input_image_1.create_html_from_text(img_width=50, word_analysis=True,
                                        split_newline=True)
