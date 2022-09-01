board= {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ','low-L': ' ', 'low-M': ' ', 'low-R': ' '}
the_board={}
def tic_tac_toe():
        for i in range(10):
            if i%2==0:
                while(True):
                    move=input(" enter your move O ")
                    if move == "":
                        break
                    if move in the_board.keys():
                        continue
                    if move in board:
                        the_board.setdefault(move,"O")
                        break
            else:
                while(True):
                    move=input("enter your move X")
                    if move in the_board:
                        continue
                    if move in board:
                        the_board.setdefault(move,"X")
                        break
            display_board()
            if i >= 4: 
                if check_board():
                    break
            if move =="":
                break
        
def display_board():
        print(the_board.get('top-L'," ") + '|' + the_board.get('top-M'," ") + '|' + the_board.get('top-R'," "))
        print('-+-+-')
        print(the_board.get('mid-L'," ") + '|' + the_board.get('mid-M'," ") + '|' + the_board.get('mid-R'," "))
        print('-+-+-')
        print(the_board.get('low-L'," ") + '|' + the_board.get('low-M'," ") + '|' + the_board.get('low-R'," "))

def check_board():
    number_notation={'1': 'top-L', '2': 'top-M', '3': ' top-R', '4': 'mid-L', '5': 'mid-M', '6': 'mid-R','7': 'low-L', '8': 'low-M', '9': 'low-R'}
    for word in ["X","O"]:
        index=0
        for pos in board.keys():
            index+=1
            if index > 7:
                break
            if word == the_board.get(pos,"0"):
                    # print(index)
                    for i in [1,3,4]:
                            if the_board.get(number_notation[str(index)],"0")== the_board.get(number_notation.get(str(int(index)+i),"1"),"0") and the_board.get(number_notation[str(index)],"2")==the_board.get(number_notation.get(str(int(index)+i*2),"0"),"3"):
                                # print(the_board.get(number_notation[str(index)],"0"), the_board.get(number_notation.get(str(int(index)+i),"1"),"0"), the_board.get(number_notation.get(str(int(index)+i),"0"),"3"))
                                print( "player " + word + " won the game ")
                                return True
                            # print(" check ")