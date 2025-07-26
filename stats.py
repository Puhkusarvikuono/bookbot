def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_character_count(text):
    text = text.lower()
    character_list = list(text)
    character_counter = {}
    for character in character_list:
        if character not in character_counter:
            character_counter[character] = 1
        else:
            character_counter[character] += 1
    return character_counter

def get_name(item):
    return item['num']

def dictionary_sorter(dictionary):
    sorted_dictionary = []
    for item in dictionary:
        if item.isalpha():
           named_dict = {'name': item, 'num': dictionary[item]}
           sorted_dictionary.append(named_dict)
    return sorted(sorted_dictionary, reverse=True, key=get_name)
