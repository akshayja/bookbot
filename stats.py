def count_words(file_contents):
    words =  file_contents.split()
    num_words = len(words)
    return num_words

def count_characters(file_contents):
    char_counts = {}
    for char in file_contents.lower():
        if char in char_counts:
            char_counts[char] = char_counts[char]+1
        else:
             char_counts[char] = 1
    return char_counts

def sort_characters(char_counts):
    chars = []

    for char, count in char_counts.items():
        if char.isalpha():
            chars.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    chars.sort(reverse=True, key=sort_on)
    return chars