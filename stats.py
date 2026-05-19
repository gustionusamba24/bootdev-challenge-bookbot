from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

def get_num_words(contents: str) -> int:
    words_len = len(contents.split())

    return words_len

def get_num_chars(contents: str) -> dict[str, int]:
    chars_count: dict[str, int] = {}
    
    lowered_text = contents.lower()

    for char in lowered_text:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

    return chars_count

def sort_on(dict_item: CharacterCount) -> int:
    return dict_item["num"]

def sort_chars_list(chars_dict: dict[str, int]) -> list[CharacterCount]:
    sorted_list: list[CharacterCount] = []

    for key, value in chars_dict.items():
        if key.isalpha():
            item: CharacterCount = {"char": key, "num": value}
            sorted_list.append(item)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list