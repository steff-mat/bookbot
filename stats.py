def get_num_words(path_to_file):
    with open(path_to_file) as file:
        book = file.read()
        book_words = book.split()
        return len(book_words)

def get_char_count(path_to_file):
    word_count = {}
    with open(path_to_file) as file:
        letter_list = list(file.read())
        for letter in letter_list:
            if letter.lower() in word_count.keys():
                word_count[letter.lower()] += 1
            else:
                word_count[letter.lower()] = 1
    return word_count

def get_sorted_letters(path_to_file):
    def sort_on(items):
        return items["num"]
    
    count_list = []
    letter_list =  get_char_count(path_to_file)
    
    for letter in letter_list:
        if letter.isalpha():
            count_list.append({"char" : letter, "num": letter_list[letter]})
    
    count_list.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Inalyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path_to_file)} total words")
    print("--------- Character Count -------")
    for letter in count_list:
        print(f"{letter["char"]}: {letter["num"]}")
