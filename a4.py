# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    def __init__(self):
       
        self.board = ["*"] * 9

    def __str__(self):
        
        row1 = " ".join(self.board[0:3])
        row2 = " ".join(self.board[3:6])
        row3 = " ".join(self.board[6:9])
        return row1 + "\n" + row2 + "\n" + row3

    def make_move(self, position, player_symbol):
        """Places a move for player_symbol ('X' or 'O') at position (1–9)."""
        
        if not isinstance(position, int) or position < 1 or position > 9:
            print("Invalid position! Choose a number between 1 and 9.")
            return False

        index = position - 1  
        if self.board[index] == "*":
            self.board[index] = player_symbol
            return True
        else:
            print("That spot is already taken! Choose another.")
            return False

    def has_won(self, player_symbol):
        """Checks if a player has won."""
        wins = [
            [0, 1, 2], 
            [3, 4, 5], 
            [6, 7, 8], 
            [0, 3, 6], 
            [1, 4, 7], 
            [2, 5, 8],  
            [0, 4, 8], 
            [2, 4, 6]              
        ]
        for combo in wins:
            if all(self.board[i] == player_symbol for i in combo):
                return True
        return False

    def is_full(self):
        """Checks if the board is full."""
        return "*" not in self.board
    def game_over(self):
        """Returns True if the game has been won or the board is full."""
        return self.has.won("x") or self.has_won("O") or self.is_full()


def play_tic_tac_toe():
    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0  

    print(brd)
    while True:
        move = input(f"Player {players[turn]}, what is your move (1–9)? ")

        try:
            move = int(move)
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        if brd.make_move(move, players[turn]):
            print(brd)
            if brd.has_won(players[turn]):
                print(f"Player {players[turn]} wins!")
                break
            elif brd.is_full():
                print("It's a draw!")
                break
            else:
                turn = 1 - turn  
        else:
            continue



brd = TTTBoard()
assert brd.make_move(1, "X") == True
assert brd.make_move(1, "O") == False
brd.make_move(2, "X")
brd.make_move(3, "X")
assert brd.has_won("X") == True
assert brd.has_won("O") == False
assert brd.make_move(10,"O") == False

full_brd = TTTBoard()
for i in range(1,10):
    full_brd.make_move(i, "x")
assert full_brd.is_full() == True
print("All tests passed!")
play_tic_tac_toe()
