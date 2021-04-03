"""MemeMaker.py implementation."""

from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import textwrap
import random
import os

from QuoteEngine import QuoteModel


class MemeMaker():
    """
    A class that creates meme.

    It takes in a picture and a quote set, and generate a meme
    based on the picture and the quote set. The location of the
    quote set is random.
    """

    def __init__(self, output_dir):
        """Initialize the output directory."""
        self.output_dir = output_dir

    def make_meme(self, in_path, text, author, width=500) -> str:
        """Create a meme basd on given path, quote-text, and quote-author.

        Arguments:
            in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
        Returns:
            str -- the file path to the output image.
        """
        try:
            img = Image.open(in_path)
        except UnidentifiedImageError as e:
            print(e)
            return None

        new_height = int(width*(img.size[1]/img.size[0]))
        img = img.resize((width, new_height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/ZillaSlabHighlight-Bold.ttf',
                                  size=20)

        # create a random location
        text_x = random.randint(0, int(width/5))
        text_y = random.randint(0, new_height-70)

        lines = textwrap.wrap(str(QuoteModel.create(text, author)), 50)

        for line in lines:
            draw.rectangle([text_x, text_y+1, width, text_y + 22],
                           fill='black')
            font_width, font_height = font.getsize(line)
            draw.text((text_x, text_y), line, font=font, fill='white')
            text_y += font_height

        tmp = f'{self.output_dir}/{random.randint(0,1000000)}.jpg'

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        img.save(tmp)
        return tmp
