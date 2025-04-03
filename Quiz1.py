# NUIST Quiz Game in Python
def quiz():
print("Welcome to the Animal Quiz!")
print("Answer the following questions:")
# uestions and Answers
questions =[
1, What is the largest animal on Earth?: a. Blue whale, b, Mouse, c. cat"
"2. Which bird can fly backwards?:a. Cuckoo, b. Eagle, c. Hummingbird "
"3. What is the only mammal capable of flight?: a. Bat, b. squirrel, c. Dolphin
]
answers =[
"Blue whale"
"Hummingbird"
"Bat"
]
score =0
# Ask questions
for i in range(len(questions)):
user_answer =input(questions[i]).strip().lower()
if user answer == answers[i]:
print("correct!")
score +=1
else:
print("Incorrect!")
# Provide final score
print("\nQuiz completed!")
print(f"You got {score}/{len(questions)} questions correct.")
# Run the quiz function
quiz()
