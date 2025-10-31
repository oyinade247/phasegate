def park_car(list_space):
	for space in range(len(list_space)):
		if list_space[space] == 0:
			list_space[space] = 1
			return space + 1
	return "no space"


def remove_car(list_space, remove):
	if remove > len(list_space):
		raise ValueError("Invalid input")
	if type(remove) is not int:
		raise TypeError("invalid input")
	if remove <= len(list_space):
		if list_space[remove - 1] == 1:
			list_space[remove - 1] = 0
			return "removed"
		else:
			return "invalid"
	else:
		return "space does not exist"










 