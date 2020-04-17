Version 0.0.01:
    I have created a very simple version of a math problems game for my son to play. Pretty much right now it can only do addition unless I go in the code and hard code the game for subtraction. The game runs simply:

    1. Upon running the file two numbers are randomly generated. 
    2. Using these, the answer is also created to be used as a comparison.
    3. I create the math problem using the math_problem function.
    4. The function requires user input for the answer. If the answer is wrong, it tells the user to try again. If it is correct, the user is rewarded with a simple congratulatory statement. Thus ending the game requiring the user to once again start the function to play again. 


Future Updates:
1. I would like for this to be able to do simple subtraction also. This will be a bit more involved since right now I would need to make sure the highest number is always the first number used in the equation. I believe this could be solved somewhat simply by just comparing the numbers using the max() function and using that as the first variable.

2. Would like to create an option for the user to continue playing the game. Right now you are required to rerun the function from the command prompt in order to play again. It should be fairly straight forward to create a statement to reroll the numbers and generate a new question. 
    Steps needed for this:
        - The random numbers would likely need to be created inside of a function itself. This way, if the user agrees to play again, the function is called which would create a new number. 
        - Would need new logic for the math_problem function which might necessitate an additional function to break it up a bit.

3. Would like to keep track of the score on how many you got right vs how many you got wrong. With this, you could generate a grade. This would be a simple score of how many right vs how many you got wrong. This could be expanded in the future to maybe include a more accurate assessment perhaps. Could maybe use the datetime feature (or similar functionality to track the amount of time the user is playing also).

4. I would like to have some sort of a gui to display this outside of the command prompt perhaps? I am unsure how this could be implemented right now so this will require a good bit of research to see if its possible and how.
