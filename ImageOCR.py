"""
Michael McCabe
Class: CS 521 - Summer 2
Date: 8/16
Final Project
Description of Problem:
Create a class object that allows a user to read a particular image and
create HTML based on the output of that particular image. Users have the
option to manipulate their image and the how the HTML output is formatted.
"""

from PIL import Image
import pytesseract
import sys
import string
import time


class ImageOCR():
    '''
    A Class for an ImageOCR
    '''
    # Static attributes for every object
    img_dir = './input_images/'
    output_dir = './output_html'
    manipulated_images_dir = "./manipulated_images"

    def __init__(self, image_name="placeholder.png"):
        '''
        Constructor for ImageOCR Class
        '''
        # incoming image_name MUST be a string
        if isinstance(image_name, str) is False:
            sys.exit("The image name provided is not a String. Please provide "
                     "a file name of String type.")

        # Create a full path
        self.__path = ImageOCR.img_dir + image_name  # Make path private

        # output and image_name will be public
        self.output_text = ''
        self.output_html = ''
        self.image_name = image_name

    def __repr__(self):
        '''
        A string that represents the ImageOCR instance
        '''
        if self.output_text != '':
            return (f"The image, \"{self.image_name}\", has been read as, "
                    f"\"{self.output_text}\"")
        else:
            return (f"The image, {self.image_name}, has yet to be determined "
                    "by the OCR")

    def read_image(self):
        '''
        Method opens an image using private path attribute, using the
        Pillow module. The opened image is read by Python-tesseract OCR
        tool and the resulting text string prediction is both updated in the
        instance and returned.
        '''
        try:
            image_file = Image.open(self.__path)
        except FileNotFoundError:
            sys.exit("Error: Input image file not found.\nPlease make "
                     "sure your file is found inside at the path, "
                     f"\"{self.__path}\", and that the name of your image and "
                     "extension is correct.")

        # Read the image text
        image_file_text = pytesseract.image_to_string(image_file)

        # Close time image_file, it is not needed
        image_file.close()

        # save the output text inside the instance
        self.output_text = image_file_text

        return self.output_text

    def create_html_from_text(self, img_width=50, split_newline=False,
                              word_analysis=False):
        '''
        Method generates an HTML file.

        The HTML file will show the image in question using the private path
        attribute and display text found in the output_text attribute.

        Optional parameters include 1) Image width (in percent), 2) The
        ability to spilt lines on newline, 3) Ability to display a word
        analysis table of word frequency (descending order)
        '''
        # initialize table and text
        table = ""
        text = self.output_text

        # The HTML is one layer deep, so we will concatenate a dot to escape
        # the "output_html" folder to grab the proper image in question
        path_from_html = "." + self.__path

        # Check optional params given by the user
        if word_analysis is True:
            # Create an HTML table for word analysis
            # Create the beginning of the table
            table = ('\n<style>'
                     '\ntable, th, td {'
                     '\nborder: 1px solid black;'
                     '\nborder-collapse: collapse;'
                     '\n}'
                     '\n</style>'
                     '\n<table style="width:40%">'
                     '\n<tr>'
                     '\n<th>Word</th>'
                     '\n<th>Frequency</th>'
                     '\n</tr>')

            # Create the table body using private __word_analysis method
            table = self.__word_analysis(table)

            # Complete the table
            table += "\n</table>"

        if split_newline is True:
            # Adds <br/> break tags between newline

            text_list = text.split("\n")
            # set text to an empty string and build off of it
            text = ""

            # using a WHILE loop to create a "split newline" output format
            idx = 0
            while idx < len(text_list):
                text_line = text_list[idx]
                text += f"{text_line}\n<br/>\n"
                idx += 1  # increment the index

        # concatenate the ending of the HTML
        html = ('<div style="padding-left:2%">'
                f'\n<h1> CS521 - ImageOCR: {self.image_name}</h1>'
                f'\n<img width="{img_width}%"  src="{path_from_html}"/>'
                '\n<div style="padding-right:45%">'
                f'\n<p >{text}</p>'
                f'\n{table}'
                '\n</div>'
                '\n</div>\n')

        # Create HTML output file path
        # time.time() used to create a timestamp for totally unique files
        output_file_name = f"{ImageOCR.output_dir}/output-{time.time()}.html"

        # Open the HTML file and write in it
        try:
            output_file = open(output_file_name, "w")
        except FileNotFoundError:
            sys.exit("ERROR: Please create an \"output_html\" folder in the "
                     "root directory")

        for line in html:
            output_file.write(line)

        # close HTML file
        output_file.close()

        # Set HTML attribute if one wishes to access it later
        self.output_html = html

        return self

    def __word_analysis(self, table):
        '''
        Private method that creates an HTML table body of word frequencies. It
        is a helper method for the create_html_from_text method.
        '''
        # Create an empty dictionary
        words_dict = {}

        # convert all output characters to lowercase
        modified_text = self.output_text.lower()

        # Split the text list on each line (a word)
        line_list = modified_text.split('\n')

        # loop through all words and add them to the dictionary
        for line in line_list:
            # get all words off of each line (split on space)
            words_list = line.split(" ")
            for word in words_list:
                # strip all punctuation
                word = word.strip(string.punctuation)
                # strip whitespace
                word = word.strip(string.whitespace)
                if word == "":
                    # Don't allow blanks in the dictionary
                    continue
                if word not in words_dict:
                    words_dict[word] = 1
                else:
                    words_dict[word] += 1

        # Sort dict pairs by value (second element in the tuple item)
        # in descending order
        sort_words_list = sorted([(k, v) for k, v in words_dict.items()],
                                 key=lambda x: x[1], reverse=True)

        # Create words/frequency table

        # loop through the dictionary, insert word and frequency
        # into tables
        for k, v in sort_words_list:
            table += ('\n<tr>'
                      f'\n\t<td>{k}</td>'
                      f'\n\t<td>{v}</td>'
                      '\n</tr>')

        # If the image does not have any words let the user know within
        # the table
        if len(sort_words_list) == 0:
            table += ('\n<tr>'
                      '\n\t<td colspan="2">No words found</td>'
                      '\n</tr>')

        return table

    def create_black_and_white(self, inverted=False):
        '''
        Method manipulates the image, located in the private path variable,
        into a new black-and-white image. New image is saved in the
        "manipulated_images" directory and the private path is updated to that
        new image path.

        User has the option to make dark colors and light colors completely
        black and white, or white and black, respectively.
        '''
        # Open the image_file from our path
        try:
            image_file = Image.open(self.__path)
        except FileNotFoundError:
            sys.exit("Error: Input image file not found.\nPlease make "
                     "sure your file is found inside at the path, "
                     f"\"{self.__path}\", and that the name of your image and "
                     "extension is correct.")

        # Convert to grayscale using "L"
        gray_img = image_file.convert("L")

        # Create black and white image
        # 0 = BLACK, 255 = WHITE
        if inverted is False:
            # In grayscale: Make dark pixels 100% dark, make white pixels
            # 100% white
            black_white = gray_img.point(lambda x: 0 if x < 128 else 255)
        elif inverted is True:
            # In grayscale: Make darks 100% white, make whites 100% dark
            black_white = gray_img.point(lambda x: 0 if x > 128 else 255)

        # Close the image_file, it is not needed anymore
        image_file.close()

        # The path of where this manipulated_image should go
        # time.time() used to create a timestamp for totally unique files
        black_white_path = (f"{ImageOCR.manipulated_images_dir}"
                            f"/img-{time.time()}.png")

        # Create the black and white image at this path
        try:
            black_white.save(black_white_path)
        except FileNotFoundError:
            sys.exit("ERROR: Please create a \"manipulated_images\" folder "
                     "in the root directory")

        # close the black and white file
        black_white.close()

        # set a new path in our instance
        self.__path = black_white_path

        # Return to the user the new image path we made
        return black_white_path

    def __add__(self, other):
        '''
        A "Magic Method" that will add the output_text of two ImageOCR
        instances for the "+" operation. The resulting output is a String type.
        '''
        return self.output_text + other.output_text


