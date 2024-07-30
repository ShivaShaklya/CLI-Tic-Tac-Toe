def print_board(d):
    for i in range(1,10):
        if(i%3==0):
            print(d[i])
            if(i!=9):
                for i in range(0,2):
                    print("-",end=" ")
                print("-")
            
        else:
            print(d[i],end="|")
def check_win(d,player):
    win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for condition in win:
        if(all(d[pos]==player for pos in condition)):
            return True
    return False
def check_draw(d):
    if all(x in ["A","B"] for x in d.values()):
        return True
    return False

#
d={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
print("Tic Tac Toe\n")
print_board(d)
while True: 
    a=int(input("Enter move Player A: "))
    if(str(d[a]).isdigit()):
        d[a]="A"
    else:
        print("Invalid Move")
    print_board(d)
    if(check_win(d,"A")==True):
        print("Player A Won")
        break
    if(check_draw(d)):
        print("Draw")
        break
    b=int(input("Enter move Player B: "))
    if(str(d[b]).isdigit()):
        d[b]="B"
    else:
        print("Invalid Move")
    print_board(d)
    if(check_win(d,"B")==True):
        print("Player B Won")
        break
    if(check_draw(d)):
        print("Draw")
        break
    
    

