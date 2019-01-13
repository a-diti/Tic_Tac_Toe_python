import random
def display_board(board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

def play_input():
        marker = ''
        while not(marker=='X' or marker=='O'):
                marker = input('Do you want to be X or O: ').upper()
                if marker=='X':
                        return ('X','O')
                else:
                        return ('O','X')

def place_marker(board,position,marker):
        board[position] = marker

def win_check(board,mark):
        return ((board[7]==mark and board[8]==mark and board[9]==mark) or 
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[3]==mark and board[2]==mark and board[1]==mark)or
        (board[7]==mark and board[4]==mark and board[1]==mark)or
        (board[8]==mark and board[5]==mark and board[2]==mark)or
        (board[9]==mark and board[6]==mark and board[3]==mark)or
        (board[7]==mark and board[5]==mark and board[3]==mark)or
        (board[9]==mark and board[5]==mark and board[1]==mark))

def choose_player():
        if random.randint(0,1) == 0:
                return 'Player 1'
        else:
                return 'Player 2'

def space_check(board,position):
        return board[position] == ' '

def check_board_full(board):
        for i in range(1,10):
                if space_check(board,i):
                        return False
        return True

def player_choice(board):
        position = ' '
        while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
                position = input('Enter your next position from 1-9: ')
        return int(position)
         
def again_play():
        return input('Do you want to play again (Y/N):').upper().startswith('Y')
        
print('Welcome to Tic Toe Game')
while True:
        play_board = [' ']*10
        player1_marker,player2_marker = play_input()
        turn = choose_player()
        print(turn +" will play first \n");
        game_on = True
        while game_on:
                if turn == 'Player 1':
                        display_board(play_board)
                        print('Player 1')
                        position = player_choice(play_board)
                        place_marker(play_board,position,player1_marker)
                        if win_check(play_board,player1_marker):
                                display_board(play_board)
                                print('Congratulations Player 1, you won!')
                                game_on = False
                        elif check_board_full(play_board):
                                display_board(play_board)
                                print('The game is a draw')
                                game_on = False
                        else:
                                turn = 'Player 2'
                else:
                        display_board(play_board)
                        print('Player 2')
                        position = player_choice(play_board)
                        place_marker(play_board,position,player2_marker)
                        if win_check(play_board,player2_marker):
                                display_board(play_board)
                                print('Congratulations Player 2, You Won!')
                                game_on = False
                        elif check_board_full(play_board):
                                display_board(play_board)
                                print('The game is Draw!')
                                game_on = False
                        else:
                                turn = 'Player 1'
        if not again_play():
                print('Thanks for playing!')
                break
                        
        
