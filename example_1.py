from ImageOCR import ImageOCR

if __name__ == "__main__":
    # EXAMPLE #1

    # This will be a user input from inside "input_images" directory
    img_name_1 = 'tester1.png'

    # instantiate ImageOCR object
    input_image_1 = ImageOCR(img_name_1)

    # Read the image
    input_image_1.read_image()

    # Print the __repr__() of the instance
    print(input_image_1)

    # Create the HTML of width 50%, and a word_analysis and split_newline
    input_image_1.create_html_from_text(img_width=50, word_analysis=True,
                                        split_newline=True)
