# Web-Based Leave Management System

A simple and professional web-based leave management system built using **Flask** and **MySQL**.  
This project is designed as an internal HR application where employees can apply for leave and administrators can approve or reject requests.

---

## 🚀 Features
- Employee login
- Apply for leave
- View leave status
- Admin approval and rejection
- Professional pastel + corporate UI
- MySQL database integration

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS (Pastel Minimal, Corporate Style)
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Version Control:** GitHub

---

## 📂 Project Structure
leave_app/
│
├── app.py
├── db_config.py
├── static/
│ └── style.css
└── templates/
├── login.html
├── dashboard.html
└── apply_leave.htmL

---

## ⚙️ How to Run Locally

1. Install required packages:
```bash
pip install flask mysql-connector-python

## ⚙️ How to Run Locally

1. Install required packages:
```bash
pip install flask mysql-connector-python
CREATE DATABASE leave_db;
USE leave_db;

2.CREATE TABLE leaves (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    reason VARCHAR(100),
    days INT,
    status VARCHAR(20)
);
3.Update database credentials in db_config.py

4.Run the application:
  python app.py

5.Open browser:
  http://127.0.0.1:5000/
🔐 Security Note

Database credentials are masked in this public repository.
For local execution, update db_config.py with your own credentials.

🎯 Use Case

This application simulates an internal enterprise HR portal and demonstrates backend logic, database integration, and professional UI design.


