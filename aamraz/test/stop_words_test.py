import aamraz

tokenizer = aamraz.WordTokenizer()
sample_sentence="هەندێک وشە زۆر بە تێپەڕ وەکاتی تێدایە لە ئەدەبیاتدا."
tokens = tokenizer.tokenize(sample_sentence)
print(tokens)

clean_tokens=aamraz.util.remove_stop_words(tokens)
print(clean_tokens)
