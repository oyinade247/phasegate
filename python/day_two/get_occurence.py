def occurence(word):
	unique = []
	count = 0
	for char in word:
		if char not in unique:
			unique.append(char)
			count += 1
	return unique


