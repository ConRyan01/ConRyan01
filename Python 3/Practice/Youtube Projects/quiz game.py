print("Welcome to Shizzle my Quizzle!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play.")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    score = score+1
    print ("Correct!")   
else:
    print('incorrect')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    score = score+1
    print ("Correct!")   
else:
    print('incorrect')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    score = score+1
    print ("Correct!")   
else:
    print('incorrect')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    score = score+1
    print ("Correct!")   
else:
    print('incorrect')

print ('your final score is ', score)


