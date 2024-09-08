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

# Embedding
model_path = 'kurdish_fasttext_skipgram_dim300_v1.bin'
embedding_model = aamraz.EmbeddingModel(model_path, dim=50)

sample_word="ئامراز"
sample_sentence="زوانی له دربره"

word_vector = embedding_model.word_embedding(sample_word)
sentence_vector = embedding_model.sentence_embedding(sample_sentence)

print(word_vector)
print(sentence_vector)