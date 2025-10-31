import java.util.Scanner;
public class ParkingSlot{
	
	public static void main(String [] args){
	int [] listSpace = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
	 mainMenu(listSpace);
	}


public static void mainMenu(int [] listSpace){
		System.out.println( """
			WELCOME TO OYINAAAADE PARKING MINI PARKING SYSTEM

			1 => Park a car

			2 => Remove a car

			3 => Check for space

			4 => Exit
			""");

		//System.out.print(prompt);
		Scanner input = new Scanner(System.in);
		System.out.print("Enter any key from above: ");
		String option = input.nextLine();
	
		
		switch (option){
			case "1":
				int parkedCar = parkCar(listSpace);
				if (parkedCar == 0){
					System.out.print("No space available!!!");
				}
				else{
					System.out.print("Your car has been  parked at slot " + parkedCar );
				}
				mainMenu(listSpace);

			case "2":
				System.out.print ("Enter slot number to remove a car: ");
				int remove = input.nextInt();
				String removed = removeCar(listSpace, remove);
				boolean myRemoved = Boolean.parseBoolean(removed);
				if ( myRemoved){
					System.out.print("Your car has removed from slot" + remove);
				}
				else{
					System.out.print("Invalid input");
					}
				mainMenu(listSpace);


			case "3":
				System.out.print(listSpace);
				


			case "4":
				System.out.print("See you next time!");

			
			 default :
				System.out.print("invalid input");
				mainMenu(listSpace);
            



			}




}







public static int parkCar(int []listSpace){
	for(int count = 0; count < listSpace.length; count++)
		if (listSpace[count] == 0){
			listSpace[count] = 1;
			return count + 1;
	}
	return 0;
}		


public static String removeCar(int [] listSpace, int remove){
		if (remove <= listSpace.length){

			if (listSpace[remove - 1] == 1){
				listSpace[remove - 1] = 0;
			return "removed";
			}
		else{
			return "invalid";}
		}
	return "space does not exist";
}


}
