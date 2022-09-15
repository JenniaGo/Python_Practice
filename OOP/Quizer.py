#Usage: Quizer.py | then type yes to start and select the type of Quiz you want to answer. (Open questions or Closed)

from string import ascii_lowercase

print("Welcome to my Quizzer game!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit()

# Open Quiz V1: simple if\else Quizzer
def Open_Quiz_V1():
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

    answer = input("Who has seen the  the end of war?  ")
    if answer.lower() == "the dead":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")


    print("Quiz is over, You got : " +str(score) + " questions correct")
    print(" Your Score is: " + str((score / 4) * 100) + "%.")

#Open quiz V2: looping the euestions, each question with correct answer as second item at the list
def Open_Quiz_V2():
    QUESTIONS = [
        ("What does GPU stand for? ", "graphic processing unit"),
        ("Which built-in function can get information from the user? ", "input"),
        ("Which keyword do you use to loop over a given list of elements? ", "for")
    ]
    score = 0
    for question, correct_answer in QUESTIONS:
        answer = input(f"{question}?")
        if answer.lower() == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect, the answer is {correct_answer!r}, not {answer!r}")

    print("Quiz is over, You got : " + str(score) + " questions correct")
    print("Your Score is: " + str((score / len(QUESTIONS)) * 100) + "%.")

#Open quiz V3: provide multiple choices using a dictionary, label choise than direct value, more user friendly
def Open_Quiz_V3():
    QUESTIONS = {
        "When was Bibi first elected? ": [
            "1999", "2009", "2012", "1982"
        ],
        "Which built-in function can get information from the user ": [
            "input", "get", "print", "write"
        ],
        "Which keyword do you use to loop over a given list of elements ": [
            "for", "while", "each", "loop"
        ],
        "What's the purpose of the built-in zip() function ": [
            "To iterate over two or more sequences at the same time",
            "To combine several strings into one",
            "To compress several files into one archive",
            "To get information from the user",
        ]
    }
    score = 0
    for question, alternatives in QUESTIONS.items():
        correct_answer = alternatives[0]
        sorted_alternatives = sorted(alternatives)
        for label, alternative in enumerate(sorted_alternatives):
            print(f" {label!r}) {alternative}?")

        answer_label = int(input(f"{question}? "))
        answer = sorted_alternatives[answer_label]
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")

    print("Quiz is over, You got : " + str(score) + " questions correct")
    print("Your Score is: " + str((score / len(QUESTIONS)) * 100) + "%.")

Open_Quiz_V3()