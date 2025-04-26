from stats import word_count
from stats import char_count
from stats import dict_sort
import sys

def main():
	try:
		if len(sys.argv) < 2:
			print("Usage: python3 main.py <path_to_book>")
			sys.exit(1)
		file_location = sys.argv[1]
		text = get_book_text(file_location)
		num_words = word_count(text)
		characters = dict_sort(char_count(text)) 
		print("============ BOOKBOT ============")
		print("Analyzing book found at books/frankenstein.txt...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for char in characters:
			print(f"{char['char']}: {char['num']}")
		#print(f"{num_words} words found in the document")
		#print(characters)

	except Exception as e:
		print(f"Error encountered: {e}")

def get_book_text(file_path): # path to book file (accepted file types?)
	with open(file_path) as f:
		file_contents = f.read() # we have book open as f, now read contents into a string
	return file_contents #return the string

main()
