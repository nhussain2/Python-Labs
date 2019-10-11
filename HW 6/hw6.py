"""
HW6
This program stores a list of the correct answers of an exam. It then asks
the user to enter answers for 20 questions and then displays whether the
student has passed or failed the exam, the number of correct and incorrect
answers and which questions were answered incorrectly
Author: Naveed Hussain
"""

# answer key
answer_key = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A"]

print("This exam has 20 multiple choice questions.")
print("Enter A, B, C or D to answer each question.")

# array to store correct and incorrect answers
correct = []
incorrect = []

# dummy values for counts
correct_count = 0
incorrect_count = 0

# loop to input answers

for i in range(len(answer_key)):
    answer = input("Enter Answer: ")

    if (answer == answer_key[i]):
        correct_count += 1
        correct.append(i+1)

    else:
        incorrect_count +=1
        incorrect.append(i+1)

# output

if (correct_count >= 15):
    print("Congratulations! You have passed the exam!")
else:
    print("Sorry, you were unable to pass the exam.")

print("Number of correct answers: ", correct_count)
print("Number of incorrect answers: ", incorrect_count)
print("Questions answered incorrectly were: ", incorrect)

        

    
    
