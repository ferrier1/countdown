import pickle
import itertools


def countdown(letters):
    valid_words = pickle.load(open('word_list.p', 'rb'))
    letters = sorted(letters)
    for n in range(6, 10):
        for word in itertools.combinations(letters, n):
            x = ''.join(word)
            if x in valid_words.keys():
                print(valid_words[x])


countdown('rvarakad')
