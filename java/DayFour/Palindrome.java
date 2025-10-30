import java.util.Arrays;

public class Palindrome{

		public static void main(String [] arg){
	      		String[] list =  {" madam", "racecar", "hello", "noon"};

			System.out.print(Arrays.toString(isPalindrome(list)));
 		}

    public static boolean[] isPalindrome(String[] list){

        boolean[] newArray = new boolean[list.length];

        for (int count = 0; count < list.length; count++) {
            String word = list[count];
             	String reversed = "";

		for(int counter = word.length()-1; counter >= 0; counter--){
			reversed += word.charAt(counter);

		}
		if(reversed.equals(reversed)){
			newArray[count] = true;
			
		}else{
			newArray[count] = false;	
		}

		
		
	}
	return newArray;
			


}




}



