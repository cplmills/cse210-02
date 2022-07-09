# Cycle
Cycle is an extension of the classic game "snake" that we all used to play on our cellphones. You play this game 
on a simulated terminal, with a textual interface.

## The Rules
* Collect food (@) to make your snake longer.
* Collect bonus gems (*) to make your opponent harder for them to see and make your snake easier to see.
* Collecting food whilst your visibility is low will give you new body parts that are easier to see, until another gem is collected by either player.
* Head to head impacts will result in a tie
* Run into another player and you will loose the game
* Run into yourself and you will loose the game.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the cycle folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycle               (source code for game)
  +-- game              (specific game classes)
    +-- casting         (contains classes representing actors in the game)
    +-- directing       (contains the director class, responsible for game flow)
    +-- scripting       (contains classes responsible for the main actions in the game)
    +-- services        (contains classes responsible for keyboard input, video output)
    +-- shared          (contains classes responsible for generating color elements and coordinates)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (contains variables that control game and screen settings)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* TODO: Chris Mills, admin@themillsclan.com
