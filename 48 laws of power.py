import random

laws_of_power = [
    {"law": "Never outshine the master.", "number": 1},
    {"law": "Never put too much trust in friends, learn how to use enemies.", "number": 2},
    {"law": "Conceal your intentions.", "number": 3},
    {"law": "Always say less than necessary.", "number": 4},
    {"law": "So much depends on reputation—guard it with your life.", "number": 5},
    {"law": "Court attention at all costs.", "number": 6},
    {"law": "Get others to do the work for you, but always take the credit.", "number": 7},
    {"law": "Make other people come to you—use bait if necessary.", "number": 8},
    {"law": "Win through your actions, never through argument.", "number": 9},
    {"law": "Infection: avoid the unhappy and unlucky.", "number": 10},
    {"law": "Learn to keep people dependent on you.", "number": 11},
    {"law": "Use selective honesty and generosity to disarm your victim.", "number": 12},
    {"law": "When asking for help, appeal to people’s self-interest, never to their mercy or gratitude.", "number": 13},
    {"law": "Pose as a friend, work as a spy.", "number": 14},
    {"law": "Crush your enemy totally.", "number": 15},
    {"law": "Use absence to increase respect and honor.", "number": 16},
    {"law": "Keep others in suspended terror: cultivate an air of unpredictability.", "number": 17},
    {"law": "Do not build fortresses to protect yourself—isolation is dangerous.", "number": 18},
    {"law": "Know who you’re dealing with—do not offend the wrong person.", "number": 19},
    {"law": "Do not commit to anyone.", "number": 20},
    {"law": "Play a sucker to catch a sucker—seem dumber than your mark.", "number": 21},
    {"law": "Use the surrender tactic: transform weakness into power.", "number": 22},
    {"law": "Concentrate your forces.", "number": 23},
    {"law": "Play the perfect courtier.", "number": 24},
    {"law": "Recreate yourself.", "number": 25},
    {"law": "Keep your hands clean.", "number": 26},
    {"law": "Play on people’s need to believe to create a cult-like following.", "number": 27},
    {"law": "Enter action with boldness.", "number": 28},
    {"law": "Plan all the way to the end.", "number": 29},
    {"law": "Make your accomplishments seem effortless.", "number": 30},
    {"law": "Control the options: get others to play with the cards you deal.", "number": 31},
    {"law": "Play to people’s fantasies.", "number": 32},
    {"law": "Discover each man’s thumbscrew.", "number": 33},
    {"law": "Be royal in your own fashion: act like a king to be treated like one.", "number": 34},
    {"law": "Master the art of timing.", "number": 35},
    {"law": "Disdain things you cannot have: ignoring them is the best revenge.", "number": 36},
    {"law": "Create compelling spectacles.", "number": 37},
    {"law": "Think as you like but behave like others.", "number": 38},
    {"law": "Stir up waters to catch fish.", "number": 39},
    {"law": "Despise the free lunch.", "number": 40},
    {"law": "Avoid stepping into a great man’s shoes.", "number": 41},
    {"law": "Strike the shepherd and the sheep will scatter.", "number": 42},
    {"law": "Work on the hearts and minds of others.", "number": 43},
    {"law": "Disarm and infuriate with the mirror effect.", "number": 44},
    {"law": "Preach the need for change, but never reform too much at once.", "number": 45},
    {"law": "Never appear too perfect.", "number": 46},
    {"law": "Do not go past the mark you aimed for: in victory, learn when to stop.", "number": 47},
    {"law": "Assume formlessness.", "number": 48},
]

def get_random_question(laws):
    question = random.choice(laws)
    correct_answer = question["law"]
    all_answers = [correct_answer]
    
    while len(all_answers) < 4:
        wrong_answer = random.choice(laws)["law"]
        if wrong_answer not in all_answers:
            all_answers.append(wrong_answer)
    
    random.shuffle(all_answers)
    return question["number"], correct_answer, all_answers

def quiz_user(laws):
    score = 0
    for _ in range(10):  # Quiz the user with 10 questions
        number, correct_answer, answers = get_random_question(laws)
        print(f"Law {number}:")
        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")
        user_answer = input("Choose the correct law by number: ")
        if answers[int(user_answer) - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {correct_answer}")
        print()
    
    print(f"Your final score is {score} out of 10.")

if __name__ == "__main__":
    quiz_user(laws_of_power)
