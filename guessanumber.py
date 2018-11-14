import random #Using number 5 for test purposes for now
# secretNumber = random.randint(1,10)

secretNumber = random.randint(1,10)
i = 0
j = 5
keepPlaying = True

print ""
Name = raw_input("What is your name?")
print ""
print "Hi, %s! I am thinking of a number between 1 and 10." % Name

while (keepPlaying == True):
    while (i<5):
        print "You have %i guesses left." % j
        print ""
        yourNumber = input("What is your number?")
    
        if (yourNumber < secretNumber):
            print ""
            print "%i is too low." % yourNumber
            i += 1
            j -= 1
        elif (yourNumber > secretNumber):
            print ""
            print "%i is too high." % yourNumber
            i += 1
            j -= 1
        else:
            if (j ==5):
                print ""
                print "You Win! Perfect!!!"
                break
            else:    
                print ""
                print "You win, %s" % Name
                break
    else:
        print ""
        print "You ran out of guesses. The number was %i." % secretNumber
        break
    print ""
    playAgain = raw_input("Would you like to play again? y or n?")
    if(playAgain == "n"):
        keepPlaying = False
        print "Thanks for playing, %s" % Name
    else:
        keepPlaying = True
        secretNumber = random.randint(1,10)
        i = 0
        j = 5
    


        