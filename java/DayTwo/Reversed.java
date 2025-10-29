
import java.util.Arrays;
public class Reversed{
	public static void main(String [] args){
	
	String word = "abcdefd";
	String ch = "d";

	String letters = "";

	
	for(int count = word.length() - 1; count >= 0 ; count--){
		letters += String.valueOf(word.charAt(count));
		if(!letters.equals(ch)){
			System.out.print(letters);
		}

	}

	if(!letters.equals(ch)){
		System.out.print(letters);
		}




	 	

	}

}




















