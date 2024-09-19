import aamraz

# Stemming
stemmer=aamraz.Stemmer(method='simple')
stemmed=stemmer.stem("کتێبەکانمان")
print(stemmed)

stemmer=aamraz.Stemmer(method='porter_snowball')
stemmed=stemmer.stem("کتێبەکانمان")
print(stemmed)