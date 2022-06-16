class Director:
    """ A person who directs the game.
    
    The responsibility of the Director is to control the flow of the game

    Attributes:
        is_playing (boolean): whether the game is currently playing
        score (int): the score for the current round of play
        total_score (int): the total score for the entire game
        current_guess (int): the current guess of higher (1) or Lower(0)
    """

    def __init__(self):
        """ Constructor. 
        Args: self (Director): an instance of Director.
        """

        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def start_game(self):
        """ starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to guess higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        highlow = int(input("Higher (1) or Lower (0)"))
        self.is_playing = (highlow == 1 or highlow == 0)
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        card.drawer()
        self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to go again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        
        card.show()

        print(f"Card is a: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)       