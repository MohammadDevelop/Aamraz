import aamraz

# Embedding by fasttext
model_path = '../kurdish_fasttext_skipgram_dim300_v2.bin'
embedding_model = aamraz.EmbeddingModel(model_path, dim=50)

sample_word="ئامراز"
word_vector = embedding_model.word_embedding(sample_word)
print(word_vector)

sample_sentence="زوانی له دربره"
sentence_vector = embedding_model.sentence_embedding(sample_sentence)
print(sentence_vector)

sim_cosine = embedding_model.similarity('زوان', 'ئامراز', method='cosine')
print(f"Cosine similarity between two words: {sim_cosine}")

nearest_words = embedding_model.nearest_words('ئامراز', 5, method='cosine')
print(f"Nearest words: {nearest_words}")
