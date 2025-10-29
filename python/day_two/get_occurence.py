def get_occurence(word, ch):
	count = 0

	for char in word.lower():
		if letter in char:
			count += 1		
			
	return count




word = "Hello World"
letter = "d"
print(get_occurence(word, letter))
