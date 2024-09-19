import aamraz

# Normalization
normalizer= aamraz.Normalizer()
sample_sentence="قڵبە‌کە‌م‌ بە‌  کوردی‌  قسە‌ دە‌کات‌."
normalized_sentence=normalizer.normalize(sample_sentence)
print(normalized_sentence)

# Tokenization
tokenizer = aamraz.WordTokenizer()
sample_sentence="زوانی له دربره"
tokens = tokenizer.tokenize(sample_sentence)
print(tokens)

# Embedding by fasttext
model_path = 'kurdish_fasttext_skipgram_dim300_v1.bin'
embedding_model = aamraz.EmbeddingModel(model_path, dim=50)

sample_word="ئامراز"
sample_sentence="زوانی له دربره"

word_vector = embedding_model.word_embedding(sample_word)
sentence_vector = embedding_model.sentence_embedding(sample_sentence)

print(word_vector)
print(sentence_vector)

# Embedding by word2vec
model_path = 'kurdish_word2vec_model_dim100_v1.bin'
embedding_model = aamraz.EmbeddingModel(model_path, type='word2vec')

sample_word="ئامراز"
sample_sentence="زوانی له دربره"

word_vector = embedding_model.word_embedding(sample_word)
sentence_vector = embedding_model.sentence_embedding(sample_sentence)

print(word_vector)
print(sentence_vector)

# Stemming
stemmer=aamraz.Stemmer(method='simple')
stemmed=stemmer.stem("کتێبەکانمان")
print(stemmed)

