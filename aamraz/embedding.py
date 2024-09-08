import fasttext
import fasttext.util
import numpy as np


class EmbeddingModel:
    def __init__(self, model_path, dim=300):
        """
        Initialize the EmbeddingModel with a FastText model.

        Parameters:
            model_path (str): The path to the FastText model file.
            dim (int): The dimension to reduce the model to (default is 300).
        """
        self.model = fasttext.load_model(model_path)
        fasttext.util.reduce_model(self.model, dim)

    def word_embedding(self, word):
        """
        Get the word vector for a given word.

        Parameters:
            word (str): The word to get the embedding for.

        Returns:
            np.ndarray: The word vector.
        """
        word_vector = self.model.get_word_vector(word)
        return word_vector

    def sentence_embedding(self, sentence):
        """
        Get the sentence vector by averaging the word vectors of the words in the sentence.

        Parameters:
            sentence (str): The sentence to get the embedding for.

        Returns:
            np.ndarray: The sentence vector.
        """
        words = sentence.split()
        word_vectors = [self.model.get_word_vector(word) for word in words]
        sentence_vector = np.mean(word_vectors, axis=0)
        return sentence_vector