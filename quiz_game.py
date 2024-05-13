print("Welcome to the Thunderdome Bitch!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("ok! let's play :l ")
score = 0

answer = input("What Does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else: 
    print("Wrong!") 

answer = input("What Does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else: 
    print("Wrong!") 

answer = input("What Does DCU stand for? ")
if answer.lower() == "dumb processing unit":
    print("correct!")
    score += 1
else: 
    print("Wrong!") 

answer = input("What Does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else: 
    print("Wrong!") 

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 4) * 100) + "%")