# Aamraz - Kurdish NLP collection

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Pre-trained Models](#PretrainedModels)
- [Usage](#usage)

## Overview
Aamraz which is written "ئامراز" in kurdish script means "instrument". This project is a collection of Natural Language Processing tools for Kurdish Language.

## Base Features
- **Normalization** 
- **Tokenization** 
- **Word Embedding:** Creates vector representations of words.
- **Sentences Embedding:** Creates vector representations of sentences.

## Tools

## Installation
    pip install aamraz
## PretrainedModels

some useful pre-trained Models:

| **Model**                                                                                                      | Description                                                                                                                                                                                                   | **Size** |
|:---------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| [**FastText WordEmbedding**](https://mega.nz/file/yNYVnDgQ#xoPydAT_75vEu0jXQIFxetFtFScdyFJpmCsAwjVUAzQ)        | Model trained using [FastText](https://fasttext.cc/) method on our own Corpus.<br/> This is bot the fasttext & skip-gram model itself ([fasttext model](https://fasttext.cc/docs/en/pretrained-vectors.html). | ~ 2.3 GB |
| [**FastText WordEmbedding - Lite**](https://mega.nz/file/qIJ1hRoD#sctXghLp-P1O8Cg1NhOBFkum6KH0ACiHpZS-GeRwB4Q) | Model trained using [FastText](https://fasttext.cc/) method on our own Corpus.<br/> This is bot the fasttext & skip-gram model itself ([fasttext model](https://fasttext.cc/docs/en/pretrained-vectors.html). | ~ 800 MB |
| [**Word2vec Model**](https://mega.nz/file/2FxR2L7R#0B1NriaXe08y1sDMluNxJ5aY00d0s8iiXP5-g7xYcwU)                | Including needed .bin and .npy files                                                                                                                                                                          | ~ 92 MB  |

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
```


## License

This project is licensed under the MIT License. You are free to use, distribute, modify, and build upon this work, even for commercial purposes, as long as you include a copy of the original MIT License and provide proper attribution.

To view a copy of this license, visit:
https://opensource.org/licenses/MIT