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
	
	highest = max(number_one, number_two)
	lowest = min(number_one, number_two)
	
	prompt = int(input(f"what is {highest}  - {lowest} = "))
	if highest - lowest == prompt :
		print("You are correct")
		correct_answer += 1

	elif highest - lowest != prompt:
		correction = int(input(f"Enter the correctnanswer for the last time: {highest} - {lowest} = "))

		if highest - lowest == correction:
			print("you are right") 
			correct_answer += 1

		else:
			print("Fish brain")
			print(f"The correct answer should be {highest} - {lowest} = {highest - lowest}")


end_time = datetime.datetime.now()
total_time = start_time - end_time
print(total_time)
print(f" Your total score is {correct_answer} / {number_of_questions}")

			

		
			
		

		

	

