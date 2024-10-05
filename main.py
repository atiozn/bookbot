def main():
	file_path = "books/frankenstein.txt"
	book_content = get_book(file_path)
	number_of_words = countwords(book_content)
	print(f"Amount of words: {number_of_words}")

def get_book(file):
	with open(file) as f:
		file_content = f.read()
	return file_content

def countwords(words):
	single_words = words.split()
	return len(single_words)

main()