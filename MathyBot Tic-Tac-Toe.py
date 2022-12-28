#TIC-TAC-TOE CODE FOR MATHYBOT
#Comments only for things I would forget.

#sets firstpalce count to see if the bot has placed the first mark
firstplacecount=0
#initializes board
board=[0,1,2,
       3,4,5,
       6,7,8]



winning=[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],[0,4,8], [2,4,6], ["a", "b", "c"]]
count=-1
count1=0

bre=False

while bre==False:
    bruh=True
    #variable names are hard to understand because they were made quickly
    yessir=0
    for e in range(len(winning)):
        if winning[e][0]=="x" and winning[e][1]=="x" and winning[e][2]=="x":
            print("X WON")
            bre=True
        elif winning[e][0]=="o" and winning[e][1]=="o" and winning[e][2]=="o":
            print("O WON")
            bre=True
    #bre varible shows if a player has won
    if bre==False:
        player1 = int(input("Enter the place: "))
        yessir=0
        placex=True
    #puts the players input on the board.
    for i in winning:
        count=winning.index(i)
        if player1 in i:
            winning[count][i.index(player1)]="x"
            if player1 in board:
                board[player1]="x"

                count=-1
    #initializes all new variables
    computer=0
    computercount=0
    ocount=0
    #puts the "o" mark in the 4th spot if conditions are met. 
    if player1!=4 and firstplacecount==0 and board[4]!="x" and board[4]!="o":
        firstplacecount+=1
        board[4]="o"
        for i in winning:
            for k in i:
                if k==4:
                    #finds the indexes in which 4 is in 
                    winning[winning.index(i)][i.index(k)]="o"
    else:

        for i in winning:
              #another way to add the "o" if it sees two "x", however this was done more efficiently later.(dont use this has code, it was done better after)
            # if ocount==2:
            #     print(f"There are two o in {winning[winning.index(i) - 1]}")
            #     for l in winning[winning.index(i)-1]:
            #         if l!="o":
            #             winning[winning.index(i) - 1][winning[winning.index(i) - 1].index(l)] = "o"
            #             if l in board:
            #                 board[l]="o"
            #checks if it sees two "x" in a index.
            if computercount==2 and placex==True:
                print(f"There is 2 x in {winning[winning.index(i)-1]}")

                for q in winning[winning.index(i)-1]:
                    if q!="x":
                        for i in winning:
                            for k in i:
                                if k==q:
                                    #blocks the two "x"
                                    winning[winning.index(i)][winning[winning.index(i)].index(q)]="o"
                        if q in board:
                            board[q]="o"
                break




            else:

                computercount=0
                ocount=0
                yessirs=0
                for qw in winning:
                    if ocount == 2:
                        print(f"I found it in {winning.index(qw)-1}")
                        for ew in winning[winning.index(qw)-1]:
                        
                            #type was used as if its anything other then an int it cannot be what we are looking for. 
                            
                            if type(ew)==int:                        
                                winning[winning.index(qw) - 1][winning[winning.index(qw) - 1].index(ew)] = "o"
                                board[ew] = "o"
                                placex=False

                        # winning[winning.index(qw)-1][winning[winning.index(qw) - 1].index(ew)] = "o"
                        # board[ew] = "o"
                        # placex = False
                        break
                    else:
                        yessirs+=1
                        ocount=0
                        for ew in qw:
                            if ew=="o" and "x" not in qw:
                                ocount+=1
            if yessirs==9:
                for j in i:
                    if j=="x" and "o" not in i:
                                computercount+=1


        #finds non filled index spaces if all conditions are false. This was put out of the "for" loop.
        while bruh and ocount!=2 and computercount!=2 and bre==False and placex==True:
            for i in winning:
                if bruh==False:
                    break
                for w in i:
                    if w!="x" and w!="o" and w!="a" and w!="b" and w!="c":
                        print(f"There is a open space in {i}, it is {w}")
                        for i in winning:
                            for k in i:
                                if k==w:
                                    winning[winning.index(i)][winning[winning.index(i)].index(w)]="o"
                        board[w]="o"
                        bruh=False
                        break



    #prints the board after each turn. This is in the while loop so it repeats untill other conditions are met. 
    print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))
    print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
    print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))
    print()
    print(winning)
