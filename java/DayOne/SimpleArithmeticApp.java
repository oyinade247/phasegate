import java.util.Scanner;

public class SimpleArithmeticApp{
	public static void main(String [] args){
		
	Scanner input = new Scanner(System.in);
	 int numberOfQuestions = 10;
	 int countCorrectAnswer = 0; 
	long countTime = System.currentTimeMillis();
	

	 int count = 0;
	 //int totalTime = 0;

	 while(count < numberOfQuestions){
	  	int numberOne = (int)(Math.random()*50);
	  	int numberTwo = (int)(Math.random()*50);
	   	count++;


	  //int temp = numberOne;
	 // numberOne = numberTwo;
	 // numberTwo = temp;
 	 
		int highest = Math.max(numberOne, numberTwo);
		int lowest = Math.min(numberOne, numberTwo);

	 	System.out.printf("What is %d %s %d %s",highest, " - " , lowest , "= ");
	 	int answer = input.nextInt();
		
	 	if(highest - lowest == answer){
	  		System.out.println("You are right! ");
	   		countCorrectAnswer++;
	 	}

		else if(highest - lowest != answer){
			System.out.print("Enter the correct answer for the last time: " + highest + "-" +  lowest + ":");
		 	answer = input.nextInt();

			if(highest - lowest == answer){
		 		System.out.println("You are right! ");
				countCorrectAnswer++;
	
			}else{
				System.out.println("fish brain!");
				System.out.printf("You are wrong! %nThe correct answer should be %d %s %d %s %d%n", highest, "-", lowest, "= ",(highest - lowest));

			    }
             	
		}
	 
	  
		 
	 }
		long endTime = System.currentTimeMillis();
	 
	  System.out.printf("The total number of your score is %d%s%d%n ", countCorrectAnswer, "/", numberOfQuestions);	
	 long totalTime = endTime - countTime;
	long total = totalTime / 1000;
	long seconds = total % 60;
	 System.out.print("The time in seconds spent is " + seconds + "seconds");
	 

 }
}
