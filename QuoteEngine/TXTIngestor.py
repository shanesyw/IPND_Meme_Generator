"""TXTIngestor.py implementation."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """A derived class implementing PDF variant."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TXT file from given path."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        # Open with utf-8-sig encoding to remove /ueff
        # https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string
        try:
            file_ref = open(path, "r", encoding="utf-8-sig")
        except FileNotFoundError as e:
            print(e)
            return []

        quotes = []
        for line in file_ref.readlines():
            if line != "":
                parse = line.split(' - ')
                if len(parse) > 1:
                    quotes.append(QuoteModel.create(str(parse[0]),
                                                    str(parse[1]).strip('\n')))

        file_ref.close()
        return quotes
