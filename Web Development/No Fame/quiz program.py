import json

# 👉 Python ko bol rahe hain:
# “Bhai, mujhe JSON files ke saath kaam karna hai.”

with open("questions.json", "r") as file:
    content = file.read()

# 👉 Matlab:
# questions.json file open karo
# Uska poora data string me le lo
# content variable me store karo
# 🧠 Soch:
# File = notebook
# read() = saara likha hua copy kar liya

data = json.loads(content)

# 👉 IMPORTANT LINE ⭐
# JSON text → Python list of dictionaries
# Ab data Python me use ho sakta hai

for question in data:
    print(question["question_text"])
    
# 👉 Har question ka text print ho raha hai

for index, alternative in enumerate(question["alternatives"]):
    print(index + 1, "-", alternative)


#  👉 enumerate kya karta hai?
#     ["Fish", "Mammals"]
#    1 - Fish
#    2 - Mammals
#    🧠 index + 1 isliye, kyunki user 1,2,3 se answer deta hai


user_choice = int(input("Enter your answer: "))
question["user_choice"] = user_choice


# 👉 User ka answer:
# number hota hai (isliye int)
# Us question ke andar save ho jata hai

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"


# 👉 Simple logic:
# User ka answer == correct answer → score +1
# warna wrong


message = f"{index + 1}) {result} - Your answer: {question['user_choice']} - Correct answer: {question['correct_answer']}"
print(message)

# 👉 Ye bas pretty output ke liye hai

