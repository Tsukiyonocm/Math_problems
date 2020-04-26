## Version 0.0.03

I updated the code so that you no longer need to reload the file to do addition problems. I am unsure if its the best solution, but it works for the time being anyway. 

## Version 0.0.02

I created an updated version where it asks if you want to play or not. I also changed the name of the math function to addition_problem so that I can easier differentiate between various types of math in the future. Next I will be looking into allowing the problems to continue until the user decides to quit.


## Version 0.0.01:

I have created a very simple version of a math problems game for my son to play. Pretty much right now it can only do addition unless I go in the code and hard code the game for subtraction. The game runs simply:

1. Upon running the file two numbers are randomly generated. 
2. Using these, the answer is also created to be used as a comparison.
3. I create the math problem using the math_problem function.
4. The function requires user input for the answer. If the answer is wrong, it tells the user to try again. If it is correct, the user is rewarded with a simple congratulatory statement. Thus ending the game requiring the user to once again start the function to play again. 


### Function Explanation

1. start_game - The function starts by asking the player if they want to play. If yes, we pass the input value as an argument into the chosen_game function.

If the start variable is no, the game closes out with a simple message.

Lastly, if the player enters an option other than "yes" or "no", the game prompts the user to choose a valid response and asks the questions again. 


2. chosen_game - when the user picks "yes" as an option, that is passed to chosen_game in order to start. Here the user is asked if they would like to do "Subtraction or Addition" problems.

Regardless of choice, once the user makes a decision the game runs 3 more functions. The first is gen_ran_num which creates the problem variables, generate_answer which does as it says. Lastly, its runs the function of the problem of choice, either addition_problem or subtraction_problem, depending on your choice earlier.


3. gen_ran_num - This function generates a random number between 0 an 10 for the global variables, num_a and num_b.


4. generate_answer - this function generates the answer depending on whether its addition or subtraction. 

If addition, it sets the global variable answer to num_a + num_b.

If subtraction its a bit more complicated. We first have to figure out the largest number between num_a and num_b, then subtract the lowest number between num_a and num_b. This is then set to the global variable answer.


5. addition_problem - Using an f-string, the game prompts the user with the question: num_a + num_b = ?. Here the user inputs their answer to the question. If its correct, the game gives a congratulatory message and asks if you would like to play again. 

If yes at this point, it passes the start variable into the chosen_game function and we go back to choose another addition or subtraction problem.

If no, it thanks the user for playing and quits out of the game.

Lastly, if the user guessed wrong on the answer, the system says to please try again. Then it reposts the question to the command line asking the user to chose an answer.


6. subtraction_problem - Using an f-string, the game prompts the user with the question: max(num_a, num_b) - min(num_a, num_b) = ?. Here the user inputs their answer to the question. If its correct, the game gives a congratulatory message and asks if you would like to play again.

If yes at this point, it passes the start variable into the chosen_game function and we go back to choose another addition or subtraction problem.

If no, it thanks the user for playing and quits out of the game.

Lastly, if the user guessed wrong on the answer, the system says to please try again. Then it reposts the question to the command line asking the user to chose an answer.


### Future Updates:
1. I would like for this to be able to do simple subtraction also. This will be a bit more involved since right now I would need to make sure the highest number is always the first number used in the equation. I believe this could be solved somewhat simply by just comparing the numbers using the max() function and using that as the first variable.

~~2. Would like to create an option for the user to continue playing the game. Right now you are required to rerun the function from the command prompt in order to play again. It should be fairly straight forward to create a statement to reroll the numbers and generate a new question. 
    Steps needed for this:
        - The random numbers would likely need to be created inside of a function itself. This way, if the user agrees to play again, the function is called which would create a new number. 
        - Would need new logic for the math_problem function which might necessitate an additional function to break it up a bit.~~

3. Would like to keep track of the score on how many you got right vs how many you got wrong. With this, you could generate a grade. This would be a simple score of how many right vs how many you got wrong. This could be expanded in the future to maybe include a more accurate assessment perhaps. Could maybe use the datetime feature (or similar functionality to track the amount of time the user is playing also).

4. I would like to have some sort of a gui to display this outside of the command prompt perhaps? I am unsure how this could be implemented right now so this will require a good bit of research to see if its possible and how.
