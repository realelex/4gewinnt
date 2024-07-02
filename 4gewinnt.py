import tabulate


gameboard = [
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ]

players = ["player1", "player2"]

header = ["1", "2", "3", "4", "5", "6", "7"]

def play(player):
    valid = False 
    while not valid:
        column = int(input(f"{player} what column do you want to play? ")) - 1
        if player == players[0]:
            try:
                col = [row[column] for row in gameboard]
            except Exception as e:
                print(e, "invalid move")
            c = 0
            try:
                for item in col:
                    if c == 0 and item != "":
                        raise Exception("invalid move")
                    if item == "" and c != 6:
                        c += 1
                    if item != "" or c == 6:
                        gameboard[c-1][column] = "X"
                        print(tabulate.tabulate(gameboard, headers=header, tablefmt="grid"))
                        valid = True
                        return gameboard, column, c-1
            except Exception as e:
                print(e, "invalid move")
                
    
        if player == players[1]:
            try:
                col = [row[column] for row in gameboard]
            except Exception as e:
                print(e, "invalid move")
            c = 0
            try:
                for item in col:
                    if c == 0 and item != "":
                        raise Exception("invalid move")
                    if item == "" and c != 6:
                        c += 1
                    if item != "" or c == 6:
                        gameboard[c-1][column] = "O"
                        print(tabulate.tabulate(gameboard, headers=header, tablefmt="grid"))
                        valid = True
                        return gameboard, column, c-1
            except Exception as e:
                print(e, "invalid move")
               
def wincondition(posx, posy):
    #check horizontal
    try:
        if gameboard[posy][posx] == gameboard[posy][posx - 1] == gameboard[posy][posx - 2] == gameboard[posy][posx - 3]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy][posx - 1] == gameboard[posy][posx - 2] == gameboard[posy][posx + 1]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy][posx - 1] == gameboard[posy][posx + 1] == gameboard[posy][posx + 2]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy][posx + 1] == gameboard[posy][posx + 2] == gameboard[posy][posx + 3]:
            return True
    except IndexError:
        pass 
    
    #check vertical
    try:
        if gameboard[posy][posx] == gameboard[posy + 1][posx] == gameboard[posy + 2][posx] == gameboard[posy + 3][posx]:
            return True
    except IndexError:
        pass
    
    #check positive diagonal
    try:
        if gameboard[posy][posx] == gameboard[posy - 1][posx + 1] == gameboard[posy - 2][posx + 2] == gameboard[posy - 3][posx + 3]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy - 1][posx + 1] == gameboard[posy - 2][posx + 2] == gameboard[posy + 1][posx - 1]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy -1 ][posx + 1] == gameboard[posy + 1][posx - 1] == gameboard[posy + 2][posx - 2]:
            return True    
    except IndexError:
        pass 
    try:    
        if gameboard[posy][posx] == gameboard[posy + 1][posx - 1] == gameboard[posy + 2][posx - 2] == gameboard[posy + 3][posx - 3]:
            return True
    except IndexError:
        pass 
    
    #check negative diagonal
    try:
        if gameboard[posy][posx] == gameboard[posy - 1][posx - 1] == gameboard[posy - 2][posx - 2] == gameboard[posy - 3][posx - 3]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy - 1][posx - 1] == gameboard[posy - 2][posx - 2] == gameboard[posy + 1][posx + 1]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy - 1][posx - 1] == gameboard[posy + 1][posx + 1] == gameboard[posy + 2][posx + 2]:
            return True
    except IndexError:
        pass 
    try:
        if gameboard[posy][posx] == gameboard[posy + 1][posx + 1] == gameboard[posy + 2][posx + 2] == gameboard[posy + 3][posx + 3]:
            return True
    except IndexError:
        pass

if __name__ == "__main__":
    print(tabulate.tabulate(gameboard, headers=header, tablefmt="grid"))
    win = False
    while not win:
        gameboard, posx, posy = play(players[0])
        win = wincondition(posx, posy)
        if win == True:
            print("PLAYER 1 WINS")
            break
        gameboard, posx, posy = play(players[1])
        win = wincondition(posx, posy)
        if win == True:
            print("PLAYER 2 WINS")
            break
    print("GAME ENDED")