def main():
	file_path = "books/frankenstein.txt"
	book_content = get_book(file_path)
	create_report(count_words(book_content), count_chars(book_content))

def get_book(file):
	with open(file) as f:
		file_content = f.read()
	return file_content

def count_words(words):
	single_words = words.split()
	return len(single_words)

def count_chars(words):
    dict = {}
    words = words.lower()
    for char in words:
        if char.isalpha():
            if char in dict:
                    dict[char] += 1
            else:
                    dict[char] = 1
    return dict

def create_report(count_words, count_chars):
    print("--- Begin report of books/frankenstein.txt ---")       
    print(f"{count_words} words found in the document")
    
    converted_list = dict_to_list(count_chars)
    converted_list.sort(reverse=True, key=sort_on)

    for dict in converted_list:
        for key in dict:
           print(f"The {key} character was found {dict[key]} times")

    print("--- End report ---")

def sort_on(dict):
       for c in dict:
             return dict[c]
 
def dict_to_list(dict):
    list_of_dict = []
    for key in dict:
          new_dict = {key:dict[key]}
          list_of_dict.append(new_dict)
    return list_of_dict
       

main()