const prompt = require('prompt-sync')();



function main(){
	listSpace = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	console.log( listSpace);
	mainMenu(listSpace);
}


function mainMenu(listSpace){
		let text = `
			WELCOME TO OYINAAAADE PARKING MINI PARKING SYSTEM

			1 => Park a car

			2 => Remove a car

			3 => Check for space

			4 => Exit
			`;

		console.log(text);
	
	

		let option = prompt("Enter an option: ")

		switch (option){
			case "1":
				parkedSlot = parkCar(listSpace)
				if (parkedSlot === "no space"){
					console.log("No space available!!!");
				}
				else{
					console.log("Your car has been  parked at slot " + parkedSlot );
				}
				mainMenu(listSpace)

			case "2":
				let remove = prompt ("Enter slot number to remove a car: ");
				if (removeCar(listSpace, remove)){
					console.log("Your car has removed from slot" + remove);
				}
				else{
					console.log("Invalid input");
					}
				mainMenu(listSpace)


			case "3":
				console.log(listSpace)
				


			case "4":
				console.log("See you next time!");
				process.exit();

			
			default :
				console.log("invalid input");
				mainMenu(listSpace)
            



			}


}


function parkCar(listSpace){
	for(let count = 0; count < listSpace.length; count++)
		if (listSpace[count] == 0){
			listSpace[count] = 1
			return count + 1
	}
	return "no space"
}		


function removeCar(listSpace, remove){
		if (remove <= listSpace.length){

			if (listSpace[remove - 1] == 1){
				listSpace[remove - 1] = 0
			return "removed"
			}
		else{
			return "invalid"}
		}
	return "space does not exist"
}

main();