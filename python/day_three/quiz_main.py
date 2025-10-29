from quiz_functions import suggest_question,suggest_option,check_answer

def main_menu(database_two,database_one, count):
	prompt = """
		WELCOME TO OYINADE QUIZ GAME
		
		1 => PLAY 

		2 => CHECK FOR SCORE

		3 => EXIT...

		
		""";
	print(prompt)
	option = input("Enter any key from above: ")
	match option:
		case "1" : 
			capital = suggest_question(database_one)
			option = suggest_option(database_two)

			print(f"What is the capital of {capital} ?")
			for index, option in enumerate(database_two):
				print(f"{index}  {option}\n")
			answer = int( input("Enter a number from the options:"))

			result = check_answer(database_one,database_two, answer, capital)
			print(result)
			
			if result == "Correct":
				count += 1
			main_menu(database_two,database_one, count)


			

		case "2" : 
			print(f"Your current score is {count}")
			main_menu(database_two,database_one, count)

		case "3" :
			print(f"Thanks for playing \n Exiting.........") 

		case default:
			print("invalid input")
			main_menu(database_two,database_one, count)

			
			
			
			
			
											
				
				
				
				
				


			
			

		
			
			



	










def main():
	count = 0
	database_one = ["oyo", "lagos", "ogun","ondo", "enugu", "ekiti","semicolon village", "mr ebuka"]

	database_two = ["ibadan", "ikeja","abeokuta","akure","enugu", "ado-ekiti","semicolon palace","oyinaaaade"]
	main_menu(database_two,database_one,count)
	


main()



