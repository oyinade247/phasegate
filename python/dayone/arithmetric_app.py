import datetime
import random

number_of_questions = 10
correct_answer = 0
start_time = datetime.datetime.now()
count = 0

while count < number_of_questions:
	number_one = random.randint(0, 50)
	number_two = random.randint(0, 50)
	count += 1
	
	#swap = number_one
	#number_one = number_two
	#number_two = swap
	
	prompt = int(input(f"what is {number_one}  - {number_two} = "))
	if number_one - number_two == prompt :
		print("You are correct")
		correct_answer += 1

	elif number_one - number_two != prompt:
		correction = int(input(f"Enter the correctnanswer for the last time: {number_one} - {number_two} = "))

		if number_one - number_two == correction:
			print("you are right") 
			correct_answer += 1

		else:
			print("Fish brain")
			print(f"The correct answer should be {number_one} - {number_two} = {number_one - number_two}")


end_time = datetime.datetime.now()
total_time = start_time - end_time
print(total_time)
print(f" Your total score is {correct_answer} / {number_of_questions}")

			

		
			
		

		

	

