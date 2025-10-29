def remove_unique(numbers):
	unique = []
	for num in numbers:
		if num not in unique:
			unique.append(num)
	return unique

numbers = [1,1,2,2,2,3,3,3]
print( remove_unique(numbers))