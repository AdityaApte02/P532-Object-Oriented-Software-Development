from acquire.tile import Tile
from acquire.hotel import Hotel

class Board:
    def __init__(self):
        self.tiles = []
        self.hotels = []

    def create_board(self):
        board = [['0' for _ in range(12)] for _ in range(9)]
        # Place tiles and hotels on the board
        for tile in self.tiles:
            row = ord(tile["row"]) - 65
            col = int(tile["column"]) - 1
            board[row][col] = "1"

        for hotel in self.hotels:
            for tile in hotel["tiles"]:
                row = ord(tile["row"]) - 65
                col = int(tile["column"]) - 1
                board[row][col] = hotel['hotel']
        
        for hotel in self.hotels:
            hotel_label = hotel['hotel']
            for tile in hotel['tiles']:
                row = ord(tile["row"]) - 65
                col = int(tile["column"]) - 1
                if (row-1 >=0 and (board[row-1][col] != hotel_label and board[row-1][col] != '0' and board[row-1][col] != '1')) :
                    raise Exception("Invalid hotel placement")
                elif (row+1 < 9 and (board[row+1][col] != hotel_label and board[row+1][col] != '0' and board[row+1][col] != '1')) :
                    raise Exception("Invalid hotel placement")
                elif  (col-1 >=0 and (board[row][col-1] != hotel_label and board[row][col-1] != '0' and board[row][col-1] != '1')) :
                    raise Exception("Invalid hotel placement")
                elif (col+1 < 12 and (board[row][col+1] != hotel_label and board[row][col+1] != '0' and board[row][col+1] != '1')):
                    raise Exception("Invalid hotel placement")
                else:
                    board[row][col] = hotel_label
            
        # todo: validate adjacent 1s
        return board
    
    def place_tile(self, row, column):
        pass

    def print_board(self, board):
        print("\n")
        for row in board:
            print(row)
        print("\n")