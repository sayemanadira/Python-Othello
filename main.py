import random



class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self):
        """Construct objects of type Board, with the given width and height."""
        self.width = 8
        self.height = 8
        self.data = [['  ']*8 for row in range(8)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
    
        s = ''                          # The string to return

        for row in range(0, self.height):
            s += str(row%10) + '|' 
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (3*self.width + 1) * '-' + "\n"   # Bottom of the board

        for col in range(0, self.width):
            s += '  ' + str(col%10)

        # Add code here to put the numbers underneath

        return s       # The board is complete; return it
    def allowMoveVert(self,ox):
        board = self.data
        vertList = []
        for y in range(self.height):
            for x in range(self.width):
                if board[y][x] == ox:
                    if board[y-1][x] != ox and board[y-1][x] != '  ':
                        rlist = range(y-1)
                        for i in rlist[::-1]:
                            if board[i][x] == '  ':
                                vertList.append([x,i])
                                break
                    if board[y+1][x] != ox and board[y+1][x] != '  ':
                        for i in range(y+2,self.height):
                            if board[i][x] == '  ':
                                vertList.append([x,i])
                                break
        return vertList
    def allowMoveHorz(self,ox):
        board = self.data
        vertList = []
        for y in range(self.height):
            for x in range(self.width):
                if board[y][x] == ox:
                    if board[y][x-1] != ox and board[y][x-1] != '  ':
                        rlist = range(x-1)
                        for i in rlist[::-1]:
                            if board[y][i] == '  ':
                                vertList.append([i,y])
                                break
                    if board[y][x+1] != ox and board[y][x+1] != '  ':
                        for i in range(x+2,self.width):
                            if board[y][i] == '  ':
                                vertList.append([i,y])
                                break
        return vertList
    
    def allowMoveDiag(self, ox):
        board = self.data
        diagList = []
        for y in range(self.height):
            for x in range(self.width):
                if board [y][x] == ox:
                    #bottom left (still have one bug, it works tho)
                    if board[y+1][x-1] != ox and board[y+1][x-1] != '  ':
                        xlist = range(x-1)
                        ylist = range(y+1, self.height)
                        flag = False
                        for i in xlist[::-1]:
                            for j in ylist:
                                if board[j][i] == '  ' and abs(x-i) == abs(y-j):
                                    diagList.append([i,j])
                                    flag = True
                                    break
                            if flag == True:
                                break
                    #top right
                    if board[y-1][x+1] != ox and board[y-1][x+1] != '  ':
                        x2list = range(x+1,self.width)
                        y2list = range(y-1)
                        flag = False
                        for i in x2list:
                            for j in y2list[::-1]:
                                if board[j][i] == '  ' and abs(x-i) == abs(y-j):
                                    diagList.append([i,j])
                                    flag = True
                                    break
                            if flag == True:
                                break
                    #top left
                    if board[y-1][x-1] != ox and board[y-1][x-1] != '  ':
                        x3list = range(x-1)
                        y3list = range(y-1)
                        flag = False
                        for i in x3list[::-1]:
                            for j in y3list[::-1]:
                                if board[j][i] == '  ' and abs(x-i) == abs(y-j):
                                    diagList.append([i,j])
                                    flag = True
                                    break
                            if flag == True:
                                break
                    #bottom right
                    if board[y+1][x+1] != ox and board[y+1][x+1] != '  ':
                        x4list = range(x+1,self.width)
                        y4list = range(y+1,self.height)
                        flag = False
                        for i in x4list:
                            for j in y4list:
                                if board[j][i] == '  ' and abs(x-i) == abs(y-j):
                                    diagList.append([i,j])
                                    flag = True
                                    break
                            if flag == True:
                                break
        return diagList



    def placeChip(self, ox, coord):
        if coord not in self.allowMoveHorz(ox) and coord not in self.allowMoveVert(ox) and coord not in self.allowMoveDiag(ox):
            print("Chip cannot be placed. Try again.")

        else:
            self.data[coord[1]][coord[0]] = ox
            rlist_horz = range(coord[0])
            rlist_vert = range(coord[1])

            if ox == '⚫':
                newList = []
                for i in rlist_vert[::-1]: #checks up vertically, from the chip, then flip
                    if self.data[i-1][coord[0]] == '⚫': #checks the presence of white chip in the direction 
                        newList = list(range(i-1,coord[1]))
                        break
                for i in newList[::-1]:
                        print(i)
                        while self.data[i][coord[0]] == '⚪':
                            self.data[i][coord[0]] = '⚫'
                #New Direction
                newList = []
                for i in range(coord[1]+1, self.height): #checks down vertically, from chip, then flip
                    if self.data[i][coord[0]] == '⚫': #checks the presence of white chip in the direction 
                        newList = list(range(coord[1],i))
                        break
                for i in newList:
                    while self.data[i][coord[0]] == '⚪':
                        self.data[i][coord[0]] = '⚫'
                #New Direction
                newList = []
                for i in rlist_horz[::-1]:
                    if self.data[coord[1]][i-1] == '⚫': #checks the presence of white chip in the direction
                        newList = list(range(i-1,coord[0]))
                        break
                for i in newList[::-1]:
                    while self.data[coord[1]][i] == '⚪': #checks left side of chip, then flip (horizontal)
                        self.data[coord[1]][i] = '⚫'
                #New Direction
                newList = []
                for i in range(coord[0]+1,self.width):
                    if self.data[coord[1]][i] == '⚫': #checks the presence of white chip in the direction 
                        newList = list(range(coord[0],i))
                        break
                for i in newList:
                    while self.data[coord[1]][i] == '⚪': #checks left side of chip, then flip (horizontal)
                        self.data[coord[1]][i] = '⚫'
                #New Direction (Diagonal 1, bottom left)
                newList = []
                xlist = []
                ylist = []
                flag = False
                for i in range(coord[1]+1, self.width):
                    for j in list(range(coord[0]-1))[::-1]:
                        if self.data[i][j] == '⚫' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist = list((range(j,coord[0])))
                            ylist = list((range(coord[1]+1,i)))
                            flag = True
                            break
                    if flag == True:
                        break
                for i in ylist:
                    for j in xlist[::-1]:
                        while self.data[i][j] == '⚪': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚫'
                #New Direction (Diagonal 2, top right)
                newList = []
                xlist1 = []
                ylist1 = []
                flag1 = False
                for i in range(coord[1]-1)[::-1]:
                    for j in list(range(coord[0]+1,self.width)):
                        if self.data[i][j] == '⚫' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist1 = list((range(coord[0]+1,j)))
                            ylist1 = list((range(i+1,coord[1])))
                            flag1 = True
                            break
                    if flag1 == True:
                        break
                for i in ylist1[::-1]:
                    for j in xlist1:
                        while self.data[i][j] == '⚪': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚫'

                #New Direction (Diagonal 3, top left)
                newList = []
                xlist2 = []
                ylist2 = []
                flag2 = False
                for i in range(coord[1]-1)[::-1]:
                    for j in list(range(coord[0]-1)[::-1]):
                        if self.data[i][j] == '⚫' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist2 = list((range(j+1,coord[0])))
                            ylist2 = list((range(i+1,coord[1])))
                            flag2 = True
                            break
                    if flag2 == True:
                        break
                for i in ylist2[::-1]:
                    for j in xlist2[::-1]:
                        while self.data[i][j] == '⚪': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚫'
                #New Direction (Diagonal 4, bottom right)
                newList = []
                xlist3 = []
                ylist3 = []
                flag3 = False
                for i in range(coord[1]+1,self.height):
                    for j in list(range(coord[0]+1,self.width)):
                        if self.data[i][j] == '⚫' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist3 = list((range(coord[0]+1,j)))
                            ylist3 = list((range(coord[1]+1,i)))
                            flag3 = True
                            break
                    if flag3 == True:
                        break
                for i in ylist3:
                    for j in xlist3:
                        while self.data[i][j] == '⚪': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚫'
            if ox == '⚪':
                newList = []
                for i in rlist_vert[::-1]: #checks up vertically, from the chip, then flip
                    if self.data[i-1][coord[0]] == '⚪': #checks the presence of white chip in the direction 
                        newList = list(range(i-1,coord[1]))
                        break
                for i in newList[::-1]:
                        print(i)
                        while self.data[i][coord[0]] == '⚫':
                            self.data[i][coord[0]] = '⚪'
                #New Direction
                newList = []
                for i in range(coord[1]+1, self.height): #checks down vertically, from chip, then flip
                    if self.data[i][coord[0]] == '⚪': #checks the presence of white chip in the direction 
                        newList = list(range(coord[1],i))
                        break
                for i in newList:
                    while self.data[i][coord[0]] == '⚫':
                        self.data[i][coord[0]] = '⚪'
                #New Direction
                newList = []
                for i in rlist_horz[::-1]:
                    if self.data[coord[1]][i-1] == '⚪': #checks the presence of white chip in the direction
                        newList = list(range(i-1,coord[0]))
                        break
                for i in newList[::-1]:
                    while self.data[coord[1]][i] == '⚫': #checks left side of chip, then flip (horizontal)
                        self.data[coord[1]][i] = '⚪'
                #New Direction
                newList = []
                for i in range(coord[0]+1,self.width):
                    if self.data[coord[1]][i] == '⚪': #checks the presence of white chip in the direction 
                        newList = list(range(coord[0],i))
                        break
                for i in newList:
                    while self.data[coord[1]][i] == '⚫': #checks left side of chip, then flip (horizontal)
                        self.data[coord[1]][i] = '⚪'
                #New Direction
                newList = []
                for i in range(coord[1]+1, self.width):
                    for j in range(coord[0]-1):
                        if self.data[j][i] == '⚪':
                            newList = list(range(j,i))
                            break
                for i in newList:
                    while self.data[j][i] == '⚫': #checks left side of chip, then flip (horizontal)
                        self.data[j][i] = '⚪'
                #New Direction (Diagonal 1, bottom left)
                newList = []
                xlist = []
                ylist = []
                flag = False
                for i in range(coord[1]+1, self.width):
                    for j in list(range(coord[0]-1))[::-1]:
                        if self.data[i][j] == '⚪' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist = list((range(j,coord[0])))
                            ylist = list((range(coord[1]+1,i)))
                            flag = True
                            break
                    if flag == True:
                        break
                for i in ylist:
                    for j in xlist[::-1]:
                        while self.data[i][j] == '⚫': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚪'
                #New Direction (Diagonal 2, top right)
                newList = []
                xlist1 = []
                ylist1 = []
                flag1 = False
                for i in range(coord[1]-1)[::-1]:
                    for j in list(range(coord[0]+1,self.width)):
                        if self.data[i][j] == '⚪' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist1 = list((range(coord[0]+1,j)))
                            ylist1 = list((range(i+1,coord[1])))
                            flag1 = True
                            break
                    if flag1 == True:
                        break
                for i in ylist1[::-1]:
                    for j in xlist1:
                        while self.data[i][j] == '⚫': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚪'

                #New Direction (Diagonal 3, top left)
                newList = []
                xlist2 = []
                ylist2 = []
                flag2 = False
                for i in range(coord[1]-1)[::-1]:
                    for j in list(range(coord[0]-1)[::-1]):
                        if self.data[i][j] == '⚪' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist2 = list((range(j+1,coord[0])))
                            ylist2 = list((range(i+1,coord[1])))
                            flag2 = True
                            break
                    if flag2 == True:
                        break
                for i in ylist2[::-1]:
                    for j in xlist2[::-1]:
                        while self.data[i][j] == '⚫': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚪'
                #New Direction (Diagonal 4, bottom right)
                newList = []
                xlist3 = []
                ylist3 = []
                flag3 = False
                for i in range(coord[1]+1,self.height):
                    for j in list(range(coord[0]+1,self.width)):
                        if self.data[i][j] == '⚪' and abs(coord[1]-i) == abs(coord[0] - j):
                            xlist3 = list((range(coord[0]+1,j)))
                            ylist3 = list((range(coord[1]+1,i)))
                            flag3 = True
                            break
                    if flag3 == True:
                        break
                for i in ylist3:
                    for j in xlist3:
                        while self.data[i][j] == '⚫': #checks left side of chip, then flip (horizontal)
                            self.data[i][j] = '⚪'

    def clear(self):
        for x in range(self.height):
            for y in range(self.width):
                self.data[x][y] = '  '
    
    def setBoard(self):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        self.data[3][3] = '⚪'
        self.data[4][4] = '⚪'
        self.data[3][4] = '⚫'
        self.data[4][3] = '⚫'
         
    def isFull(self):
        for x in range(self.height):
            for y in range(self.width):
                if self.data[x][y] == '  ':
                    return False
        return True

    def noMovesLeft(self,ox):
        if len(self.allowMoveHorz(ox)) == 0 and len(self.allowMoveVert(ox)) == 0 and len(self.allowMoveDiag(ox)) == 0 :
            return True
        else:
            return False

    def score(self):
        pointsWhite = 0
        for y in self.height:
            for x in self.width:
                if self.data[y][x] == '⚪':
                    pointsWhite += 1
        pointsBlack = 0
        for y in self.height:
            for x in self.width:
                if self.data[y][x] == '⚫':
                    pointsBlack += 1
        return [pointsWhite, pointsBlack]
            # col was empty

    def hostGame(self):
        """
        hosts a game of connect four with an ai playing aginst the user
        """
        while True:
            if self.noMovesLeft('⚫'):
                print('Game over!')
                if self.score()[0] > self.score()[1]:
                    print("White wins!")
                elif self.score()[0] == self.score()[1]:
                    print("It's a draw!")
                else:
                    print ("Black wins!")
                break
            print(self)

            playableMovesBlack = self.allowMoveHorz('⚫') + self.allowMoveVert('⚫') + self.allowMoveDiag('⚫') 
            move = -1
            
            while move < 0 or move >= len(playableMovesBlack)+1:
                print("Pick a move in the playable range")
                print("Player Black can move: ", playableMovesBlack)
                move = int(input("Where do you want to move? "))-1
            
            self.placeChip('⚫',playableMovesBlack[move])
            print(self)

            if self.noMovesLeft('⚪'):
                print('Game over!')
                if self.score()[0] > self.score()[1]:
                    print("White wins!")
                elif self.score()[0] == self.score()[1]:
                    print("It's a draw!")
                else:
                    print ("Black wins!")
                break

            playableMovesWhite =self.allowMoveHorz('⚪') + self.allowMoveVert('⚪') + self.allowMoveDiag('⚪') 
            move = -1

            while move < 0 or move >= len(playableMovesWhite)+1:
                print("Pick a move in the playable range")
                print("Player White can move: ", playableMovesWhite)
                move = int(input("Where do you want to move? "))-1
            
            self.placeChip('⚪',playableMovesWhite[move])

b = Board()
b.setBoard()