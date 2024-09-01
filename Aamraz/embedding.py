import fasttext
import fasttext.util
import numpy as np

def word_embedding(word, model_path, dim):
    model = fasttext.load_model(model_path)
    fasttext.util.reduce_model(model, dim)
    word_vector = model.get_word_vector(word)
    return word_vector

def sentence_embedding(sentence, model_path, dim):
    model = fasttext.load_model(model_path)
    fasttext.util.reduce_model(model, dim)
    words = sentence.split()
    word_vectors = [model.get_word_vector(word) for word in words]
    sentence_vector = np.mean(word_vectors, axis=0)
    return sentence_vector