import random


def play():
    computer_count = 0
    user_count = 0
    computer_standing = False
    user_standing = False
    
    print("Let's play higher or lower!\n")
    while computer_standing == False and user_standing == False:
        computer = random.choice(range(1,10))
        user = random.choice(range(1,10))
        x = input("Press enter to start a round. \n")
        print("The dealer has", computer, ",you have", user, ".")
        
        if computer > user:
            print("The dealer won this round!\n")
            computer_count += 1
        elif computer < user:
            print("U won this round!\n")
            user_count += 1
        else:
            print("I'ts a tie, try again!")
        print("The score is:")
        print("Dealer: ",computer_count,)
        print("User: ", user_count, "\n")
        print("______________________________________")
        if computer_count == 5:
            computer_standing = True
        if user_count == 5:
            user_standing = True
    if computer_standing:
        print("Computer Won!!")
    else:
        print("You won!!")
        

play()
    

    
        
            
        
    

