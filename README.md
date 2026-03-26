# Experiment 4: Basic Arithmetic Calculator API
A bug-free, full-stack prototype of a basic calculator that performs addition, subtraction, multiplication, and division via a RESTful API.

## 🚀 Overview
This project demonstrates a decoupled architecture where the mathematical logic is handled by a **Python Flask API** (Backend) and the user interactions are managed by a **Responsive Web UI** (Frontend).

### Key Features:
* **API-Driven:** Calculations are executed on the server-side via POST requests.
* **Keyboard Support:** Full mapping for NumPad and standard keys (0-9, +, -, *, /, Enter, Backspace).
* **Error Handling:** Built-in protection against "Division by Zero" and invalid operations.
* **Device Independent:** Configured to run seamlessly on GitHub Codespaces.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** Flask (REST API)
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **Environment:** GitHub Codespaces / Local Terminal

---

## 📂 Project Structure
```text
.
├── app.py              # Flask Server & Calculation Logic
├── requirements.txt    # Project Dependencies
├── templates/
│   └── index.html      # Calculator UI & Keyboard Event Listeners
└── README.md           # Documentation
