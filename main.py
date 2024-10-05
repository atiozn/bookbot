def main():
	file_path = "books/frankenstein.txt"
	book_content = get_book(file_path)
	number_of_words = count_words(book_content)
	print(f"Amount of words: {number_of_words}")
	count_chars(book_content)

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
    print(dict)
main()