# Healthcare-Monitoring-AI-Agent

A simple AI-powered healthcare assistant that helps users track medications, monitor daily fitness activities, and access reliable health information through trusted medical sources.

Personal Health Assistant

A simple AI-powered healthcare assistant that helps users track medications, monitor daily fitness activities, and access reliable health information through trusted medical sources.

Project Overview

The Personal Health Assistant is designed to provide essential healthcare monitoring features while keeping the application lightweight and easy to use.

The project focuses on:

* Medication tracking and reminders
* Basic fitness monitoring
* Health information lookup
* Nutrition tracking
* Simple patient dashboard

---

Features

Medication Management

* Add medications and dosage schedules
* View upcoming medications
* Receive reminder notifications
* Track medication history

Fitness Tracking

* Daily step count monitoring
* Calories burned tracking
* Activity summary dashboard

🥗 Nutrition Tracking

* Food calorie lookup
* Nutrition information retrieval
* Daily calorie consumption tracking

📚 Health Information Lookup

* Search reliable medical information
* Drug information lookup
* Basic symptom and condition information

📊 Patient Dashboard

* Medication overview
* Daily fitness statistics
* Nutrition summary
* Health insights

---

Tech Stack

| Component    | Technology            |
| ------------ | --------------------- |
| Backend      | Python                |
| AI Framework | LangChain             |
| LLM          | Groq API / OpenAI API |
| UI           | Streamlit             |
| Database     | SQLite                |
| Deployment   | Streamlit Cloud       |

---

APIs Used

### Health Data

* Google Fit API *(steps and calories tracking)*

### Nutrition Data

* Edamam API *(nutrition and calorie information)*

### Medical Information

* MedlinePlus API *(trusted health information)*

---

Project Structure

```text
personal-health-assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── dashboard.py
│   ├── medications.py
│   ├── fitness.py
│   └── health_lookup.py
│
├── database/
│   └── health_data.db
│
├── utils/
│   ├── api_handler.py
│   ├── reminder_service.py
│   └── health_tools.py
│
└── assets/
    └── images/
```

---

Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd personal-health-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add API keys

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
EDAMAM_APP_ID=your_app_id
EDAMAM_APP_KEY=your_app_key
GOOGLE_FIT_API_KEY=your_api_key
```

### 6. Run the application

```bash
streamlit run app.py
```

---

Project Goals

* Build strong healthcare AI fundamentals.
* Learn API integration using real-world services.
* Understand LangChain tool usage.
* Create an interactive healthcare dashboard.
* Deploy a production-ready application using Streamlit Cloud.

---

Future Improvements

* Wearable device integration
* AI health recommendations
* Sleep tracking
* Water intake reminders
* Doctor appointment management
* Health report generation

---
