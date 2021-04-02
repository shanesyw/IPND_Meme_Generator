"""
app.py implementation.

A argparse based console application that accepts user input
to make memes.
"""

import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeMaker


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/starwars/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None or author is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        quote = QuoteModel(body, author)

    meme = MemeMaker('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    """The main function triggered by command prompt."""
    parser = argparse.ArgumentParser(description="This is a meme generator.")
    parser.add_argument('--path', type=str,
                        default=None, help="What is the image path?")
    parser.add_argument('--body', type=str,
                        default=None, help="What is the quote content?")
    parser.add_argument('--author', type=str,
                        default=None, help="Who is the author?")
    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
