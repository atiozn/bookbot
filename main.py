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
        if char in dict:
                dict[char] += 1
        else:
                dict[char] = 1
    return dict

def create_report(count_words, count_chars):
    print("--- Begin report of books/frankenstein.txt ---")       
    print(f"{count_words} words found in the document")
    sorted(count_chars)
    
    for char in count_chars:
           print(f"The {char} character was found {count_chars[char]} times")

    print("--- End report ---")

main()