"""Ingestor.py implementation."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """A derived class implementing CSV variant."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file from given path."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            df = pandas.read_csv(path, header=0)
        except FileNotFoundError as e:
            print(e)
            return []

        for index, row in df.iterrows():
            quotes.append(QuoteModel.create(row['body'], row['author']))

        return quotes
