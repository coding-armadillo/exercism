from string import ascii_lowercase
def is_pangram(sentence):
    return len(set(sentence.lower()) & set(ascii_lowercase))==26
    