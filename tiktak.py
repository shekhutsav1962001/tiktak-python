
x = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
]

p1 = "X"
p2 = "O"

def p(x):
    for i in range(0,3):
        if i != 0:
            print("----------")
        print(x[i][0],"|",x[i][1],"|",x[i][2])
    print("PLAYER-1 ==> X")
    print("PLAYER-2 ==> O")
p(x)


def find(x,value):
    if(value in x[0]):
        return True
    elif value in x[1]:
        return True
    elif value in x[2]:
        return True
    else:   
        return False
    

i=0
flag=True

def update(x,value,p):
    if value == "1":
        x[0][0]=p
    elif value=="2":
        x[0][1]=p
    elif value=="3":
        x[0][2]=p
    elif value=="4":
        x[1][0]=p
    elif value=="5":
        x[1][1]=p
    elif value=="6":
        x[1][2]=p
    elif value=="7":
        x[2][0]=p
    elif value=="8":
        x[2][1]=p
    elif value=="9":
        x[2][2]=p
    else:
        print("INVALID")
        return x
    return x

def display(point):
    if(point==p1):
        print("-----------------------------")
        print("-----------------------------")
        print("Hurrah player1 is winnner!!!")
        print("-----------------------------")
        print("-----------------------------")
    else:
        print("-----------------------------")
        print("-----------------------------")
        print("Hurrah player2 is winnner!!!!")
        print("-----------------------------")
        print("-----------------------------")

def checkwin(x):
    if(x[0][0]==x[0][1] and x[0][1]==x[0][2]):
        display(x[0][0])
    elif(x[1][0]==x[1][1] and x[1][1]==x[1][2]):
        display(x[1][1])
    elif(x[2][0]==x[2][1] and x[2][1]==x[2][2]):
        display(x[2][2])
    elif(x[0][0]==x[1][0] and x[1][0]==x[2][0]):
        display(x[0][0])
    elif(x[0][1]==x[1][1] and x[1][1]==x[2][1]):
        display(x[1][1])
    elif(x[0][2]==x[1][2] and x[1][2]==x[2][2]):
        display(x[2][2])
    elif(x[0][0]==x[1][1] and x[1][1]==x[2][2]):
       display(x[1][1])
    elif(x[0][2]==x[1][1] and x[1][1]==x[2][0]):
       display(x[1][1])
    else:
        return False
    return True        
    
if __name__ == "__main__":
    count=0
    while(flag):
        # print (count)
        if count >= 9:
            print("DRAW!!!")
            break
        if i%2 == 0:
            value =str(input("PLAYER-1 Enter a number: "))
            if find(x,value):
                i=i+1   
                y=update(x,value,p1)
                count=count+1
                x=y
                p(x)
                if(checkwin(x)):
                    break
            else:
                p(x)
                print("Invalid number")
        else:
            value = str(input("PLAYER-2 Enter a number: "))
            if find(x,value):
                i=i+1
                y=update(x,value,p2)
                count=count+1
                x=y
                p(x)
                if(checkwin(x)):
                    break
            else:
                p(x)
                print("Invalid number")