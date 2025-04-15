words = {"I": 3, "love": 5, "Python": 1, "!": 50}


def key_multiplier(any_dict):
    for key, multiplier in any_dict.items():
        print(key * multiplier)


key_multiplier(words)
