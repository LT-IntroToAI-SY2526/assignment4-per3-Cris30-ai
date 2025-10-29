# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
    The most difficult part of the aissgnment was figruginh out the different positions and the wining combinations. I was a little confused that in python, the computer starts at zero not one. But once I figured this out I was able to do (index = position - 1), which gives same position on the board that users would assume. 


2. Explain how you would add a computer player to the game.
    I would add a computer player to the game by creating a function that gives the computer the ability to chose its own moves on the board. I wouldn't have to change any of the class and objects I created already because those are the essetinally rules of the game. Therefore, ever time I want the computer to play against me I will call upon the function. 

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
    I would make the computer play pick the best move every time by programming it to pick positions like the center or corner first, which is essentially from my experience the best position to set up a win. But a more technically response, would be that I can program it to check all possible winning combination and to decide if the opponent is about to win or if they are about to win. Also, I could programm it to stragetically place positons to block the opponent from winning.  
