import pickle

# Load the N-gram model from the file
with open('ngram_model_n3_v1.pkl', 'rb') as model_file:
    n_gram_freq = pickle.load(model_file)


ngram_value = "بەرمیلێک نزیک دەبێتەوه"

if ngram_value in n_gram_freq:
    print(f"The frequency of '{ngram_value}' is: {n_gram_freq[ngram_value]}")
else:
    print(f"The N-gram '{ngram_value}' is not found in the model.")
