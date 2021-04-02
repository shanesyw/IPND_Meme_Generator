"""DOCXIngestor.py implementation."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """A derived class implementing DOCX variant."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse DOCX file from given path."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        try:
            doc = docx.Document(path)
        except (FileNotFoundError,
                docx.opc.exceptions.PackageNotFoundError) as e:
            print(e)
            return []

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                quotes.append(QuoteModel.create(str(parse[0]).strip('\"'),
                                                    str(parse[1])))

        return quotes
