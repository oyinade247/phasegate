import random

def suggest_question(database_one):
	index = random.randint(0, len(database_one)- 1)
	suggest = database_one[index]
	return suggest

def suggest_option(database_two):
	index = random.randint(0,len(database_two)-1)
	return index


def check_answer(database_one, database_two, answer, capital):
	if type(answer) is not int:
		raise TypeError("invalid input")

	if answer < 0 or answer >= len(database_two):
		raise ValueError("your input is out of range")
	index_state = database_one.index(capital)
	correct_capital = database_two[index_state]
	answer = int(answer)
	user_choice = database_two[answer]

	if user_choice == correct_capital:
        	return "Correct"
	else:
		return f"Wrong The correct answer is {correct_capital}"







	



















































	
	