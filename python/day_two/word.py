
def backward(words, ch):
	for word in words:
		if word in  ch:
			store = words[3::-1] + words[3:]

	return store


words = "abcdefd"

ch = "d"

store = ""

print(backward(words, ch))


		
		