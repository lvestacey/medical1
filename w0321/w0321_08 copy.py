import random

flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for gold?": "Au",
    "What is the tallest mountain in the world?": "Mount Everest"
}

def quiz():
    question = random.choice(list(flashcards.keys()))
    answer = flashcards[question]
    
    print(question)
    user_answer = input("Enter your answer: ")
    
    if user_answer.lower() == answer.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is: " + answer)

quiz()