import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------
# 1. MEDICAL KNOWLEDGE BASE (The "Brain" of the Assistant)
# ---------------------------------------------------------
# In a real-world app, this would be a database file (SQL/CSV).
# For a project, a nested dictionary is efficient and easy to explain.
medical_db = {
    # Format: 
    # "keyword": {
    #     "diagnosis": "Name of Disease",
    #     "type": "symptom" or "disease", (helper for search)
    #     "treatment": "How to fix it",
    #     "medication": "Basic meds (OTC)",
    #     "prevention": "How to avoid it",
    #     "severity": "low" or "high" (Triggers doctor referral)
    # }
    
    "headache": {
        "diagnosis": "Tension Headache or Migraine",
        "type": "symptom",
        "treatment": "Rest in a dark room, hydration, sleep.",
        "medication": "Paracetamol or Ibuprofen.",
        "prevention": "Manage stress, stay hydrated, regular sleep schedule.",
        "severity": "low"
    },
    "fever": {
        "diagnosis": "Viral Infection or Flu",
        "type": "symptom",
        "treatment": "Rest, plenty of fluids, cool compress.",
        "medication": "Paracetamol or Acetaminophen.",
        "prevention": "Wash hands often, avoid contact with sick people.",
        "severity": "medium"
    },
    "cold": {
        "diagnosis": "Common Cold",
        "type": "symptom",
        "treatment": "Steam inhalation, gargling salt water.",
        "medication": "Decongestants, Vitamin C.",
        "prevention": "Boost immunity, hygiene.",
        "severity": "low"
    },
    "chest pain": {
        "diagnosis": "Potential Cardiac Issue or Angina",
        "type": "symptom",
        "treatment": "IMMEDIATE MEDICAL ATTENTION REQUIRED.",
        "medication": "Aspirin (only if advised previously).",
        "prevention": "Healthy diet, exercise, quit smoking.",
        "severity": "high" # This triggers the Complex/Referral logic
    },
    "stomach ache": {
        "diagnosis": "Indigestion or Gastritis",
        "type": "symptom",
        "treatment": "Avoid heavy food, drink ginger tea.",
        "medication": "Antacids (e.g., Eno, Gelusil).",
        "prevention": "Eat on time, avoid spicy food.",
        "severity": "low"
    },
    "malaria": {
        "diagnosis": "Malaria",
        "type": "disease",
        "treatment": "Hospitalization and anti-parasitic course.",
        "medication": "Artemisinin-based combination therapy (ACTs).",
        "prevention": "Mosquito nets, insect repellent, remove stagnant water.",
        "severity": "high"
    },
    "diabetes": {
        "diagnosis": "Type 2 Diabetes",
        "type": "disease",
        "treatment": "Blood sugar monitoring, insulin therapy.",
        "medication": "Metformin, Insulin injections.",
        "prevention": "Low sugar diet, weight management, active lifestyle.",
        "severity": "medium"
    },
    "cough": {
        "diagnosis": "Upper Respiratory Infection or Bronchitis",
        "type": "symptom",
        "treatment": "Honey and warm water, steam inhalation, rest.",
        "medication": "Cough syrup (Expectorant or Suppressant), Lozenges.",
        "prevention": "Cover mouth when coughing, hydration.",
        "severity": "medium"
    },
    "rash": {
        "diagnosis": "Allergic Reaction or Dermatitis",
        "type": "symptom",
        "treatment": "Wash with mild soap, apply cool cloth.",
        "medication": "Antihistamines (Benadryl), Hydrocortisone cream.",
        "prevention": "Identify and avoid triggers (food, plants, chemicals).",
        "severity": "low"
    },
    "covid": {
        "diagnosis": "COVID-19",
        "type": "disease",
        "treatment": "Quarantine, rest, hydration, monitor oxygen levels.",
        "medication": "Paracetamol for fever, Antivirals if prescribed.",
        "prevention": "Masks, vaccination, social distancing.",
        "severity": "high"
    },
    "burn": {
        "diagnosis": "Minor Thermal Burn",
        "type": "symptom",
        "treatment": "Run cool (not cold) water over area for 10-15 mins.",
        "medication": "Antibiotic ointment, Aloe Vera.",
        "prevention": "Caution with hot objects/liquids.",
        "severity": "medium"
    },
    "fracture": {
        "diagnosis": "Bone Fracture",
        "type": "symptom",
        "treatment": "Immobilize the area, do not massage.",
        "medication": "Painkillers (prescribed only).",
        "prevention": "Calcium rich diet, safety gear during sports.",
        "severity": "high"
    },
    "food poisoning": {
        "diagnosis": "Foodborne Illness",
        "type": "disease",
        "treatment": "Hydration (ORS), rest, avoid solid foods initially.",
        "medication": "Anti-diarrheal meds (consult doctor first), Probiotics.",
        "prevention": "Hygiene, cook food thoroughly, avoid expired food.",
        "severity": "medium"
    }
}

