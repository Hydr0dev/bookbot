def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_char_dict(dict):
    dict_list = dict_to_list(dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def dict_to_list(dict):
    list = []
    for char,count in dict.items():
        list.append({"char": char, "num": count})
    return list
