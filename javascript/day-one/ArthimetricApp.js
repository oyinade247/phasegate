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


		let highest = Math.max(numberOne, numberTwo);
		let lowest = Math.min(numberOne, numberTwo)	 		
 	 
	 	let answer = prompt("What is "+ highest +  " - " + lowest + " = ");
	 	
		
	 	if(highest - lowest == answer){
	  		console.log("You are right! ");
	   		countCorrectAnswer++;
	 	}

		else if(highest - lowest != answer){
			let answer = prompt("Enter the correct answer for the last time: " + highest + "-" +  lowest + ":");

			if(highest - lowest == answer){
		 		console.log("You are right! ");
				countCorrectAnswer++;
	
			}else{
				console.log("fish brain!");
				console.log("You are wrong! The correct answer should be"+ highest + "-" + lowest, " = "+ (highest - lowest));

			    }
             	
		}
	 
	  
		 
	 }
		//long endTime = System.currentTimeMillis();
	 
	  console.log("The total number of your score is " + countCorrectAnswer + "/" + numberOfQuestions);	
	 //let totalTime = countTime - endTime ;
	// console.log("The time in seconds spent is " + totalTime + "seconds");
	 

 


