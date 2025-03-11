def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(text):
    new_book_text = get_book_text("books/frankenstein.txt")
    num_words = 0
    for num in new_book_text.split():
        num_words += 1
    
    return num_words

def count_character(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_dic(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list