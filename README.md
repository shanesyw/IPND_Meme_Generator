# Meme Generator

## Overview of Project

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

To better reflect project instruction, I have updated the application logic from starter code. We would make both author and body as necessary instead of either raising exception for the other or just missing that value. In the console app, if there's any missing element (either for author or quote body), we will randomly generate author and quote based on our databse. For the web app, if there's any missing element, we will handle it by making a meme to tell the user what is the error. We will attemtp the word wrap the quote set input by the user; however, when it gets unnecessarily too long (>120 characters), it defeats the purpose of meme, we will make a meme to tell the user.

The PDF to text conversion is using the open source xpdfReader executable. It is included in the project for convenience.
https://www.xpdfreader.com/pdftotext-man.html

## Instruction to Setup
This project has been developed and tested using Python 3.8.6-64bit in Windows 10 environment using Visual Studio Code

To get started, you need to set up things:

### 1. Set up virtual environment (optional)

```
virtualenv venv
.\venv\Scripts\activate
```

### 2. Install required modules
```
pip install -r pip_requirements.txt
```

## Meme Generator(s) Overview

There are two programs in this project:

### 1) Meme Generator Console Application (meme&#46;py)
To run the console application, use the following syntax:
Note: python is mapped to python3.8 on developer machine.

```
python .\meme.py --path '<path to image>' --body '<quote body>' --author '<author of quote>'
```
Example:
```
python .\meme.py --path './_data/photos/starwars/starwars5.jpg' --body 'I love Star Wars' --author 'Woof Woof'
```

### 2) Meme Generator Web Application (app&#46;py)
To run this web application, use the following command:
```
python .\app.py
```

You should see console output like the following
```
(venv) PS C:\shane\IntermediatePython\MemeGenerator\git2\meme-generator-shane> python .\app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You then can open a web page like the following:
```
http://127.0.0.1:5000/
```

## Overview of Sub-modules
### QuoteEngine module
Module used:
- pandas (external)
- docx (external)
- pdftotext executable (external: XpdfReader utility)

Using the module
```
list_of_quotes = []
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))

for elem in list_of_quotes:
    print(elem)
```

Output:
```
"Treat yo self" - Fluffles
"Life is like a box of treats" - Forrest Pup
"It's the size of the fight in the dog" - Bark Twain
"Bark like no one’s listening" - Rex
"RAWRGWAWGGR" - Chewy
"Life is like peanut butter: crunchy" - Peanut
"Channel your inner husky" - Tiny
"Chase the mailman" - Skittle
"When in doubt, go shoe-shopping" - Mr. Paws
"To bork or not to bork" - Bork
"He who smelt it..." - Stinky
```

### MemeMaker module
External module used:
- argparse
#### Using the module
Using the module
```
meme_maker = MemeMaker('./tmp')
result = meme_maker.make_meme('./_data/photos/starwars/starwars5.jpg', 'Where is the love!?', 'Luke Arroof' )
print(result)
```

Output:
```
./tmp/506653.jpg
```


## Appendix
- The following resource is used to setup the virtual env:

    https://www.youtube.com/watch?v=vG4AHYXsOgc&ab_channel=LiquidWeb

- Setup virtualenv in Windows 10:

    https://www.c-sharpcorner.com/article/steps-to-set-up-a-virtual-environment-for-python-development/

- If there is issue running ".\venv\Scripts\activate", the user may need to run "Set-ExecutionPolicy Unrestricted -Force" in PowerShell admin mode before running ".\venv\Scripts\activate"

    https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

