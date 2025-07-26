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
