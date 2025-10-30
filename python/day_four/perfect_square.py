list =  [4, 9, 25, 49]

def is_perfect_square(list):
	for count in range(0, len(list)):
		number = list[count]
		divisor = 2
		while number % divisor != 0:
			divisor += 1

		dividedIndex = number / divisor

		if number == dividedIndex * dividedIndex:
			list[count] = True
		else:
			list[count] = False
            	
	return list

number =  {4, 9, 25, 49}

print(is_perfect_square(list))
	
		
  
