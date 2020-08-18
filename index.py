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
    print(f"\n{input_image_1}")

    # Create the HTML of width 50%, and a word_analysis and split_newline
    input_image_1.create_html_from_text(img_width=50, word_analysis=True,
                                        split_newline=True)

    # EXAMPLE #2
    img_name_2 = 'walmart.jpg'  # This will be a user input

    input_image_2 = ImageOCR(img_name_2)
    output_text_2 = input_image_2.read_image()
    print(f"\n{input_image_2}")  # Output has yet to be determined?

    # Try manipulating the image then.

    # Create a black and white image
    input_image_2.create_black_and_white(inverted=True)
    output_text_2_bw = input_image_2.read_image()
    print(f"\n{input_image_2}")

    # Create HTML using the default 50% width
    input_image_2.create_html_from_text()

    print(f"\nMagic Method: {input_image_1 + input_image_2}")

    # EXAMPLE #3
    img_name_3 = "lecture_notes.png"

    input_image_3 = ImageOCR(img_name_3)
    input_image_3.read_image()
    input_image_3.create_html_from_text(img_width=20, split_newline=True)

    # EXAMPLE #4.1
    img_name_4 = "invoice_example.png"

    input_image_4 = ImageOCR(img_name_4)
    input_image_4.create_black_and_white()

    input_image_4.read_image()
    input_image_4.create_html_from_text(img_width=45, split_newline=True)

    # EXAMPLE #4.2
    # In this particular example, we want to accurately read the
    # "Description", "Quantity", "Unit Price" and "Cost" headers, to make up
    # for the last example not being able to read that particular text.

    input_image_4.create_black_and_white(inverted=True)
    input_image_4.read_image()
    input_image_4.create_html_from_text(img_width=45, split_newline=True)
