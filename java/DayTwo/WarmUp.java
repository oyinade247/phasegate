import java.util.Scanner;
public class WarmUp{

	public static void main(String [] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter number of item:");
		double num = input.nextDouble();

		
		System.out.print(getNumberOfYear(num));
		
	}

public static double getNumberOfYear(double number){
	double fixPrice = 50000;
	double depreciation = 0.08;
	double  multiplyFixedPrice = fixPrice * number;
	double rate = multiplyFixedPrice * depreciation;
	int count = 0;
	double multiply = multiplyFixedPrice ;

	while(multiply > 0){
	
	multiply -= rate;
		count++;
		
		
		}

		return count;
	
	
	

}




}