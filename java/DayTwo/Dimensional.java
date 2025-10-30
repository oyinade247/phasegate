import java.util.Arrays;
public class HighestTwoD{
	public static void main(String[] args){

	double [][] number = {
	{1.5, 2.3, 3.7, 4.6},
	{5.1,6.2,7.3,8.4},
 	{9.5,10.1,11.8,12.7}};



	double [] highest = new int[number.length]; 
	double []  index1 = new int[number.length]; 

	for(int count = 0; count < number.length; count++){
		double max = number[count][0];
		int index = 0;

		for(int counter = 0; counter < number[count].length; counter++){
			if(number[count][counter] > max){
				max = number[count][counter];
				index = counter;
				
			}

			highest[count] = max;
			index1[count] = index ;
	}
	}
		System.out.print(Arrays.toString(highest));
		System.out.print(Arrays.toString(index1));	