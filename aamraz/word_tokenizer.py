import re

class WordTokenizer:
    """
    Kurdish Punctuation-based Tokenizer class.
    """

    def __init__(self):
        # Define Kurdish punctuation characters and patterns
        self.punctuation = r"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~،؛؟«»“”"
        self.pattern = re.compile(rf"(\s+|[{self.punctuation}])")

    def tokenize(self, text):
        """
        Tokenizes the given Kurdish text based on punctuation and spaces.
        Returns a list of tokens.
        """
        # Split the text based on the pattern
        tokens = re.split(self.pattern, text)

        # Filter out empty tokens and strip extra spaces
        tokens = [token.strip() for token in tokens if token.strip()]

        return tokens



