# 📄 Project Statement — Health Assistant Terminal

## 🔍 Problem Statement
People often search the internet for medical guidance when experiencing common symptoms such as *fever, cold, headache, or chest pain*.  
However, online information can be confusing, unreliable, and overwhelming.  
There is a need for a **quick and simple terminal-based tool** that gives:
- A basic understanding of common symptoms
- A possible diagnosis
- First-aid treatment suggestions
- Warning messages when the condition is severe

This project focuses on providing **beginner-level self-care hints**, not medical treatment.

---

## 📌 Scope of the Project
The scope of this project includes:
- A Python-based console program
- A medical data dictionary with symptoms and related information
- Detection of user input and mapping it to symptoms
- Displaying diagnosis, severity and recommended treatment
- Showing strong warning messages for high-risk symptoms

The project does **NOT** include:
- Real doctor consultation
- AI-generated medical diagnosis
- Accessing medical databases or internet resources
- Emergency medical decision making

---

## 🧑‍💻 Target Users
This application is suitable for:
| User Category | Benefit |
|--------------|---------|
| Students | Learn Python dictionaries and chatbot logic |
| Beginners in programming | Easy introduction to input/output and loops |
| People practicing medical-based projects | Ready-to-use base model |
| Individuals curious about symptoms | Basic self-care suggestions (non-clinical) |

⚠️ **This tool is NOT intended for patients needing real medical guidance.**  
Always consult a doctor for actual health issues.

---

## 🔹 High-Level Features
| Feature | Description |
|--------|-------------|
| Symptom recognition | Detect symptoms from user input |
| Simulated "AI" | Uses time and random to create fake loading bars and confidence percentages. |
| System Integration | Uses the os module to auto-clear the terminal screen on launch. |
| Condition report | Displays diagnosis, treatment & severity level |
| Critical warning | Strong alert when “high severity” symptoms are detected |
| Safe fallback | User notified when unknown symptoms are entered |
| User interaction loop | Program continues until user types `Exit` |
| Crash-free lookup | Uses `.get()` to avoid key errors in medical data |

---

 
