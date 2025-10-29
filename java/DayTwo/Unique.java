
import java.util.Arrays;
public class Unique{
public static void main(String [] args){

int [] numbers = {1,2,3,1};

int [] newArray = new int[numbers.length];

	for(int count = 0; count < numbers.length; count++){
		if(numbers[count] == numbers[count]){
			continue;	
		}
		else{
		newArray[count] = numbers[count];
		}
		

			
	}
		System.out.print(Arrays.toString(newArray));

}

}
