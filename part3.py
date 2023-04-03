#Written by Shiven Desai
def separate_words(s):
    words = []
    word = ""
    for ch in s:
        if ch.isupper():
            if word:
                words.append(word)
            word = ch.lower()
        else:
            word += ch
    words.append(word)
    words[0] = words[0].capitalize()
    return " ".join(words)

string = input("Enter a sentence: ")
separated = separate_words(string)
print("Separated sentence:", separated)
