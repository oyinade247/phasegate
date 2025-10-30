function elementIsPalindrome(my_list){

let new_list = []
	for(let count = 0; count < my_list.length; count++){
		
			let palindrome = ""
		for (let counter = 0; counter < my_list[count].length; counter++){
			palindrome = my_list[count].charAt(counter) + palindrome
		}

		if (my_list[count] == palindrome){
		new_list[count] = true;
		}
		else{
		new_list[count] = false;
		}

	}
	return new_list


}

