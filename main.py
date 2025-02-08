def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document\n")
        char_map = count_chars(file_contents)
        for key, value in char_map.items():
            print(f"The '{key}' character was found {value} times")
        print("--- End report ---")

def count_words(words:str)->int:
    # split by whitespace
    word_list = words.split()
    return len(word_list)

def count_chars(words:str)->dict[str, int]:
    words = words.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_map = {}
    for char in words:
        if char not in alphabet:
            continue
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1
    return char_map 
main()
