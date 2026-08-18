# Password Leak Checker

A lightweight desktop application built with **Python, PyWebView and JavaScript** that checks whether a password has appeared in known data breaches using the **Have I Been Pwned Pwned Passwords API**.

## Features

- Password leak detection
- Have I Been Pwned API integration
- SHA-1 hashing
- k-anonymity approach
- Python ↔ JavaScript communication through PyWebView
- Simple desktop interface
- Network error handling and request timeout

## How it works

The application does not send the complete password or its complete SHA-1 hash to the API.

```text
Password
   ↓
SHA-1 hash
   ↓
First 5 characters of the hash
   ↓
Pwned Passwords API
   ↓
Compare the remaining hash locally
```

This is based on the range API and its k-anonymity model.

## Technologies

- Python
- Requests
- PyWebView
- JavaScript
- HTML5
- CSS3
- Have I Been Pwned API

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/luccaschumaher/Password-Leak-Checker.git
cd Password-Leak-Checker
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python app.py
```

## Security note

The application is an educational cybersecurity project. It uses the Pwned Passwords range API so the complete password is not sent to the service. A result of "no known breach found" does not guarantee that a password has never been compromised.

## Author

**Lucca Schumaher**

GitHub: https://github.com/luccaschumaher
