def check_pangram(phrase):
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z'}

    phrase_dict = set(phrase)
    return phrase_dict >= letters


print(check_pangram('the quick brown fox jumps over the lazy dog'))
