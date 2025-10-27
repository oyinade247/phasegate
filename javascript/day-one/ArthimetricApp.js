const prompt = require('prompt-sync')();


let numberOfQuestions = 10;
let countCorrectAnswer = 0; 
//let countTime = System.currentTimeMillis();

 let count = 0;
	 //int totalTime = 0;

	 while(count < numberOfQuestions){
	  	let numberOne = Math.floor(Math.random() * 12);
	  	let numberTwo = Math.floor(Math.random() * 12);
	   	count++;


	  let hold = numberOne;
	  numberOne = numberTwo;
	  numberTwo = hold;
 	 
	 	let answer = prompt("What is "+ numberOne +  " - " + numberTwo + "=");
	 	
		
	 	if(numberOne - numberTwo == answer){
	  		console.log("You are right! ");
	   		countCorrectAnswer++;
	 	}

		else if(numberOne - numberTwo != answer){
			let answer = prompt("Enter the correct answer for the last time: " + numberOne + "-" +  numberTwo + ":");

			if(numberOne - numberTwo == answer){
		 		console.log("You are right! ");
				countCorrectAnswer++;
	
			}else{
				console.log("fish brain!");
				console.log("You are wrong! The correct answer should be"+ numberOne + "-" + numberTwo, "="+ (numberOne - numberTwo));

			    }
             	
		}
	 
	  
		 
	 }
		//long endTime = System.currentTimeMillis();
	 
	  console.log("The total number of your score is " + countCorrectAnswer + "/" + numberOfQuestions);	
	 //let totalTime = countTime - endTime ;
	// console.log("The time in seconds spent is " + totalTime + "seconds");
	 

 


