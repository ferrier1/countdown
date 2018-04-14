import pickle

valid_words = {}
with open('word_list.txt') as f:
    x = f.read().strip().split()
    for word in x:
        temp_dict = {''.join(sorted(word)): word}
        valid_words.update(temp_dict)
pickle.dump(valid_words, open('word_list.p', 'ab'))
