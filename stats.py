def get_book_text(filepath):
    """ Take a filepath as input and return the contents as a string """
    with open(filepath) as f:
        book = f.read()
        return book
    
def count_words(book):
    """ Take a book as an input and return its word count as an int """
    return len(book.split())

def count_char(book):
    """ Take a string as an input and reuturn its character count as a dictionary.
        e.g.: dict = { "r" : 65, "." : 128} """

    count = {}

    # Convert the entire book to lowercase and iterate through it character by character
    for char in book.lower():

        # Update the count for the character
        count[char] = count.get(char, 0) + 1

    return count

def sort_char(char_count):
    """  Take a dictionary of characters and their counts and return a sorted list of dictionaries """
    
    # Define our sorted list that will be returned
    list_of_dicts = []

    for char, count in char_count.items():
        list_of_dicts.append({"char": char, "num": count})

    sorted_list = sorted(
        list_of_dicts,
        key=lambda item: item["num"],
        reverse=True        
    )

    return sorted_list
