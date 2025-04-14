sentence = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

new_sentence = sentence.split()
result = []
for word in new_sentence:
    if word[-1] in [",", "."]:
        sym = word[-1]
        base = word[:-1]
        new_word = base + "ing" + sym
    else:
        new_word = word + "ing"
    result.append(new_word)

new_result = " ".join(result)
print(new_result)
