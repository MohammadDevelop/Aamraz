import fasttext
import fasttext.util
import numpy as np
import gensim
from gensim.models import Word2Vec
import re


class EmbeddingModel:
    def __init__(self, model_path, type='fasttext', dim=300):
        """
        Initialize the EmbeddingModel with a FastText or Word2Vec model.

        Parameters:
            model_path (str): The path to the model file.
            type (str): Embedding type (default is FastText).
            dim (int): The dimension to reduce the model to (default is 300).
        """
        self.type = type
        self.dim = dim
        if self.type == 'fasttext':
            self.model = fasttext.load_model(model_path)
            fasttext.util.reduce_model(self.model, dim)
        if self.type == 'word2vec':
            self.model = Word2Vec.load(model_path)

    def get_dim(self):
        return self.dim

    def word_embedding(self, word):
        """
        Get the word vector for a given word.

        Parameters:
            word (str): The word to get the embedding for.

        Returns:
            np.ndarray: The word vector.
        """
        if self.type == 'fasttext':
            return self.model.get_word_vector(word)
        if self.type == 'word2vec':
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
        words = re.split(r'\s+|[.,!?;:"()«»“”]', sentence)
        word_embeddings = [self.word_embedding(word) for word in words if word]

        if len(word_embeddings) > 0:
            return np.mean(word_embeddings, axis=0)
        else:
            return np.zeros(self.model.vector_size)

    def similarity(self, word1, word2, method='cosine'):
        """
        Compute similarity between two words using the specified method.

        Parameters:
            word1 (str): First word.
            word2 (str): Second word.
            method (str): The method to compute similarity. Options are:
                          'cosine', 'euclidean', 'manhattan'.

        Returns:
            float: Similarity score between word1 and word2.
        """
        vector1 = self.word_embedding(word1)
        vector2 = self.word_embedding(word2)

        # Ensure word vectors are valid
        if np.linalg.norm(vector1) == 0 or np.linalg.norm(vector2) == 0:
            return 0.0  # Return 0 if one of the words is OOV (out of vocabulary)

        # Compute the similarity based on the chosen method
        if method == 'cosine':
            # Cosine Similarity
            dot_product = np.dot(vector1, vector2)
            norm1 = np.linalg.norm(vector1)
            norm2 = np.linalg.norm(vector2)
            return dot_product / (norm1 * norm2)

        elif method == 'euclidean':
            # Euclidean Distance
            return -np.linalg.norm(vector1 - vector2)

        elif method == 'manhattan':
            # Manhattan Distance (L1 norm)
            return -np.sum(np.abs(vector1 - vector2))

        else:
            raise ValueError(f"Unknown method: {method}. Supported methods: 'cosine', 'euclidean', 'manhattan'")

    def nearest_words(self, word, top_n=5, method='cosine'):
        """
        Find the most similar words to a given word using the specified similarity method.

        Parameters:
            word (str): The word to find similar words for.
            top_n (int): The number of nearest words to return (default is 5).
            method (str): The method to compute similarity. Options are:
                          'cosine', 'euclidean', 'manhattan'.

        Returns:
            list of tuples: List of (word, similarity) tuples.
        """
        if self.type == 'fasttext':
            vocab = self.model.get_words()
        elif self.type == 'word2vec':
            vocab = list(self.model.wv.index_to_key)
        else:
            return []

        word_vector = self.word_embedding(word)
        similarities = []

        for vocab_word in vocab:
            if vocab_word != word:
                similarity = self.similarity(word, vocab_word, method=method)
                similarities.append((vocab_word, similarity))

        # Sort by similarity and return the top_n most similar words
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
        return similarities[:top_n]

    def nearest_to_vector(self, vector, top_n=5, method='cosine'):
        """
        Find the most similar words to a given vector using the specified similarity method.

        Parameters:
            vector (np.ndarray): The vector to compare with words in the vocabulary.
            top_n (int): The number of nearest words to return (default is 5).
            method (str): The method to compute similarity. Options are:
                          'cosine', 'euclidean', 'manhattan'.

        Returns:
            list of tuples: List of (word, similarity) tuples.
        """
        if self.type == 'fasttext':
            vocab = self.model.get_words()
        elif self.type == 'word2vec':
            vocab = list(self.model.wv.index_to_key)
        else:
            return []

        similarities = []

        for vocab_word in vocab:
            vocab_vector = self.word_embedding(vocab_word)
            # Compute similarity between the input vector and vocab vector
            if method == 'cosine':
                similarity = np.dot(vector, vocab_vector) / (np.linalg.norm(vector) * np.linalg.norm(vocab_vector))
            elif method == 'euclidean':
                similarity = -np.linalg.norm(vector - vocab_vector)
            elif method == 'manhattan':
                similarity = -np.sum(np.abs(vector - vocab_vector))
            else:
                raise ValueError(f"Unknown method: {method}. Supported methods: 'cosine', 'euclidean', 'manhattan'")

            similarities.append((vocab_word, similarity))

        # Sort by similarity and return the top_n most similar words
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
        return similarities[:top_n]
