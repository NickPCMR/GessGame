# Author: Nick Osborne
# Date: 5/26/2020
# Description: Gess game

import math

class GessGame:
    def __init__(self):
        """" initializes game: sets status, whose turn it is, and starting
        positions"""
        self.__dict__ = {
            "X": "WHITE",
            "O": "BLACK",
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19}
        self._status = 'UNFINISHED'
        self._turn = "O"
        self._board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ",  " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "X", " ", "X", " ", "X", "X", "X", "X",
                        "X", "X", "X", "X", " ", "X", " ", "X", " ", " "],
                       [" ", "X", "X", "X", " ", "X", " ", "X", "X", "X",
                        "X", " ", "X", " ", "X", " ", "X", "X", "X", " "],
                       [" ", " ", "X", " ", "X", " ", "X", "X", "X", "X",
                        "X", "X", "X", "X", " ", "X", " ", "X", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "X", " ", " ", "X", " ", " ", "X", " ",
                        " ", "X", " ", " ", "X", " ", " ", "X", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "O", " ", " ", "O", " ", " ", "O", " ",
                        " ", "O", " ", " ", "O", " ", " ", "O", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "O", " ", "O", " ", "O", "O", "O", "O",
                        "O", "O", "O", "O", " ", "O", " ", "O", " ", " "],
                       [" ", "O", "O", "O", " ", "O", " ", "O", "O", "O",
                        "O", " ", "O", " ", "O", " ", "O", "O", "O", " "],
                       [" ", " ", "O", " ", "O", " ", "O", "O", "O", "O",
                        "O", "O", "O", "O", " ", "O", " ", "O", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]


    def display(self):
        """func for printing board to screen"""
        for i in range(0, 20):
            for y in range(0, 20):
                if y ==19:
                    print(self._board[i][y])
                else:
                    print(" " + self._board[i][y] + " " + "|", end="")

    def set_board(self, board):
        self._board = board

    def get_game_state(self):
        """returns the current status of the game"""
        return self._status

    def set_game_state(self, state):
        """changes the current state of the game, options include UNFINISHED,
        BLACK_WON, WHITE_WON"""
        self._status = state

    def get_turn(self):
        return self._turn

    def set_turn(self):
        if self.get_turn() == "X":
            self._turn = "O"

        else:
            self._turn = "X"

    def resign_game(self, player):
        """allows a player to resign, calls set_game_state()"""
        pass

    def make_move(self, old_pos, new_pos):
        """ takes 2 coordinates as input and will make the move if it is
        legal"""


        # if the game is over return false
        if self.get_game_state() != "UNFINISHED":
            print("game is over")
            return False

        # if coordinate was invalid return False
        coordinates = self.translate_coordinates(old_pos,new_pos)
        if not coordinates:
            return False

        # if piece is invalid return false
        piece = self.get_piece(coordinates[0], coordinates[1])
        if not self.validate_piece(piece):
            return False

        # check if move is at a legal distance and slope
        dist = self.measure_distance(coordinates)
        if not dist:
            return False

        # check if piece has the necessary stones to move
        valid = self.legal_move(piece,coordinates, dist)
        if not valid:
            return False

        # returns a single x/y coordinate
        next_pos = self.get_next_pos(coordinates)

        # get coordinates for next piece and the next one
        old_coord = self.get_coordinates(coordinates[0],coordinates[1])
        next_coord = self.get_coordinates(next_pos[0],next_pos[1])

        # get a list of the new coordinates covered by move
        unique_coords = self.compare_coordinates(old_coord, next_coord)

        # check if those spaces contain characters
        new_stones = self.get_stones(unique_coords)

        for move in range(0, dist[0]):
            if self.contains_stones(new_stones):
                if coordinates[2] == next_pos[0] and coordinates[3] == next_pos[1]:
                    print("complete move")
                    board_copy = [stone[:] for stone in self._board]
                    self.move_piece(piece,next_coord)
                    self.clear_footprint(coordinates)
                    self.clear_perimeter()

                    if not self.check_win():
                        self.set_board(board_copy)
                        return False
                    self.set_turn()
                    return True

                else:
                    print("overlapping footprint")
                    return False
            else:
                if coordinates[2] == next_pos[0] and coordinates[3] == next_pos[1]:
                    print("complete move")
                    board_copy = [stone[:] for stone in self._board]
                    self.move_piece(piece,next_coord)
                    self.clear_footprint(coordinates)
                    self.clear_perimeter()

                    if not self.check_win():
                        self.set_board(board_copy)
                        return False
                    self.set_turn()
                    return True

                else:
                    next_pos.extend([coordinates[2],coordinates[3]])
                    next_pos = self.get_next_pos(next_pos)
                    old_coord = next_coord
                    next_coord = self.get_coordinates(next_pos[0],next_pos[1])
                    unique_coords = self.compare_coordinates(old_coord,next_coord)
                    new_stones = self.get_stones(unique_coords)

    def check_win(self, x=2, y=2,o_ring=False,x_ring=False):
        """check the board to see if both players have a ring"""




        piece = self.get_piece(x,y)

        x_count = 0
        o_count = 0
        for stone in piece:
            if stone == "X":
                x_count += 1
            if stone == "O":
                o_count += 1

        if x_count == 8 and piece[4] == " ":
            x_ring = True

        if o_count == 8 and piece[4] == " ":
            o_ring = True


        # base case, reach end of board or 2 rings are found


        if (x_ring is True and o_ring is True) or (x == 17 and y == 17):
            if x_ring is False and self.get_turn() == "X":
                print("can't break X ring")
                return False


            if o_ring is False and self.get_turn() == "O":
                print("can't break O ring")
                return False


            if x_ring is False and self.get_turn() == "O":
                self.set_game_state("BLACK_WON")
                print(self.get_game_state())
                return True


            if o_ring is False and self.get_turn() == "X":
                self.set_game_state("WHITE_WON")
                print(self.get_game_state())
                return True

            if x_ring is True and o_ring is True:
                return True

        if x == 17:
            x = 2
            y += 1
        else:
            x += 1

        return self.check_win(x,y,o_ring,x_ring)

    def clear_perimeter(self):
        """erases any pieces moved over the edge of the board"""
        for x in range(0,20):
            for y in range(0,20):
                if x == 0 or x == 19 or y == 0 or y == 19:
                    self._board[y][x] = " "



    def clear_footprint(self, coordinates):
        """sets old footprint to blank spaces unless they overlap with new
        position"""
        old = self.get_coordinates(coordinates[0],coordinates[1])
        new = self.get_coordinates(coordinates[2],coordinates[3])
        unique = self.compare_coordinates(new, old)

        for spot in unique:
            self._board[spot[1]][spot[0]] = " "


    def move_piece(self,piece, coordinates):
        """moves piece on the board"""

        for x in range(0,9):
            self._board[coordinates[x][1]][coordinates[x][0]] = piece[x]


    @staticmethod
    def contains_stones(char_list):
        """receives a list of charcters from the board and determines if they
        are blank or stones, returns T if blank, F otherwise"""
        char_count = 0
        for char in char_list:
            if char != " ":
                char_count += 1

        if char_count > 0:
            return True
        else:
            return False




    def get_stones(self,coordinates):
        """receives a list of coordinates and returns a list of the stones at
         those coordinates"""
        stones = []
        for spot in coordinates:
            stones.append(self._board[spot[1]][spot[0]])
        return stones


    @staticmethod
    def compare_coordinates(coord1, coord2):
        """ compare 2 pieces' coordinates and remove any coordinates that
        overlap"""
        new_coords = []
        for x in coord2:
            if x not in coord1:
                new_coords.append(x)

        return new_coords


    @staticmethod
    def get_coordinates(x, y):
        """gets the coordinates for the piece  surrounding the x/y coordinate
        provided"""

        piece_coordinates = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1],
                             [x - 1, y], [x, y], [x + 1, y], [x - 1, y + 1],
                             [x, y + 1], [x + 1, y + 1]]

        return piece_coordinates

    @staticmethod
    def get_next_pos(coordinates):
        """receives the x/y coordinates as a list and calculates the next
        space for the piece to move to in a line"""
        next_pos = []
        x1 = coordinates[0]
        x2 = coordinates[2]
        y1 = coordinates[1]
        y2 = coordinates[3]

        # NW move
        if x2 < x1 and y2 < y1:
            next_pos.append(x1-1)
            next_pos.append(y1-1)

        # N move
        if x2 == x1 and y2 < y1:
            next_pos.append(x1)
            next_pos.append(y1 - 1)

        # NE move
        if x2 > x1 and y2 < y1:
            next_pos.append(x1 + 1)
            next_pos.append(y1 - 1)

        # W move
        if x2 < x1 and y1 == y2:
            next_pos.append(x1 - 1)
            next_pos.append(y1)

        # E move
        if x2 > x1 and y1 == y2:
            next_pos.append(x1 + 1)
            next_pos.append(y1)

        # SW move
        if x2 < x1 and y2 > y1:
            next_pos.append(x1 - 1)
            next_pos.append(y1 + 1)

        # S move
        if x2 == x1 and y2 > y1:
            next_pos.append(x1)
            next_pos.append(y1 + 1)

        # SE move
        if x2 > x1 and y2 > y1:
            next_pos.append(x1 + 1)
            next_pos.append(y1 + 1)

        return next_pos


    @staticmethod
    def measure_distance(coordinates):
        """receives a list of coordinates and returns the distance between 2
        points. Returns False if coordiantes are the same or if move is not
        diagonal or straight"""
        x1 = coordinates[0]
        x2 = coordinates[2]
        y1 = coordinates[1]
        y2 = coordinates[3]

        if x1 == x2 and y2 == y1:
            print("can't move to current position")
            return False
        try:
            distance = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
            slope = abs((y2-y1)/(x2-x1))
        except ZeroDivisionError:
            slope = 0
        if slope == 1.0:
            distance = abs(x1-x2)

        if slope not in (1.0,0):
            print("impossible slope")
            return False

        return [distance, slope]

    @staticmethod
    def legal_move(piece, coordinates, distance):
        """ receives a piece,coordinates and distance as arguments,
        determines if a legal move can be made"""
        x1 = coordinates[0]
        x2 = coordinates[2]
        y1 = coordinates[1]
        y2 = coordinates[3]
        slope = distance[1]
        dist = distance[0]

        # cannot travel  more than 3 spaces without center piece
        if dist > 3 and piece[4] == " ":
            print("too far")
            return False

        # illegal NW move
        if piece[0] == " " and x2 < x1 and y2 < y1:
            print("no NW stone")
            return False

        # illegal N move
        if piece[1] == " " and x2 == x1 and y2 < y1:
            print("no N stone")
            return False

        # illegal NE move
        if piece[2] == " " and x2 > x1 and y2 < y1:
            print("no NE stone")
            return False

        # illegal W move
        if piece[3] == " " and x2 < x1 and y1 == y2:
            print("no W stone")
            return False

        # illegal E move
        if piece[5] == " " and x2 > x1 and y1 == y2:
            print("no E stone")
            return False

        # illegal SW move
        if piece[6] == " " and x2 < x1 and y2 > y1:
            print("no SE stone")
            return False

        # illegal S move
        if piece[7] == " " and x2 == x1 and y2 > y1:
            print("no S stone")
            return False

        # illegal SE move
        if piece[8] == " " and x2 > x1 and y2 > y1:
            print("no SE stone")
            return False


        return True

    def translate_coordinates(self, old, new):
        """takes 2 input strings as coordinates and converts them to list
        indices for the board, returns a list of integers as x and y
        coordinates;
        returns False if invalid input"""

        x1 = ""
        x2 = ""
        y1 = ""
        y2 = ""

        try:
            x1 = self.__dict__[old[0].lower()]
            y1 = 20 - int(old[1:])
            x2 = self.__dict__[new[0].lower()]
            y2 = 20 - int(new[1:])

        # if  a letter not in [a-t] or a special character is entered return
        # False
        except KeyError or ValueError:
            print("invalid coordinates")
            return False

        # if coordinates are not withing the 18x18 grid return False
        if y1 not in range(1,19) or y2 not in range(1,19) or x1 not in range(
                1,19) or x2 not in range(1,19):
            print("out of range")
            return False
        return [x1,y1,x2,y2]

    def get_piece(self, x, y):
        """accepts a list with an x and y coordinate, returns a list  of the
        surrounding piece values"""
        piece = []

        piece.append(self._board[y-1][x-1])     # NW
        piece.append(self._board[y-1][x])       # N
        piece.append(self._board[y-1][x+1])     # NE
        piece.append(self._board[y][x-1])       # W
        piece.append(self._board[y][x])         # C
        piece.append(self._board[y][x+1])       # E
        piece.append(self._board[y+1][x-1])     # SW
        piece.append(self._board[y+1][x])       # S
        piece.append(self._board[y+1][x+1])     # SE

        return piece


    def validate_piece(self, piece):
        """validates selected piece (list of strings).
                False Conditions:
                    all blanks
                    different characters (Xs and Os)
                    single char in center
        """
        x_count = 0
        o_count = 0
        blank_count = 0
        for char in piece:
            if char == 'X':
                x_count += 1
            if char == 'O':
                o_count += 1
            if char == ' ':
                blank_count += 1

        if x_count > 0 and o_count > 0:
            print("piece contains multiple players' pieces")
            return False
        if x_count == 0 and o_count == 0:
            print("blank piece")
            return False
        if piece[4] != ' ' and blank_count == 8:
            print("single center piece")
            return False

        if x_count > 0 and self.get_turn() == "O":
            print("Not your turn1")
            return False

        if o_count > 0 and self.get_turn() == "X":
            print("Not your turn2")
            return False

        return True

# g = Gess()
#
#
# g.make_move("l6", "l9")
# g.display()
# g.make_move("k14","n14")
# g.display()
# g.make_move("l9","l12")
# g.display()
# g.make_move("n14","o14")
# g.make_move("l12","l15")
# g.make_move("o14","p14")
# g.make_move("l15","l16")
# g.make_move("p15","q15")
#
#
# g.display()












