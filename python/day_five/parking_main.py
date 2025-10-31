from parking_function import park_car, remove_car

def main_menu(list_space):
	while True:
		prompt = """
			WELCOME TO OYINAAAADE PARKING MINI PARKING SYSTEM

			1 => Park a car

			2 => Remove a car

			3 => Check for space

			4 => Exit
			"""
		print(prompt)
		option = input("Enter an option: ")

		match option:
			case "1":
				parked_slot = park_car(list_space)
				if parked_slot == "no space":
					print("No space available!!!")
				else:
					print(f"Your car has been  parked at slot {parked_slot}")

			case "2":
				remove = int(input("Enter slot number to remove a car: "))
				if remove_car(list_space, remove):
					print(f"Your car has removed from slot {remove}")
				else:
					print("Invalid input")
            
			case "3":
				print(f"The current parking spaces availaible are: {list_space}")
            
			case "4":
				print("THANK YOU SO MUCH, BUT YOU ARE NOT WELCOME ")
				break

			case _:
				print("Invalid Aboki. Try again!.")


def main():
	list_space = [0] * 20
	print("Available parking slots:", list_space)
	main_menu(list_space)

main()
