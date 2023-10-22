import random
print("PRACTICE TEST") 

questions = open('ReviewerProgram\questions.txt').read().splitlines()
answers = open('ReviewerProgram\\answers.txt').read().splitlines()

indexList = random.sample((range(0,len(questions))), len(questions))
score = 0

for x in range(len(questions)):
    
    response = input(f"\n{x+1}. {questions[indexList[x]]}: ").lower()

    if response == (answers[indexList[x]].lower()):
        print("Correct!")
        score = score+1
    else: print(f"Incorrect! It's {answers[indexList[x]]}!")
    
input(f"\nYou got {score}/{len(questions)} points!")