#importy
#from IPython.display import clear_output
import random
print("Witaj w mojej grze chujku! Kółko i krzyżyk! \n\n")

# Set the game up here
#rysuje planszę
def display_board(board): 
    print (' {7} | {8} | {9} \n --------- \n {4} | {5} | {6}  \n --------- \n {1} | {2} | {3} '.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]))


#losuje kto gra pierwszy
def choose_first():
    random_num = random.randint(1,100)
    print ('Ten chujek gra pierwszy: ')
    if random_num%2 == 0:
        
        return 'Player1'
    else:
        return 'Player2'
    pass    

#Wybierz czym gra gracz
def player_input():
    znak = ""    
    print ("Czym grasz mistrzu?")
    while len(znak) == 0:
        wybor = input("Wpisz x lub o tutaj: ")
        if wybor.lower() == 'x':
            znak = wybor.upper()
            break
        elif wybor.lower()  == 'o':
            znak = wybor.upper()
            break
        else:
            print('\n Źle wpisałeś, śmieciu! Dawaj jeszcze raz!')
            continue
    return znak

#wstawia znak gracza na plansze
def place_marker(board, marker, position): 
    board[int(position)] = marker
    return board
    pass

#sprawdza czy gracz wygrał, sprawdza znaki
def win_check(board, mark):
    winlist = [mark,mark,mark]
    winline =(board[1:4],board[4:7],board[7:10],board[1:10:4],board[1:10:4],board[3:9:2],board[1:9:3],board[2:9:3],board[3:10:3])
    
    for pos in winline:
        if pos == winlist:
            return True
            break
       
    return False
    pass

#sprawdzam czy wybrane miejsce jest wolne
def space_check(board, position):
    if board[int(position)] == " ":
        return True
    else:
        return False

#sprawdzam czy plansza jest zapełniona
def full_board_check(board):
    if " " in board:
        return False
    else:
        return True
    pass

#wybór pola przez gracza
def player_choice(board):
    position = 0
    while position == 0:
        wybor = input("Wpisz pozycję gdzie chcesz ustawić znak, śmieciu: ")
        if space_check(board,int(wybor)):
            position = wybor
            return  position
            break
        else:
            print('\n To miejsce jest już zajęte cwelu! Dawaj jeszcze raz!')
            continue
            
#czy powtórzyć grę? 
def replay():
    print("Chcecie zagrać jeszcze raz Śmiecie?")
    l_powtorzen = 0
    wynik = 0
    while wynik == 0:
        wybor = input("Wpisz T jeśli tak, N jeśli nie:")
        if wybor.lower() == "t":
            return  True
            break
        if wybor.lower() == 'n' or l_powtorzen == 3:
            return  False
            break
        else:
            l_powtorzen += 1
            print('\n\n Wpisz T lub N, czego nie rozumiesz?!')
            continue

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#while True:
start = 0
while start == 0:
    game_on = 1
    #pass
    player1 = choose_first()
    if player1 == 'Player1':
        player2 = 'Player2'
    else:
        player2 = 'Player1'
    print(player1)
    marker = player_input()
    if marker == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    turn = 1
    
    #while game_on:
    while game_on == 1:
        
        
        
        
        #Player 1 Turn
        while turn == 1:
            display_board(board)
            print('Wybiera {}'.format(player1))
            position = player_choice(board)
            if space_check(board, position):
                board = place_marker(board, marker, position)
                turn = 2
                break
            else:
                continue
        # Player2's turn.
        while turn == 2:
            display_board(board)
            print('Wybiera {}'.format(player2))
            position = player_choice(board)
            if space_check(board, position):
                board = place_marker(board, marker2, position)
                turn = 1
                break
            else:
                continue
        #pass    
        
        if win_check(board, marker):
                wygrany = marker
                game_on = 0
                print("Wygral: "+marker)
        elif win_check(board, marker2):
            wygrany = marker2
            game_on = 0
            print("Wygral: "+marker)
        else: 
            print("Remis!")    
    
    #if not replay():
    #break
    if replay() != True:
        start = 1
        break
