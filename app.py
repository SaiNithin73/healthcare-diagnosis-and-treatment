from flask import Flask, render_template, request

app = Flask(__name__)

diagnosis_rules = {
    "Common Cold": ["cough", "sore throat", "runny nose"],
    "Flu": ["fever", "body ache", "chills", "fatigue"],
    "COVID-19": ["fever", "cough", "shortness of breath", "loss of taste"],
    "Allergy": ["sneezing", "itchy eyes", "runny nose"],
    "Pneumonia": ["fever", "chest pain", "shortness of breath", "fatigue"]
}

treatments = {
    "Common Cold": "Rest, stay hydrated, over-the-counter medicine",
    "Flu": "Antiviral drugs, rest, fluids, pain relievers",
    "COVID-19": "Isolation, antiviral meds, consult healthcare provider",
    "Allergy": "Avoid triggers, antihistamines, nasal sprays",
    "Pneumonia": "Antibiotics (if bacterial), hospitalization in severe cases"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    symptoms = request.form['symptoms'].lower().split(',')

    symptoms = [s.strip() for s in symptoms]
    emergency_signs = ["chest pain", "shortness of breath", "loss of consciousness"]
    emergency = any(s in symptoms for s in emergency_signs)

    matched_diagnoses = []
    for disease, disease_symptoms in diagnosis_rules.items():
        if len(set(symptoms) & set(disease_symptoms)) >= len(disease_symptoms) // 2:
            matched_diagnoses.append((disease, treatments[disease]))

    return render_template('result.html',
                           name=name,
                           age=age,
                           gender=gender,
                           emergency=emergency,
                           diagnoses=matched_diagnoses)

if __name__ == '__main__':
    app.run(debug=True)
