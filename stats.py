def get_num_words(string):
    words = string.split()
    return len(words)

def get_char_count(string):
    chars = {}
    string = string.lower()
    for char in string:
        if char in chars:
            chars[char] +=1
        else:
            chars[char] =1
    
    return chars

def sort_by_count(item):
    return item["num"]

def sort_chars(chars):
    items = []

    for char in chars:
        if (char != ' ' and char != '\n'):
            items.append({"char": char, "num": chars[char]})

    items.sort(reverse=True, key=sort_by_count)

    return items