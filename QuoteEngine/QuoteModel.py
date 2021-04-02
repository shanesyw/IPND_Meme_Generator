"""QuoteModel.py implementation."""


class QuoteModel():
    """A class to represent a set of quote (body + author)."""

    def __init__(self, body, author):
        """Initialize instance."""
        self.body = body
        self.author = author

    @classmethod
    def create(cls, body, author):
        """
        A classmethod to quickly create QuoteModel.

        :param info: A list of variadic positional arguments
        supplied to the constructor.
        """
        return cls(body, author)

    def __str__(self):
        """return str(self)."""
        return f"\"{self.body}\" - {self.author}"

    def __repr__(self):
        """return repr(self)."""
        return f'<{self.body}, {self.author}>'