class DoctorAssistantApp:
    def __init__(self, root):
        """
        Constructor function to set up the GUI window.
        """
        self.root = root
        self.root.title("Virtual Doctor Assistant")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f4f8") # Light blue-grey background

        # --- HEADER SECTION ---
        header_frame = tk.Frame(root, bg="#008080", bd=5)
        header_frame.pack(fill=tk.X)
        
        lbl_title = tk.Label(header_frame, text="Health & Medical Assistant", 
                             font=("Helvetica", 20, "bold"), bg="#008080", fg="white")
        lbl_title.pack(pady=10)

        # --- INPUT SECTION ---
        input_frame = tk.Frame(root, bg="#f0f4f8", pady=20)
        input_frame.pack()

        lbl_instruct = tk.Label(input_frame, text="Enter Symptom or Disease Name:", 
                                font=("Arial", 12), bg="#f0f4f8")
        lbl_instruct.grid(row=0, column=0, padx=10)

        # Entry box for user input
        self.user_input = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.user_input.grid(row=0, column=1, padx=10)
        # Bind the 'Enter' key to the check_condition function
        self.user_input.bind('<Return>', self.check_condition)

        # Button to trigger analysis
        btn_check = tk.Button(input_frame, text="Consult Doctor", command=self.check_condition,
                              bg="#008080", fg="white", font=("Arial", 11, "bold"), padx=10)
        btn_check.grid(row=0, column=2, padx=10)

        # --- RESULTS SECTION ---
        result_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
        result_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Text area to display the output (Scrollable)
        self.result_text = tk.Text(result_frame, font=("Consolas", 11), state=tk.DISABLED, wrap=tk.WORD)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Scrollbar for the text area
        scrollbar = tk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)

        # --- STATUS BAR ---
        self.status_lbl = tk.Label(root, text="Ready...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_lbl.pack(side=tk.BOTTOM, fill=tk.X)

    def check_condition(self, event=None):
        """
        Main logic function:
        1. Get user input.
        2. Search the medical_db dictionary.
        3. Display results or warning based on severity.
        """
        query = self.user_input.get().lower().strip() # Convert input to lowercase for matching
        
        # Clear previous results
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        
        if not query:
            messagebox.showwarning("Input Error", "Please enter a symptom or disease name.")
            self.result_text.config(state=tk.DISABLED)
            return

        # --- GREETING LOGIC ADDED HERE ---
        greetings = ["hi", "hello", "hey", "good morning", "greetings", "sup"]
        if query in greetings:
            self.result_text.insert(tk.END, "Hello! I am your Virtual Doctor Assistant.\n\n")
            self.result_text.insert(tk.END, "How can I help you today?\n")
            self.result_text.insert(tk.END, "Please type a symptom (e.g., 'fever', 'headache') or a disease name.")
            self.result_text.config(state=tk.DISABLED)
            return
        # ---------------------------------

        found = False
        
        # Iterate through database to find a match
        # We use 'in' to check if the keyword exists in the user's sentence
        # e.g., user types "I have a headache", we look for "headache" in that string
        for key, data in medical_db.items():
            if key in query:
                self.display_info(key, data)
                found = True
                break # Stop after finding the first relevant match

        if not found:
            self.result_text.insert(tk.END, "Sorry, I couldn't recognize that condition in my database.\n\n")
            self.result_text.insert(tk.END, "Please try a different keyword (e.g., 'fever', 'headache') \n")
            self.result_text.insert(tk.END, "or consult a real doctor for unknown symptoms.")
        
        self.result_text.config(state=tk.DISABLED) # Make read-only again

    def display_info(self, key, data):
        """
        Helper function to format and print the data to the text box.
        """
        # Header for the result
        self.result_text.insert(tk.END, f"--- REPORT FOR: {key.upper()} ---\n\n")
        
        # 1. Identify the Problem
        self.result_text.insert(tk.END, f"Diagnosis/Problem: {data['diagnosis']}\n")
        self.result_text.insert(tk.END, "-" * 40 + "\n")

        # 2. Check Severity (Complex case logic)
        if data['severity'] == 'high':
            # WARNING IN RED TEXT (Visual feedback)
            self.result_text.tag_config("warning", foreground="red", font=("Arial", 12, "bold"))
            self.result_text.insert(tk.END, "\n[!!!] CRITICAL WARNING [!!!]\n", "warning")
            self.result_text.insert(tk.END, "This condition appears complex or dangerous.\n")
            self.result_text.insert(tk.END, "REFERRAL: Please visit a specialized doctor or hospital IMMEDIATELY.\n\n", "warning")
        
        # 3. Provide Solutions / Treatments
        self.result_text.insert(tk.END, f"Suggested Solution/Treatment:\n -> {data['treatment']}\n\n")

        # 4. Provide Medications (Basic info)
        self.result_text.insert(tk.END, f"Common Medications:\n -> {data['medication']}\n\n")
        
        # 5. Prevention Tips
        self.result_text.insert(tk.END, f"Prevention / Care:\n -> {data['prevention']}\n")

        # Update status bar
        self.status_lbl.config(text=f"Displaying info for {key}")

# ---------------------------------------------------------
# MAIN EXECUTION BLOCK
# ---------------------------------------------------------
if __name__ == "__main__":
    # Create the main window object
    root = tk.Tk()
    
    # Initialize the application
    app = DoctorAssistantApp(root)
    
    # Run the main event loop
    root.mainloop()
    #end 