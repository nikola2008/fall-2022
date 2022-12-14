import random

quiz = [
    {
        "question": "How tall is the worlds tallest tower? ",
        "choices": [
            "100ft",
            "600ft",
            "2,716ft",
            "3,143ft"
        ],
        "answer": "2,716ft"
    },
    {
        "question": "Who is the worlds richest person? ",
        "choices": [
            "Bill Gates ",
            "Elon Musk ",
            "Jeff Bezos ",
            "Your Mom"
        ],
        "answer": "Your Mom"
    },
    {
        "question": "What is the most commenly looked up thing? ",
        "choices": [
            "Facebook ",
            "Youtube ",
            "Amazon ",
            "Weather "
        ],
        "answer": "Facebook"
    }
]
random.shuffle(quiz)
problemNumber = 0
correct = 0
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f" {choice}")
    
    guess = input("Your guess: ")
    if guess == problem['answer']:
        correct += 1
        print(f"You are correct!")
    else:
        print(f"Incorrect")

    print()

print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}&)")
