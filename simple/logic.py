import operator
from nltk.tokenize import word_tokenize


def count_vocabulary(text):
    tokens = word_tokenize(text)
    return {
        'tokens': __count_tokens(tokens),
        'word_types': __count_word_types(tokens),
        'lexical_diversity': "{0:.5f}".format(__calculate_lexical_diversity(tokens)),
        'word_type_collection': __calculate_word_types_percentage(tokens)
    }


def __count_tokens(text):
    return len(text)


def __count_word_types(text):
    return len(set(text))


def __calculate_lexical_diversity(text):
    return __count_tokens(text) / __count_word_types(text)


def __calculate_word_types_percentage(text):
    data = {}
    for token in set(text):
        data[token] = text.count(token) / len(text)
    return sorted(data.items(), key=operator.itemgetter(1), reverse=True)
