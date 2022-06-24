# cse210-02

Name: Chris Mills
Email: admin@themillsclan.com

Title: Jumper Game
Description: The Jumper game is a game where the player needs to guess the letters of a secret word. 
Each time a letter is guessed incorrectly, the jumper looses some of his parachute.
If the jumper looses his chute and all his appendages, the game is over. If the player guesses the secret word correctly
the win the game.

Project Structure:
The project is seperated into 4 main classes with a __main__ program calling the neccessary classes into action.
Director Class:
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        player (Player): The Person playing the game
        isPlaying (boolean): Whether or not to keep playing.
        jumper (Jumper): The poor guy hanging from the parachute
        word (Word): controls the list of words and any actions taken on the word

    Methods:
        start_game(): Starts the game by running the main game loop.
            Args:
            self (Director): an instance of Director.
        
        get_inputs(self):
            Asks the player to make a guess.
                Args:
                self (Director): An instance of Director.
            
        _do_updates(self):
            Keeps watch on how many wrong guesses the player has made and updates the masked word.
            and checks if the word has been completed successfully
                Args:
                self (Director): An instance of Director.

        _do_outputs(self):
            prints the masked word to the terminal and the jumpers current state.
                Args:
                self (Director): An instance of Director.

Player class:
    The responsibility of a player is to guess letters, update the director when they are no longer playing.
    and check if they got a good guess or a bad guess.

    Attributes:
        isPlaying (boolean): Are you still playing the game?
        guessedLetter (string): The letter the player has guessed when last asked
        badGuesses (int): The number of guesses the player has made wrong

    Methods:
        getIsPlaying: returns the value of the isPlaying attribute
        setIsPlaying(boolean): sets the value of the isPlaying attribute
        guessLetter (string): Asks the player for a letter
        setBadGuesses (int): increments the number of guesses the player has made wrong
        getBadGuesses (int): Returns the number of wrong guesses the player has made

Word class:
    A word that the game has chosen to be guessed by the player. 
    
    The responsibility of a Word is to control access to the list of potential words and to perform operation on that chosen word.

    Attributes:
        availableWords (list): The list of available words to guess from
        currentWord (string): The current word to guess
        maskedWord (string): The hidden word with only the correctly guessed letters shown
        
    Methods:
        getWord (string): sets a new word to guess and sets the coresponding masked word
        checkLetter(string): checks if the provided letter is in the currently chosen word
        getWordLength: returns the length of the currently chosen word
        completeMask: updates the maskedWord attribute with the completed letters filled in
        isWordComplete: returns true if the word is completly guessed
        printWord: prints the masked word to the screen with a space between each character

Jumer Class:
    A poor soul dangling from a parachute. 
    
    The responsibility of the Jumper is to inform the player of its status.

    Attributes:
        _man (list): a list containing each line of the parachute man

    Methods:
        show_jumper(): Displays the jumper on the terminal window.

        showDeadMan(): if the jumper dies, this displays the jumper with an 'X' in place of his head and displays an end game message.

Required software
    requires the random class
