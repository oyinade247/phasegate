
def isPalindrome(list):
	for count in range(0, len(list)):
		word = list[count]
		reversed = ""
		
		for char in str(word):
			reversed = char + reversed
		if reversed == word:
			list[count] = True
		
		else:
			list[count] = False
	
	return list


list =  ["madam", "racecar", "hello", "noon","ewe", "ada"];
print(isPalindrome(list))
		

		

		

			


