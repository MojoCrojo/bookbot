def word_count(book): #input a string
	word_list = book.split()
	return len(word_list)

def char_count(book): # count of each character, including spaces
	book_lower = book.lower()
	char_dict = {}
	for char in book_lower:
		if char not in char_dict:
			char_dict[char] = 0
		char_dict[char] += 1
	return char_dict

def sort_on(dict):
	return dict["num"]

def dict_sort(char_dict):
	characters = []
	for char in char_dict:
		if char.isalpha():
			characters.append({"char":char, "num":char_dict[char]})
	characters.sort(reverse=True, key=sort_on)
	return characters