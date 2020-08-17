from ImageOCR import ImageOCR


if __name__ == "__main__":
    # EXAMPLE #1
    img_name_1 = 'walmart.jpg'  # This will be a user input

    input_image_1 = ImageOCR(img_name_1)
    output_text_1 = input_image_1.read_image()
    print(output_text_1)  # Nothing?

    # Create a black and white image
    input_image_1.create_black_and_white()
    output_text_1_bw = input_image_1.read_image()
    print(output_text_1_bw)

    # Create HTML
    input_image_1.create_html_from_text(img_width=50)

    # EXAMPLE #2

    img_name_2 = 'walmart.jpg'  # This will be a user input

    input_image_2 = ImageOCR(img_name_2)
    output_text_2 = input_image_2.read_image()
    print(output_text_2)  # Nothing?

    # Create a black and white image
    input_image_2.create_black_and_white(inverted=True)
    output_text_2_bw = input_image_2.read_image()
    print(output_text_2_bw)

    # Create HTML
    input_image_2.create_html_from_text(img_width=50)
