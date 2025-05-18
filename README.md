
---

# 🧾 **GrievanceAI**: Smart Municipal Complaint Management System




---

## 📌 **Overview**

GrievanceAI is an AI-powered platform designed to streamline the process of lodging and managing municipal complaints. By leveraging Natural Language Processing (NLP) and sentiment analysis, it ensures efficient categorization and prioritization of grievances, enhancing civic engagement and administrative responsiveness.


---

## 🚀 **Key Features**

🤖 **AI-Driven Complaint Categorization**: Automatically classifies complaints into predefined categories such as sanitation, infrastructure, and public safety.

🗣️ **Sentiment Analysis**: Assesses the urgency and severity of complaints based on user sentiment.

💬 **Interactive Chatbot**: Guides users through the complaint submission process and provides real-time assistance.

📊 **Admin Dashboard**: Offers municipal officers a comprehensive view of complaints, enabling efficient resolution tracking.

📱 **Cross-Platform Accessibility**: Accessible via web and mobile applications for user convenience.



---

## 🏗️ **Project Structure**
```
grievance-ai/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── complaint_routes.py
│   │   └── user_routes.py
│   ├── ai_utils.py
│   ├── chatbot/
│   │   ├── chatbot.py
│   │   └── intents.json
│   ├── admin_panel.py
│   ├── config.py
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── web/
│   │   ├── index.html
│   │   ├── styles.css
│   │   └── scripts.js
│   └── mobile/
│       ├── lib/
│       │   ├── main.dart
│       │   └── screens/
│       │       └── home_screen.dart
│       └── pubspec.yaml
├── database/
│   ├── schema.sql
│   └── sample_data.sql
├── tests/
│   ├── test_app.py
│   └── test_models.py
├── LICENSE
├── README.md
└── .gitignore
```

---

## 🧠 **AI Components**

1. **Complaint Categorization (NLP)**

Utilizes NLP techniques to automatically classify complaints into relevant categories, facilitating targeted responses.

2. **Sentiment Analysis**

Analyzes the sentiment of complaint descriptions to determine urgency levels, aiding in prioritization.

3. **Interactive Chatbot**

An AI-powered chatbot assists users in lodging complaints and provides information on existing grievances.


---

## 🖥️ **Frontend Interfaces**

## 🌐 **Web Application**

**Technologies**: HTML, CSS, JavaScript

**Features:**

User-friendly complaint submission form

Real-time chatbot assistance

Responsive design for various devices



## 📱 **Mobile Application**

**Framework**: Flutter

**Features**:

Seamless complaint registration

Push notifications for complaint updates

User profile management




---

## 🛠️ **Backend Services**

**Framework**: Flask

**Database**: SQLite

**APIs**:

**/register**: User registration

**/complaints**: Complaint submission and retrieval

**/status**: Check complaint status




---

## 📦 **Installation & Setup**

**Prerequisites**

'''
Python 3.x

Flutter SDK

Node.js and npm (for frontend dependencies)
```

**Backend Setup**

```
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
**Frontend Web Setup**

cd frontend/web
# Open index.html in your preferred browser

Mobile App Setup

```
cd frontend/mobile
flutter pub get
flutter run
```

---

## 🧪 **Testin**

Backend Tests

```
cd tests
python test_app.py
python test_models.py
```

---

## 🤝 **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.


---

## 📬 **Contact**

For any inquiries or support, please contact bhavishyakaushik3288@gmail.com


---

