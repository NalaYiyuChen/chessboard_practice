"""chess notation works, but come back to better implement it later. You are breaking a lot of abstraction barriers."""

#Copied over from working bishop.py, 7/09/19. Should I make a github.... :p 

board = [['_' for i in range(8)] for i in range(8)]

select_column = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
select_row = {'1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0}

move_column = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
move_row = {7:'1', 6:'2', 5:'3', 4:'4', 3:'5', 2:'6', 1:'7', 0:'8'} 

    # def play(self): 
    #     turn = 0
    #     while not self.game_over: 
    #         self.display()
    #         if turn == 0: 
    #             move_from = input("White to move. Where is the piece you want to move?")
    #         elif turn ==1: 
    #             move_from = input("Black to move. Where is the piece you want to move?")
    #         try: 
    #             column = select_column[move_from[0]]
    #             row = select_row[move_from[1]]
    #             pieceToMove = board[row][column]
    #             assert (pieceToMove.can_move == turn)
    #         except: 
    #             print("This piece is the wrong color. Please select a valid piece to move.")
    #             continue
    #         print(self.show_moves(move_from))
    #         move_to = input("Where will this piece move?")
    #         try: 
    #             self.add_piece(move_to, move_from)
    #         except: 
    #             print("Invalid move. Please enter your input again.")
    #             continue
    #         turn = (turn+1)%2

    # def play(self): 
    #     turn = 0
    #     while not self.game_over: 
    #         self.display()
    #         if turn == 0: 
    #             move = input("White to move. Please select a piece to move.")
    #         else: 
    #             move = input("Black to move. Please select a piece to move.")
    #         move_info = chess_notation(move)
    #         move_piece = move_info[2]
    #         move_to_column = select_column[move_info[0]]
    #         move_to_row = select_row[move_info[1]]
    #         original_square = board[move_to_row][move_to_column]
    #         if (move_piece == "K"): 
    #             new_piece = King(turn, 'K', move_to)
    #         else if (move_piece == "Q"): 
    #             new_piece = Queen(turn, 'Q', move_to)
    #         else if (move_piece == "N"): 
    #             new_piece = Knight(turn, 'N', move_to)
    #         else if (move_piece == "B"):
    #             new_piece = Bishop(turn, 'B', move_to)
    #         else if (move_piece == "R"): 
    #             new_piece = Rook(turn, 'R', move_to)
    #         else if (move_piece == "p"):
    #             new_piece = Pawn(turn, 'p', move_to)
    #         board[move_to[1]][move_to[0]] = new_piece
    #         legal_spots = new_piece.move_piece(move)
    #         move_from = "k9"
    #         for spot in legal_spots: 
    #             spot_info = chess_notation(spot)
    #             spot_row = select_row[spot_info[1]]
    #             spot_column = select_column[spot_info[0]]
    #             try_square = board[spot_row][spot_column]
    #             if (try_square != "_"): 
    #                 if ((try_square.color == new_piece.color) and (try_square.type_of_piece == new_piece.type_of_piece)): 
    #                     move_from = move
    #         try: 
    #             self.add_piece(move_to, move_from)
    #         except: 
    #             print("Invalid move. Please enter your input again.")
    #             continue
    #         turn = (turn+1)%2


    # def play(self): 
    #     turn = 0
    #     while not self.game_over: 
    #         self.display()
    #         if turn == 0: 
    #             move_from = input("White to move. Where is the piece you want to move?")
    #         elif turn ==1: 
    #             move_from = input("Black to move. Where is the piece you want to move?")
    #         if (move_from == "castle"): 
    #             if turn == 0: 
    #                 king_place = "e1"
    #             elif turn == 1: 
    #                 king_place = "e8"
    #             king_to_castle = board[select_row[king_place[1]]][select_column[king_place[0]]]
    #             rook_place = input("Where is the rook you'd like to move?")
    #             rook_to_castle = board[select_row[rook_place[1]]][select_column[rook_place[0]]]
    #             try: 
    #                 if (!isinstance(rook_to_castle, King) or king_to_castle.has_moved == True): 
    #                     raise AssertionError("You have moved your king. You cannot castle. Please try again.")
    #                 if (!isinstance(rook_to_castle, Rook) or rook_to_castle.has_moved == True):
    #                     raise AssertionError("You have moved your rook. You cannot castle in this direction. Please try again.")
    #             except: 
    #                 continue
    #         try: 
    #             column = select_column[move_from[0]]
    #             row = select_row[move_from[1]]
    #             pieceToMove = board[row][column]
    #             assert (pieceToMove.can_move == turn)
    #         except: 
    #             print("Please select a valid piece to move.")
    #             continue
    #         print(self.show_moves(move_from))
    #         move_to = input("Where will this piece move?")
    #         try: 
    #             self.add_piece(move_to, move_from)
    #         except: 
    #             print("Invalid move. Please enter your input again.")
    #             continue
    #         turn = (turn+1)%2

class Piece(object):
    def __init__(self, color, type_of_piece, place):
        self.type_of_piece = type_of_piece
        self.place = place
        target_column = select_column[place[0]]
        target_row = select_row[place[1]]
        board[target_row][target_column] = self
        if color: 
            self.color = 'black'
        elif color == 0: 
            self.color = 'white'
        self.can_move = color
        
    def __repr__(self):
        return str(self.can_move) + str(self.type_of_piece) + " "

    def chess_notation(self, place): 
        if place[0] in ["N", "K", "Q", "B", "R"]: 
            column = place[1]
            row = place[2]
            name = place[0]
            return [column, row, name, place[1:]]
        elif place[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']: 
            column = place[0]
            row = place[1]
            name = "p"
            return [column, row, name, place]

    def show_moves(self, move_from): 
        old_column = select_column[move_from[0]]
        old_row = select_row[move_from[1]]
        piece_to_move = board[old_row][old_column]
        return piece_to_move.move_piece(move_from)

    def add_piece(self, move_to, move_from):
        new_column = select_column[move_to[0]]
        new_row = select_row[move_to[1]]
        old_column = select_column[move_from[0]]
        old_row = select_row[move_from[1]]
        if board[new_row][new_column] != '_': 
            print("Congratulations! You have captured a piece.")
        piece_to_move = board[old_row][old_column]
        available_moves = piece_to_move.move_piece(move_from)
        if move_to not in available_moves: 
            raise AssertionError("Invalid move, please try again.")
        board[new_row][new_column] = piece_to_move
        if isinstance(piece_to_move, Pawn):
            piece_to_move.has_moved = True
        elif isinstance(piece_to_move, Rook):
            piece_to_move.has_moved = True
        elif isinstance(piece_to_move, King): 
            piece_to_move.has_moved = True
        piece_to_move.place = move_to
        self.remove_piece(move_from)

    def castle(self, king_move_to, rook_move_to, king_move_from, rook_move_from):
        king_new_column = select_column[king_move_to[0]]
        king_old_column = select_column["e"]
        king_new_row = select_row[king_move_to[1]]
        rook_new_column = select_column[rook_move_to[0]]
        rook_old_column = select_column[rook_move_from[0]]
        rook_new_row = select_row[rook_move_to[1]]
        print("we're here")
        king_to_move = board[king_new_row][king_old_column]
        rook_to_move = board[rook_new_row][rook_old_column]
        print(king_to_move)
        board[king_new_row][king_new_column] = king_to_move
        board[rook_new_row][rook_new_column] = rook_to_move
        king_to_move.place = king_move_to
        rook_to_move.place = rook_move_to
        print("anyone home")
        self.remove_piece(king_move_from)
        self.remove_piece(rook_move_from)

    def remove_piece(self, place):
        target_column = select_column[place[0]]
        target_row = select_row[place[1]]
        board[target_row][target_column] = '_'

class King(Piece):
    """A King."""
    def __init__(self, color, type_of_piece, place): 
        Piece.__init__(self, color, 'K', place)
        self.has_moved = False

    def move_piece(self, place):
        old_column = place[0]
        old_row = place[1]
        old_column = select_column[old_column]
        old_row = select_row[old_row]
        move_left = [old_column - 1, old_row]
        move_right = [old_column + 1, old_row]
        move_up = [old_column, old_row + 1]
        move_down = [old_column, old_row - 1]
        move_right_up = [old_column + 1, old_row + 1]
        move_right_down = [old_column + 1, old_row -1]
        move_left_up = [old_column -1, old_row + 1]
        move_left_down = [old_column - 1, old_row - 1]
        try_moves = [move_left, move_right, move_up, move_down, move_right_up, move_right_down, move_left_up, move_left_down]
        legal_moves = [moves for moves in try_moves  if ((moves[0] >= 0) and (moves[1] >= 0) and (moves[0] < 8) and (moves[1] <8))]
        legal_moves = [(move_column[moves[0]] + move_row[moves[1]]) for moves in legal_moves]
        return legal_moves
        
class Queen(Piece):
    def __init__(self, color, type_of_piece, place):
        """Create a Queen."""
        Piece.__init__(self, color, 'Q', place)

    def move_piece(self, place): 
        old_column = place[0]
        old_row = place[1]
        old_column = select_column[old_column]
        old_row = select_row[old_row]
        right_up = []
        left_down = []
        right_down = []
        left_up = []
        for i in range(8): 
            left_down.append([old_column - i, old_row - i]) 
            left_up.append([old_column + i, old_row - i])
            right_up.append([old_column + i, old_row + i])
            right_down.append([old_column - i, old_row + i])
        try_moves = right_up + left_up + left_down + right_down
        legal_moves = [moves for moves in try_moves if ((moves != [old_column, old_row]) and (moves[0] >= 0) and (moves[1] >= 0) and (moves[0] < 8) and (moves[1] <8))]
        legal_diagonal_moves = [(move_column[moves[0]] + move_row[moves[1]]) for moves in legal_moves]
        old_board_column = place[0]
        old_board_row = place[1]
        old_column = select_column[old_board_column]
        old_row = select_row[old_board_row]
        horizontal_moves = []
        vertical_moves = []
        for i in range(8): 
            vertical_moves.append([i, old_column]) 
        for i in range(8): 
            horizontal_moves.append([old_row, i]) 
        try_moves = vertical_moves + horizontal_moves
        legal_moves = [moves for moves in try_moves if (moves != [old_row, old_column])]
        legal_vertical_moves = [(move_column[moves[1]] + move_row[moves[0]]) for moves in legal_moves]
        legal_moves = legal_vertical_moves + legal_diagonal_moves
        return legal_moves
    

class Bishop(Piece):
    def __init__(self, color, type_of_piece, place):
        """Create a Bishop."""
        Piece.__init__(self, color, 'B', place)

    def move_piece(self, place): 
        old_column = place[0]
        old_row = place[1]
        old_column = select_column[old_column]
        old_row = select_row[old_row]
        right_up = []
        left_down = []
        right_down = []
        left_up = []
        for i in range(8): 
            left_down.append([old_column - i, old_row - i]) 
            left_up.append([old_column + i, old_row - i])
            right_up.append([old_column + i, old_row + i])
            right_down.append([old_column - i, old_row + i])
        try_moves = right_up + left_up + left_down + right_down
        legal_moves = [moves for moves in try_moves if ((moves != [old_column, old_row]) and (moves[0] >= 0) and (moves[1] >= 0) and (moves[0] < 8) and (moves[1] <8))]
        legal_moves = [(move_column[moves[0]] + move_row[moves[1]]) for moves in legal_moves]
        return legal_moves

class Knight(Piece):
    def __init__(self, color, type_of_piece, place):
        """Create a Knight."""
        Piece.__init__(self, color, 'N', place)

    def move_piece(self, place): 
        old_column = place[0]
        old_row = place[1]
        old_column = select_column[old_column]
        old_row = select_row[old_row]
        one_right = old_column + 1
        two_right = old_column + 2
        one_left = old_column - 1
        two_left = old_column -2 
        one_up = old_row + 1
        two_up = old_row + 2
        one_down = old_row - 1
        two_down = old_row - 2
        move_one = [one_right, two_up]
        move_two = [one_left, two_up]
        move_three = [one_right, two_down]
        move_four = [one_left, two_down]
        move_five = [two_right, one_up]
        move_six = [two_right, one_down]
        move_seven = [two_left, one_up]
        move_eight = [two_left, one_down]
        try_moves = [move_one, move_two, move_three, move_four, move_five, move_six, move_seven, move_eight]
        legal_moves = [moves for moves in try_moves  if ((moves[0] >= 0) and (moves[1] >= 0) and (moves[0] < 8) and (moves[1] <8))]
        legal_moves = [(move_column[moves[0]] + move_row[moves[1]]) for moves in legal_moves]
        return legal_moves

class Rook(Piece):
    def __init__(self, color, type_of_piece, place):
        """Create a Rook."""
        Piece.__init__(self, color, 'R', place)
        self.has_moved = False

    def move_piece(self, place): 
        old_board_column = place[0]
        old_board_row = place[1]
        old_column = select_column[old_board_column]
        old_row = select_row[old_board_row]
        horizontal_moves = []
        vertical_moves = []
        for i in range(8): 
            vertical_moves.append([i, old_column]) 
        for i in range(8): 
            horizontal_moves.append([old_row, i]) 
        try_moves = vertical_moves + horizontal_moves
        legal_moves = [moves for moves in try_moves if (moves != [old_row, old_column])]
        legal_moves = [(move_column[moves[1]] + move_row[moves[0]]) for moves in legal_moves]
        return legal_moves

class Pawn(Piece):
    def __init__(self, color, type_of_piece, place):
        """Create a Pawn."""
        Piece.__init__(self, color, 'p', place)
        self.has_moved = False
        self.can_be_

    def move_piece(self, place):
        old_board_column = place[0]
        old_board_row = place[1]
        old_column = select_column[old_board_column]
        old_row = select_row[old_board_row]
        if self.color == 'white':
            move_forward = -1
        elif self.color == 'black':
            move_forward = 1
        move_two_forward, move_one_forward, capture_right, capture_left = [-1,-1], [-1,-1], [-1,-1], [-1,-1]
        two_spaces_up = [old_row + move_forward + move_forward, old_column]
        one_space_up = [old_row + move_forward, old_column]
        if self.has_moved == False:
            if board[two_spaces_up[0]][two_spaces_up[1]] == '_':
                move_two_forward = two_spaces_up
        if board[one_space_up[0]][one_space_up[1]] == '_':
            move_one_forward =  one_space_up
        if old_board_column != "h":
            right_up = [old_row + move_forward, old_column + 1]
            if board[right_up[0]][right_up[1]] != '_':
                capture_right = right_up
        if old_board_column != "a":
            left_up = [old_row + move_forward, old_column - 1]
            if board[left_up[0]][left_up[1]] != '_':
                capture_left = left_up
        try_moves = [move_two_forward, move_one_forward, capture_right, capture_left]
        legal_moves = [moves for moves in try_moves  if ((moves[0] >= 0) and (moves[1] >= 0) and (moves[0] < 8) and (moves[1] <8))]
        legal_moves = [(move_column[moves[1]] + move_row[moves[0]]) for moves in legal_moves]
        return legal_moves

dict_of_pieces = {'K': King, 'Q': Queen, 'B': Bishop, "N": Knight, "R": Rook, "p":Pawn}

class Set_Board(Piece):
    game_over = False
    def __init__(self):
        Pawn(0, 'p', 'a2')        
        Pawn(0, 'p', 'b2')        
        Pawn(0, 'p', 'c2')        
        Pawn(0, 'p', 'd2')        
        Pawn(0, 'p', 'e2')        
        Pawn(0, 'p', 'f2')        
        Pawn(0, 'p', 'g2')        
        Pawn(0, 'p', 'h2')        
        Pawn(1, 'p', 'a7')        
        Pawn(1, 'p', 'b7')        
        Pawn(1, 'p', 'c7')        
        Pawn(1, 'p', 'd7')        
        Pawn(1, 'p', 'e7')        
        Pawn(1, 'p', 'f7')        
        Pawn(1, 'p', 'g7')        
        Pawn(1, 'p', 'h7')        
        Rook(0, 'R', 'a1')     
        Rook(0, 'R', 'h1')     
        Rook(1, 'R', 'a8')     
        Rook(1, 'R', 'h8')
        Knight(0, 'N', 'g1')
        Knight(0, 'N', 'b1')
        Knight(1, 'N', 'b8')
        Knight(1, 'N', 'g8')
        Bishop(0, 'B', 'f1')
        Bishop(0, 'B', 'c1')
        Bishop(1, 'B', 'c8')
        Bishop(1, 'B', 'f8')
        Queen(0, 'Q', 'd1')
        Queen(1, 'Q', 'd8')
        King(0, 'K', 'e1')
        King(1, 'K', 'e8')     

    def display(self):
        for i in range(8):
            print(board[i])     

    def play(self): 
        turn = 0
        while not self.game_over: 
            self.display()
            if turn == 0: 
                move_from = input("White to move. Where is the piece you want to move?")
                king_place = "e1"
            elif turn == 1: 
                move_from = input("Black to move. Where is the piece you want to move?")
                king_place = "e8"
            if (move_from == "castle"): 
                king_to_castle = board[select_row[king_place[1]]][select_column[king_place[0]]]
                rook_place = input("Where is the rook you'd like to move?")
                rook_to_castle = board[select_row[rook_place[1]]][select_column[rook_place[0]]]
                try: 
                    if ((not isinstance(king_to_castle, King)) or (king_to_castle.has_moved == True)): 
                        raise AssertionError("You have moved your king. You cannot castle. Please try again.")
                    if ((not isinstance(rook_to_castle, Rook)) or (rook_to_castle.has_moved == True)):
                        raise AssertionError("You have moved your rook. You cannot castle in this direction. Please try again.")
                    if (rook_to_castle.can_move != turn):
                        raise AssertionError("You cannot castle with your opponent's rook.")
                except: 
                    continue
                king_row = king_place[1]
                if (rook_place[0] == "a"): 
                    knight_place = board[select_row[king_row]][select_column["b"]]
                    bishop_place = board[select_row[king_row]][select_column["c"]]
                    queen_place = board[select_row[king_row]][select_column["d"]]
                    if ((knight_place == "_") and (bishop_place == "_") and (queen_place == "_")):
                        try: 
                            print("Trying to castle")
                            self.castle("c" + king_row, "d" + king_row, king_place, rook_place)
                            print("Castled")
                            turn = (turn + 1) % 2
                            continue
                        except: 
                            print("something went wrong.")
                            continue
                    else: 
                        print("There is at least one piece in the way. You cannot castle.")
                elif (rook_place[0] == "h"): 
                    knight_place = board[select_row[king_row]][select_column["g"]]
                    bishop_place = board[select_row[king_row]][select_column["f"]]
                    if ((knight_place == "_") and (bishop_place == "_")):
                        try: 
                            print("Trying to castle")
                            self.castle("g" + king_row, "f" + king_row, king_place, rook_place)
                            print("Castled")
                            turn = (turn + 1) % 2
                            continue
                        except: 
                            print("something went wrong.")
                            continue
                    else: 
                        print("There is at least one piece in the way. You cannot castle.")
                continue
            try: 
                column = select_column[move_from[0]]
                row = select_row[move_from[1]]
                pieceToMove = board[row][column]
                assert (pieceToMove.can_move == turn)
            except: 
                print("This piece is the wrong color. Please select a valid piece to move.")
                continue
            print(self.show_moves(move_from))
            move_to = input("Where will this piece move?")
            try: 
                self.add_piece(move_to, move_from)
                if turn == 0: 
                    last_white_move = piece
                else: 
                    last_black_move = piece
            except: 
                print("Invalid move. Please enter your input again.")
                continue
            turn = (turn+1)%2

start_game = Set_Board()
start_game.play()