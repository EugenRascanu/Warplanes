# Warplanes

## Warplanes is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
### In my country, we would play the pen-and-paper game "Warplanes". Same game as "Battleship", but with planes. 

![Responsive Image](/images/Untitled.jpg)

## How to Play

In this version of the game, the objective is to shoot 5 warplanes out of the sky. When the player starts the app, he will be able to see the board, but not the warplane placement onto that board. 
The board is 8x8. Rows 1 to 8 and columns A to H. The player has 10 tries, before the game is over. 
## Features
  
 * Random generated planes onto the board with each new game
 * The player doesn't see where the planes are placed

![Start Image](/images/start.jpg)

 * Accepts user input
 * Hits are marked with "X" and miss with "-"

 ![Hit Image](/images/hit.jpg)
 
 
 ![Miss Image](/images/miss.jpg)

 * After each row and column input, the player is reminded of how many turns he has left
 * You cannot enter a value outside the grid

 ![Valid Row](images/validrow.jpg)

 
 ![Valid Col](images/validcol.jpg)

 * If you repeat the same input, you will not get punished for it, thus you will not loose a turn

 ![Same Input](images/already.jpg)

 * If the 5 warplanes haven't been shot out of the sky within the 10 turns, the game is over

 ![Game Over](images/nomore.jpg)

 
 ## Testing

 * The code has been passed through PEP8 - results found: "All right"
 * The app has been tested localy and on the Heroku terminal

 ## Bugs

 *