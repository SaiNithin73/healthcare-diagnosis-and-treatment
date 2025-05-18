# 🏥 Healthcare Diagnosis and Treatment System

An intelligent healthcare assistant that helps users identify potential illnesses and receive treatment recommendations based on their symptoms. The system captures patient input through a web form, analyzes the symptoms, and provides possible diagnoses and emergency alerts when necessary.

---

## 🚀 Features

- ✅ Interactive symptom input form  
- 🤖 Automated diagnosis based on rule-based symptom matching  
- 🚨 Emergency detection and alert system  
- 💊 Treatment suggestions for common illnesses  
- 📁 Patient data storage with diagnosis history  
- 📱 Mobile-responsive layout using Bootstrap  

---

## 🧱 Technology Stack

### Frontend

- HTML5 & CSS3 (Bootstrap 5)  
- JavaScript  
- Jinja2 templating (Flask)  

### Backend

- Python 3 with Flask  
- SQLite (via SQLAlchemy ORM)  
- Symptom matching logic  

---

## ⚙️ Setup Instructions

### 1. Backend Setup

Install required Python packages:

```bash
pip install flask flask_sqlalchemy
```

Run the Flask application:

```bash
python app.py
```

The app will be available at:

```
http://127.0.0.1:5000
```

### 2. Folder Structure

```
healthcare_project/
├── app.py
├── patients.db         # SQLite database (auto-created)
├── templates/
│   ├── index.html      # Patient input form
│   └── result.html     # Diagnosis results page
```

---

## 🩺 Usage

1. Open the app in your browser.  
2. Enter the patient's name, age, gender, and symptoms.  
3. Click "Diagnose" to receive:
   - A list of potential diagnoses  
   - Suggested treatments  
   - Emergency alert (if critical symptoms detected)  
4. Patient records are saved automatically to the database.

---

## 📌 Development Notes

To upgrade this system for production use:

- Integrate a machine learning model for smarter diagnoses  
- Add a dashboard to review patient records  
- Implement user authentication for doctors/admins  
- Connect to a full-featured database (e.g., PostgreSQL)  
- Add autocomplete for symptom input  
- Improve UX with Tailwind CSS or React frontend  

---

## 📄 License

This project is for educational and demonstration purposes.

