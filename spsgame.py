def Results(m,n):
 print("YOUR SCORE:",m)
 print("COMPUTER SCORE:",n)
 if(m>n):
  print("YOU WON THE MATCH!!!")
 elif(m<n):
     print("COMPUTER WON THE MATCH!!")
 else:
     print("DRAW!!")
def Choices():
    from random import randint
    i=0
    yp=0
    cp=0
    g= ["Rock", "Paper", "Scissors"]
    n=input("ENTER THE NUMBER OF ROUNDS:")
    for i in range(int(n)):
       print("ROUND:",i+1)
       computer = g[randint(0,2)]
       player = input("YOUR CHOICE!!(Rock, Paper, Scissors)=")
       print("COMPUTER CHOICE:",computer)
       if player == computer:
        print("DRAW !!!")
       elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
            cp=cp+1
        else:
            print("You win!")
            yp=yp+1
       elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
            cp=cp+1
        else:
            print("You win!")
            yp=yp+1
       elif player == "Scissors":
        if computer == "Rock":
            print("You lose!")
            cp=cp+1
        else:
             print("You win!")
             yp=yp+1
       else:
        print("INVALID SPELLING")

    Results(yp,cp)



    
        

"""MAIN FUCTION"""
print("""WELCOME TO THE GAME OF ROCK PAPER AND SCISSORS
         RULES ARE SIMPLE...YOUR CHOICE MATTERS..
         YOU WON ONLY WHEN YOU CHOOSE
         PAPER OVER ROCK
         ROCK OVER SCISSORS
         SCISSOR OVER PAPER...
         LETS GET STARTED !!!""")
z=0
if z==0:
 Choices()
 print("   :):) THANK YOU :):) ")
        
