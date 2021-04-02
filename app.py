"""
app.py implementation.

A flask based website that accepts user input to make memes.
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeMaker

app = Flask(__name__)

meme = MemeMaker('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/starwars/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    images = "./_data/photos/starwars/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    img = random.choice(imgs)

    # 2. select a random quote from the quotes array
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    quote = random.choice(quotes)

    # make meme
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    download_path = request.form['image_url']

    author = request.form['body']
    body = request.form['author']

    if request.form['body'] == "" or request.form['author'] == "":
        body = "Your quote has nothing!"
        author = "Darth Woofer"

    try:
        r = requests.get(download_path, allow_redirects=True)
        extName = download_path.split('.')[-1]

        if not os.path.exists('./static/'):
            os.makedirs('./static/')

        tmp = f'./static/{random.randint(0, 100000000)}.{extName}'
        open(tmp, 'wb').write(r.content)
    except (requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError) as e:
        print(e)
        path = meme.make_meme("./_data/photos/starwars/starwars3.jpg",
                              'Your URL is not valid!!', 'Darth Woofer')
        return render_template('meme.html', path=path)

    path = meme.make_meme(tmp, body, author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
