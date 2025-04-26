def word_count(file_contents):
    words = file_contents.split()
    return len(words)


def number_of_characters(file_contents):
    characters = {}
    file_contents = file_contents.lower()
    char_list = list(file_contents)
    for char in char_list:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_on(dictionary):
    return dictionary["num"]


sorted_list = []


def sort_dictionaries(dictionary):
    for character in dictionary:
        count = dictionary[character]
        two_key_pairs = {"char": character, "num": count}
        sorted_list.append(two_key_pairs)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
