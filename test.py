from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeMaker


list_of_quotes = []
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
list_of_quotes.extend(Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))

for elem in list_of_quotes:
    print(elem)


meme_maker = MemeMaker('./tmp')
result = meme_maker.make_meme('./_data/photos/starwars/starwars5.jpg', 'Yoyo!', 'Luke' )
print(result)