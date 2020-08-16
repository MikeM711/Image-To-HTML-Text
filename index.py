from ImageOCR import ImageOCR

# EXAMPLE #1
img_name = 'some_text.png'  # This will be a user input

input_image = ImageOCR(img_name)
input_image.read_image()
print(input_image)

input_image.create_html_from_text(img_width=50, word_analysis=True,
                                  split_newline=True)

# EXAMPLE #2
img_name_2 = 'walmart.jpg'  # This will be a user input

input_image_2 = ImageOCR(img_name_2)
output_text_2 = input_image_2.read_image()
print(output_text_2)

# Create a black and white image
input_image_2.create_black_and_white()
output_text_2_bw = input_image_2.read_image()
print(output_text_2_bw)

# Create HTML
input_image_2.create_html_from_text(img_width=50)

print(f"Magic Method: {input_image + input_image_2}")

# EXAMPLE #3
img_name_3 = "marc_notes.png"

input_image_3 = ImageOCR(img_name_3)
input_image_3.read_image()
input_image_3.create_html_from_text(img_width=20, split_newline=True)

# EXAMPLE #4
img_name_4 = "invoice_example.png"

input_image_4 = ImageOCR(img_name_4)
input_image_4.create_black_and_white(inverted=True)

print(input_image_4.read_image())
input_image_4.create_html_from_text(img_width=50, split_newline=True)
