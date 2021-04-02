"""PDFIngestor.py implementation."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """A derived class implementing PDF variant."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF file from given path."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'

        try:
            call = subprocess.run(['pdftotext', '-raw', path, tmp])
        except FileNotFoundError as e:
            print(e)
            return []

        try:
            file_ref = open(tmp, "r")
        except FileNotFoundError as e:
            print(e)
            return []

        quotes = []
        for line in file_ref.readlines():
            if line != "":
                parse = line.split(' - ')
                if len(parse) > 1:
                    quotes.append(QuoteModel.create(str(parse[0]).strip('\"'),
                                                    str(parse[1]).strip('\n')))

        file_ref.close()
        os.remove(tmp)
        return quotes
