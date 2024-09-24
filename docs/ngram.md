N-gram Models

| **Vector Size**                                                                      | Description | Version | **Size** |
|:-------------------------------------------------------------------------------------|:------------|:--------|:---------|
| [**n=2**](https://mega.nz/file/OQo0HZzT#O6evDUNtKppUhCmyVlL2yvgR5_Q6M2Y7uud8URC1rz4) | .pkl file   | 1       | ~ 43 MB  |
| [**n=3**](https://mega.nz/file/XQ51hSgY#gJwuipuPEvVpPFQZ1zLoMZ20s3oGh_vouH751kaRCHk) | .pkl file    | 1       | ~ 80 MB  |
| [**n=4**](https://mega.nz/file/uUA2DD4R#h1NrNhWY5CsHvSNeiHmm6uW5rTNPvUMlS4_j5oFycgk) | .pkl file    | 1       | ~ 102 MB |
| [**n=5**](https://mega.nz/file/aU4T2IRB#-TAeApOh8Vk1cIUGSk9rs-fUke8AgBbH23frlISqnHQ) | .pkl file    | 1       | ~ 121 MB |


## Usage
```python
import pickle

# Load the N-gram model from the file
with open('ngram_model_n3_v1.pkl', 'rb') as model_file:
    n_gram_freq = pickle.load(model_file)


ngram_value = "بەرمیلێک نزیک دەبێتەوه"

if ngram_value in n_gram_freq:
    print(f"The frequency of '{ngram_value}' is: {n_gram_freq[ngram_value]}")
else:
    print(f"The N-gram '{ngram_value}' is not found in the model.")
```
