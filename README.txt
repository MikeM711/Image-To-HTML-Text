Project & Presentation Grade: 100/100

Michael McCabe - Final Project for CS 521 - Summer 2

----------------------------------------------------------------------------
Installation

Please install the following modules (I personally use pip):

1) Pillow: pip install Pillow
2) pytesseract: pip install pytesseract

Tesserect documentation: https://pypi.org/project/pytesseract/
Pillow documentation: https://pypi.org/project/Pillow/

----------------------------------------------------------------------------
ImageOCR

How to use:
1) Inside the "input_images" directory, add the image you would like to read text from.
2) When you instantiate an ImageOCR class object, provide the name of the image file and the
file extention inside the constructor as a String.
- ex: ImageOCR("my_image.jpg")
3) Read the image using the read_image() method. This method will store the resulting
text inside its own output_text instance attribute.
4) Create an HTML file of the resulting text using the create_html_from_text() method.
This file will be stored inside your "output_html" directory.
5) If necessary, modify your image into a new image using the create_black_and_white()
method (The OCR is most efficient when text is black and the background is white). 
This method will create a new image in your "manipulated_images" directory, and will update
the instance's private path to the address of the new "manipulated" image. 
This new path will be the path referenced by the read_image() method the next time it is invoked.

Public Functions and default parameters:

1) read_image()
2) create_html_from_text(img_width=50, split_newline=False, word_analysis=False)
- img_width: Width of image displayed in HTML in percent
- split_newline: Will create <br/> where the output_text has a newline character
- word_analysis: Will create a word-frequency table alongside your image and output_text
3) create_black_and_white(inverted=False)
- inverted=False: Will make dark colors 100% black and white colors 100% white
- inverted=True: Will make light colors 100% black and dark colors 100% white

Public Variables:

output_text
- Created when invoked by read_image()
- It is the text read by the OCR
output_html
- Created when invoked by create_html_from_text()
- It is the HTML inside the HTML file that was created
image_name
- The name of the image provided by the user

Magic Method:
- Add 2 ImageOCR instances together to receive a concatenated output_text string
