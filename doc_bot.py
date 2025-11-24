import os
import time
import random

bank = {
    "headache": {
        "diagnosis": "Tension Headache or Migraine ",
        "type": "symptom",
        "treatment": "Rest in a dark room , hydration , sleep . ",
        "medication": "Ibuprofen , Paracetamol . ",
        
    },
    "fever": {
        "diagnosis": "Viral Infection or Flu ",
        "type": "symptom",
        "treatment": "Rest , plenty of fluids , cool compress . ",
        "medication": "Acetaminophen , fever reducers . ",
        
    },
    "cold": {
        "diagnosis": "Common Cold",
        "type": "symptom",
        "treatment": "Steam inhalation , gargling salt water . ",
        "medication": "Cough syrup , Decongestants . ",
        
    },
    "chest pain": {
        "diagnosis": "Potential Cardiac Issue or Angina",
        "type": "symptom",
        "treatment": "IMMEDIATE MEDICAL ATTENTION REQUIRED .",
        "medication": "None - Call Emergency . ",
        
    }
}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def condition(key, info):
    # time module 
    print("\nChecking Database", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    
    # random module 
    conf = random.randint(70, 99)
    
    print(f"Condition Check: {key.upper()} (Confidence: {conf}%)")
    print("Diagnosis / Possible Issue:", info["diagnosis"])
    print("-" * 42)

    if info.get("severity") == "high":
        print("\n  CRITICAL NOTICE  ")#notice
        print("This looks like something that needs   urgent professional care  .")
        print("So yeah… pleases don't rely on me for this one.\n")

    recommended_treatment = info["treatment"]
    print(f"Suggested treatment:\n -> {recommended_treatment}")

    # adding the file
    print(f"Suggested medications:\n -> {info.get('medication'  , 'Not listed in database')}")
    
    #prevention tips
    print(f"Preventions Tips:\n -> {info.get('prevention', 'Not listed in database'  )}")
    
    # time module 
    print(f"Time of report: {time.strftime('%H:%M:%S')}")
    print("-" * 42)

def analyze_input(user_msg):
    msg = user_msg.lower().strip()

    greet = ["Hi", "hello", "hey", "Good morning", "greetings", "sup", "yo","what's up"]

    if msg in greet:
        # random module greeting
        greetings_list = [
            "\nHey there! I'm your  medical helper bot.     ",
            "\nHello. I am ready to help. ",
            "\nYo. What hurts today? "
        ]
        print(random.choice(greetings_list))
        print("Tell me what you're feeling — like 'fever', 'cold', etc.\n")
        return

    was_found = False

    for symptom, details in bank.items():
        if symptom in msg:
            condition(symptom, details)
            was_found = True
            break

    if not was_found:
        print("\nHmm… I don't seemed to have that condition noted anywhere.")
        print("Try anothers symptom like 'fever' or 'headache'.")
        print("Or, you know, maybe talk to a real doctor just in case.\n")

# os module 
clear()
print("Health Assistant Terminalin (type 'Exit' to leave)  ")

while True:
    usr = input("Describe your symptoms : ")
    if usr.lower() == "exit":
        # random module tip on exit
        tips = [
            "Drink water . ",
            "Sleep more . ",
            "Eat apples . "
        ]
        print("\nClosing down...")
        time.sleep(1)
        print(f"Tip: {random.choice(tips)}")
        break
    analyze_input(usr)