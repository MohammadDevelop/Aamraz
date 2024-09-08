import fasttext
import fasttext.util
import numpy as np
import gensim
from gensim.models import Word2Vec
import re

class EmbeddingModel:
    def __init__(self, model_path, type='fasttext', dim=300):
        """
        Initialize the EmbeddingModel with a FastText model.

        Parameters:
            model_path (str): The path to the FastText model file.
            type (str): embedding type (default is FastText).
            dim (int): The dimension to reduce the model to (default is 300).
        """
        self.type = type
        if self.type =='fasttext':
            self.model = fasttext.load_model(model_path)
            fasttext.util.reduce_model(self.model, dim)
        if self.type =='word2vec':
            self.model = Word2Vec.load(model_path)

    def word_embedding(self, word):
        """
        Get the word vector for a given word.

        Parameters:
            word (str): The word to get the embedding for.

        Returns:
            np.ndarray: The word vector.
        """
        if self.type =='fasttext':
            word_vector = self.model.get_word_vector(word)
            return word_vector
        if self.type =='word2vec':
            if word in self.model.wv:
                return self.model.wv[word]
            else:
                # Return a zero vector for OOV words
                return np.zeros(self.model.vector_size)


    def sentence_embedding(self, sentence):
        """
        Get the sentence vector by averaging the word vectors of the words in the sentence.

        Parameters:
            sentence (str): The sentence to get the embedding for.

        Returns:
            np.ndarray: The sentence vector.
        """

        if self.type =='fasttext':
            words = sentence.split()
            word_vectors = [self.model.get_word_vector(word) for word in words]
            sentence_vector = np.mean(word_vectors, axis=0)
            return sentence_vector

        if self.type =='word2vec':
            words = re.split(r'\s+|[.,!?;:"()«»“”]', sentence)  # Simple punctuation-based tokenizer
            word_embeddings = [self.word_embedding(word) for word in words if word]

            if len(word_embeddings) > 0:
                # Return the average of the word embeddings
                return np.mean(word_embeddings, axis=0)
            else:
                # Return a zero vector if no valid words are found
                return np.zeros(self.model.vector_size)

