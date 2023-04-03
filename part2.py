#Written by Shiven Desai
def most_frequent_char(s):
    char_count = {}
    for ch in s:
        if ch.isalpha():
            ch = ch.lower()
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1
    max_count = max(char_count.values())
    most_frequent = [ch for ch, count in char_count.items() if count == max_count]
    return most_frequent

string = input("Enter a string: ")
most_frequent = most_frequent_char(string)
print("Most frequent character(s):", most_frequent)
