#Written by Shiven Desai
def pig_latin(s):
    words = s.split()
    pig_latin_words = []
    for word in words:
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    return " ".join(pig_latin_words)

string = input("Enter a sentence: ")
pig_latin_string = pig_latin(string)
print("Pig Latin sentence:", pig_latin_string)
