# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self):
        self.board: ["*"] * 9

    def __str__(self):
        row1 = " ".join(self.board[0:3])
        row2 = " ".join(self.board[3:6])
        row3 = " ".join(self.board[6:9])
        return row1 + "\n" + row2 + "\n" + row3
    
    def make_move(self, position, player_symbol):
        index = position - 1
        if self.board[index] == "*":
            self.board[index] = player_symbol
        else:
            print("That spot is already taken! Choose another.")
    
    def has_won(self, player: str) -> bool:
        """Returns Ture if the given player has won, False otherwise"""
        winning_combos = [
            [0, 1, 2], #top row
            [3, 4, 5], # middle row
            [6, 7, 8], # bottom row
            [0, 3, 6], # left column
            [1, 4, 7], # middle column
            [2, 5, 8], #right column
            [0, 4, 8], #diagonal top-left to bottom-right
            [2, 4, 6], #diagonal top-right to bottom-left
        ]
        for combos in winning_combos:
            if all(self.board[i] == player for i in combos):
                return True
        return False
    
    def game_over(self) -> bool:
        """Return True if someone has won or the board is full, False otherwis."""
        if self.has_won("X") or self.has_won("O"):
            return True
        if "*" not in self.board:
            return True
        return False
    def clear(self) -> None:
        """Reset the board to start a new game."""
        self.board = ["*"] * 9



        

def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    
    #Board set-up
    assert brd.board == ["x"] * 9, "Initial board not set up correctly"
    assert brd.game_over() == False, "Game should start not be over"

    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
     play_tic_tac_toe()
