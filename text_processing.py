from nltk.tokenize import word_tokenize

def split_by_token(text, max_tokens):
    words = word_tokenize(text)
    return [' '.join(words[i:i+max_tokens]) for i in range(0, len(words), max_tokens)]
