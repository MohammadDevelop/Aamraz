# Aamraz - Kurdish NLP collection

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Pre-trained Models](#PretrainedModels)
- [Usage](#usage)

## Overview
Aamraz which is written "ئامراز" in kurdish script means "instrument". This project is a collection of Natural Language Processing tools for Kurdish Language.
Despite being spoken by millions, Kurdish remains an under-resourced language in Natural Language Processing (NLP).
Recognizing the rich cultural heritage and historical significance of the Kurdish people, we—regardless of ethnicity—are committed to advancing tools and pre-trained models that empower the Kurdish language in modern research and technology.
Our work aims to foster further development and provide a foundation for future research and applications in NLP.

## Base Features
- **Normalization** 
- **Tokenization** 
- **Stemming**
- **Word Embedding:** Creates vector representations of words.
- **Sentences Embedding:** Creates vector representations of sentences.

## Tools

## Installation
    pip install aamraz
## PretrainedModels

some useful pre-trained Models:

| **Model**                                                                                                 | Version | Description                                                                                                                                                                                                    | **Size** |
|:----------------------------------------------------------------------------------------------------------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| [**FastText WordEmbedding**](https://mega.nz/file/bBhn1aaL#6QBlZT5QmFx4HCufcQ8Vr9hwPGNu2hvrh9_f_A8aoXM)   | 3       | Model trained using [FastText](https://fasttext.cc/) method on our own Corpus.<br/> This is bot the fasttext & skip-gram model itself ([fasttext model](https://fasttext.cc/docs/en/pretrained-vectors.html).) | ~ 2.3 GB |
| [**FastText WordEmbedding - Lite**](https://mega.nz/file/aRwQVaZa#nDmXYeFRWOm229NBgqvuk5Od0nd7mGxAQwn6B61Dtfs) | 2       | Model trained using [FastText](https://fasttext.cc/) method on our own Corpus.<br/> This is bot the fasttext & skip-gram model itself ([fasttext model](https://fasttext.cc/docs/en/pretrained-vectors.html).) | ~ 800 MB |
| [**Word2vec Model**](https://mega.nz/file/2FxR2L7R#0B1NriaXe08y1sDMluNxJ5aY00d0s8iiXP5-g7xYcwU)                | 1       | Including needed .bin and .npy files. Find other vector sizes [Here](docs/word2vec.md))                                                                                                                        | ~ 92 MB  |

- [**All Fasttext Models**](docs/fasttext.md) 
- [**All N-gram Models**](docs/ngram.md) 

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

- [**Stop Word Removal**](docs/stop_words.md) 
