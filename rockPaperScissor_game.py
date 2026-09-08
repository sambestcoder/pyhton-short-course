#......Rock Paper Scissor___ Game......

#logic = rock vs paper ------>  paper winner
#        rock vs scissor----->  rock winner
#        paper vs scissor---->  scissor winer.

import random
l = ["rock", "paper", "scissor"]

while True:    
    ccount = 0 #.... computer ka count..
    ucount = 0  #.... user ka count...
 
    uc = int(input(''' 
Game  start....
1 yes 
2 No / exit                                      
                   
'''))
    if(uc==1):
        for a in range(1,6):
            userInput = int(input(''' 
1 Rock
2 Scissor
3 paper

'''))
            if(userInput==1):
                uchoice = "rock"
            elif(userInput==2):
                uchoice = "scissor"
            elif(userInput==3):
                uchoice = "paper"
            Cchoice = random.choice(l)
            if(uchoice==Cchoice):
                print(" Game is Draw..")
                print("computer Value:- ", Cchoice)
                print("user Value:- ", uchoice)
                ccount = ccount+1 #... agar game draw zala tar ccount and ucount vadhla
                ucount = ucount+1  #                                  payejet
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="scissor" and Cchoice=="paper") or (uchoice=="paper"and  Cchoice=="rock"):                                                                                       
                print("computer Value:- ", Cchoice)
                print("user Value:- ", uchoice)
                print(" You  Are Win..")
                ucount = ucount+1 
                print(ucount)
            else:
                print("computer Value:- ", Cchoice)
                print("user Value:- ", uchoice)
                print(" Computer  Are Win..")
                ccount = ccount+1
                print(ccount)
                
            

            
            
            


               


                  

    else:
        break
winner()



         
    

    
    

