import java.util.Arrays;
public class Dimensional{
	public static void main(String [] args){

	double [][] numbers = {{1.5, 2.3, 3.7, 4.6},{5.1,6.2,7.3,8.4}, {9.5,10.1,11.8,12.7}};

	
	double[] highestRow = numbers[0];
	double index = 0;

	for (int rows = 1; rows < numbers.length; rows++) {
		for (int columns = 0; columns < rows; columns++){
			if(numbers[columns] < numbers[rows]){
				highestRow = numbers[rows];
			}
			
		}

 	}
		System.out.print(Arrays.toString(highestRow));

	
}
}






























