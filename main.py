def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        words = file_contents.split()
        print(len(words))
        char_dict = count_characters(file_contents)
        print(char_dict)
        sort_on(char_dict, words)
        


def count_characters(file_contents):
    lowered_string = file_contents.lower()
    dictionary = {}
    for i in lowered_string:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
        
    return dictionary


def sort_on(dictionary, words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    for key, value in dictionary.items():
        print(f"The {key} character was found {value} times")


main()

