bank = {
    "headache": {
        "diagnosis": "Tension Headache or Migraine ",
        "type": "symptom",
        "treatment": "Rest in a dark room , hydration , sleep . ",
        "severity": "low"
    },
    "fever": {
        "diagnosis": "Viral Infection or Flu ",
        "type": "symptom",
        "treatment": "Rest , plenty of fluids , cool compress . ",
        "severity": "medium"
    },
    "cold": {
        "diagnosis": "Common Cold",
        "type": "symptom",
        "treatment": "Steam inhalation , gargling salt water . ",
        "severity": "low"
    },
    "chest pain": {
        "diagnosis": "Potential Cardiac Issue or Angina",
        "type": "symptom",
        "treatment": "IMMEDIATE MEDICAL ATTENTION REQUIRED .",
        "severity": "high"
    }
}

def condition(key, info):
    print(f"Condition Check: {key.upper()} ")
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
    print("-" * 42)

def analyze_input(user_msg):
    msg = user_msg.lower().strip()

    greet = ["Hi", "hello", "hey", "Good morning", "greetings", "sup", "yo","what's up"]

    if msg in greet:
        print("\nHey there! I'm your  medical helper bot.     ")
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

print("Health Assistant Terminalin (type 'Exit' to leave)  ")

while True:
    usr = input("Describe your symptoms : ")
    # FIX: compared to "exit" (lowercase) because usr.lower() makes input lowercase
    if usr.lower() == "exit":
        break
    # FIX: Indented this line so it runs inside the loop
    analyze_input(usr)