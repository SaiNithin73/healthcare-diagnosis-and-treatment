def collect_patient_info():
    print("\n--- Patient Information ---")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    return {"name": name, "age": age, "gender": gender}

def get_symptoms():
    print("\n--- Symptom Entry ---")
    print("Enter symptoms separated by commas (e.g., fever, cough, fatigue):")
    user_input = input("Symptoms: ").lower()
    symptoms = [s.strip() for s in user_input.split(',')]
    return symptoms

def diagnose(symptoms):
    diagnosis_rules = {
        "Common Cold": ["cough", "sore throat", "runny nose"],
        "Flu": ["fever", "body ache", "chills", "fatigue"],
        "COVID-19": ["fever", "cough", "shortness of breath", "loss of taste"],
        "Allergy": ["sneezing", "itchy eyes", "runny nose"],
        "Pneumonia": ["fever", "chest pain", "shortness of breath", "fatigue"],
    }

    possible_diagnoses = []
    for disease, disease_symptoms in diagnosis_rules.items():
        match_count = len(set(symptoms).intersection(disease_symptoms))
        if match_count >= len(disease_symptoms) // 2:
            possible_diagnoses.append(disease)

    return possible_diagnoses

def recommend_treatment(diagnoses):
    treatments = {
        "Common Cold": "Rest, stay hydrated, over-the-counter medicine",
        "Flu": "Antiviral drugs, rest, fluids, pain relievers",
        "COVID-19": "Isolation, antiviral meds, consult healthcare provider",
        "Allergy": "Avoid triggers, antihistamines, nasal sprays",
        "Pneumonia": "Antibiotics (if bacterial), hospitalization in severe cases"
    }

    print("\n--- Diagnosis and Treatment ---")
    if diagnoses:
        for disease in diagnoses:
            print(f"- {disease}: {treatments.get(disease, 'Consult a doctor')}")
    else:
        print("Unable to determine illness based on symptoms. Please consult a doctor.")

def detect_emergency(symptoms):
    emergency_signs = ["chest pain", "shortness of breath", "loss of consciousness"]
    if any(symptom in symptoms for symptom in emergency_signs):
        print("\n!!! EMERGENCY ALERT: Symptoms may require immediate medical attention !!!")

def follow_up_advice():
    print("\n--- Follow-Up Advice ---")
    print("If symptoms worsen or persist beyond 3 days, consult a doctor.")
    print("Maintain good hygiene, stay hydrated, and rest well.")

def main():
    print("=== Healthcare Diagnosis and Treatment System ===")
    patient = collect_patient_info()
    symptoms = get_symptoms()

    print(f"\nAnalyzing symptoms for patient: {patient['name']} ({patient['age']} yrs, {patient['gender']})")
    detect_emergency(symptoms)
    
    diagnoses = diagnose(symptoms)
    recommend_treatment(diagnoses)
    follow_up_advice()

if __name__ == "__main__":
    main()
