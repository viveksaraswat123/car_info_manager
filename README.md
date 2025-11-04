# 🚗 Car Info Manager

A FastAPI + PostgreSQL web application that helps users manage their car information, documents, and service history efficiently. The system automatically notifies users about upcoming document expirations and service reminders.

---

## 🌟 Features

- **User Registration & Authentication** – Secure login and personalized dashboard  
- **Car Management** – Add, view, and update car details  
- **Document Tracking** – Upload and store important files (insurance, PUC, RC, etc.)  
- **Expiry Notifications** – Automated alerts before document or service expiry  
- **Service History** – Maintain service records and billing information  
- **Database Integration** – PostgreSQL with SQLAlchemy ORM  
- **RESTful API** – Built using FastAPI for high performance and scalability  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Validation:** Pydantic  
- **Scheduler:** APScheduler (for expiry notifications)  
- **Frontend:** Basic HTML, CSS, JS (or React if used)  
- **Tools:** Git, VS Code, Postman  

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/car-info-manager.git
   cd car-info-manager


2. **Create a virtual environment**

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate


**Install dependencies**

- pip install -r requirements.txt


**Set up PostgreSQL**

- Create a database named carinfo_db

- Update your connection URL in config.py or .env:

- DATABASE_URL=postgresql://username:password@localhost/carinfo_db


**Run the FastAPI app**

- uvicorn main:app --reload


### Access

- API docs: http://127.0.0.1:8000/docs

- Home: http://127.0.0.1:8000

### 📬 Future Enhancements

- Add email/SMS notification system

- Add cloud storage for documents

- Add role-based access (admin/user)

- Deploy on Render/Heroku