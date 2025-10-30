import java.util.Arrays;

public class PerfectSquare{

 	public static void main(String [] args){
		int[] list =  {4, 9, 25, 49,6};

		System.out.print(Arrays.toString(getPerfectSquare(list)));
	}

	
	public static String[] getPerfectSquare(int [] list) {
        
 
       String[] results = new String[list.length];
	

        for (int count = 0; count < list.length; count++) {
            int number = list[count];
             	int divisor = 2;

                while(number % divisor != 0) {
                    	divisor++;

                }
		int dividedIndex = number / divisor;
		
               	if (number == dividedIndex * dividedIndex) {
                	results[count] = "true";
            	}else{
                	results[count] = "false";
            	}
		}
		
		return results;
	}
	
		
  


      
}











