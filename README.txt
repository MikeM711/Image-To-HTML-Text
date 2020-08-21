Please install the following modules (I personally use pip):

1) Pillow: pip install Pillow
2) pytesseract: pip install pytesseract

Tesserect documentation: https://pypi.org/project/pytesseract/
Pillow documentation: https://pypi.org/project/Pillow/

----------------------------------------------------------------------------

ImageOCR

How to use:
1) Inside the "input_images" directory, add the image you would like to read text from.
2) When you instantiate an ImageOCR class object, provide the name of the file and the
file extention inside the constructor as a String (ex: "my_image.jpg").
3) Read the image using the read_image method. This method will store the resulting
text inside its own output_text attribute.
4) Create an HTML file of the resulting text using the create_html_from_text method.
This file will be stored inside your "output_html" directory.
5) If necessary, modify your image into a new image using the create_black_and_white
method. This method will create a new image in your "manipulated_images" directory and update
the instance's private path to the address of the new image. This new path will be the path
referenced by the read_image method the next time it is invoked.

Public Functions and default parameters:

read_image()
create_html_from_text(img_width=50, split_newline=False, word_analysis=False)
create_black_and_white(inverted=False)

Public Variables:

output_text
output_html
image_name