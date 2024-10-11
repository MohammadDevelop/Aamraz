# Aamraz - Kurdish NLP collection

## Overview
Aamraz which is written "ئامراز" in kurdish script means "instrument". This project is a collection of Natural Language Processing tools for Kurdish Language.
Despite being spoken by millions, Kurdish remains an under-resourced language in Natural Language Processing (NLP).
Recognizing the rich cultural heritage and historical significance of the Kurdish people, we—regardless of ethnicity—are committed to advancing tools and pre-trained models that empower the Kurdish language in modern research and technology.
Our work aims to foster further development and provide a foundation for future research and applications in NLP. [see github repository](https://github.com/MohammadDevelop/Aamraz)


## Installation
    pip install aamraz

## Base Features
- **Normalization** 
- **Tokenization** 
- **Stemming**
- **Word Embedding:** Creates vector representations of words.
- **Sentences Embedding:** Creates vector representations of sentences.

## Usage
```python
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
```

