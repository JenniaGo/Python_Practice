


print("Welcome to my Quizer game!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Get ready...")
score =0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the president of Russia? ")
if answer.lower() == "putin":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who has seem the end of war?  ")
if answer.lower() == "the dead":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("Quiz is over, You got : " +str(score) + " questions correct")
print(" Your Score is: " + str((score / 4) * 100) + "%.")