if __name__ == "__main__":
    # Unit Testing

    # One Image OCR instance - a very simple image.

    # First image path
    img_name_1 = 'tester1.png'

    input_ocr_image_1 = ImageOCR(img_name_1)  # Create an ImageOCR instance
    im_txt_1 = input_ocr_image_1.read_image()  # Have the OCR read the image

    # Expted ouptut
    expect_im_txt_1 = ("When we covered strings, we emphasized that they are "
                       "immutable. In particular, we noted\nthat you could "
                       "not have a string index operator on the left-hand "
                       "side of an assignment\nstatement. In other words, you "
                       "could not change a character of the string at some "
                       "index\nwithin an existing string to a different "
                       "character. Once created, the string cannot be "
                       "changed.")

    # Test to see if the tester1 image text output is the expected test
    assert im_txt_1 == expect_im_txt_1, (
        "The simple image 'tester1.png', was incorrectly read.")

    # A second ImageOCR instance - another very simple image

    # Second image path
    img_name_2 = 'tester2.png'

    input_ocr_image_2 = ImageOCR(img_name_2)  # Create an ImageOCR instance
    im_txt_2 = input_ocr_image_2.read_image()  # Have the OCR read the image

    # Expted ouptut
    expect_im_txt_2 = ("We’ve seen what’s the same about lists and strings, "
                       "so let’s look a bit more at what’s different.")

    # Test to see if the tester2 image text output is the expected test
    assert im_txt_2 == expect_im_txt_2, (
        "The simple image 'tester2.png', was incorrectly read.")

    # Perform a "Magic Method" assertion
    # adding 2 instances together should equal a string concatenation of their
    # output
    assert input_ocr_image_1 + input_ocr_image_2 == (
        expect_im_txt_1 + expect_im_txt_2), (
            "This simple image was incorrectly read.")

    print("Unit Tests passed!")
