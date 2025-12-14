🛡️ AI Spam & Scam Message Detector (Web Application)

An AI-powered web application built using HTML, CSS, JavaScript, and Flask, designed to detect spam, phishing, and scam messages in real time.
The website provides clear visual alerts, context-based safety warnings, and easy-to-understand guidance to help users avoid online scams.

🚀 Features

✅ Detects Scam / Phishing / Safe messages using AI

🚨 Clear Scam Alert and Safe Message indicators

🧠 Context-aware warnings, such as:

❌ Don’t click suspicious links

❌ Don’t make payments

❌ Banks never ask OTP or account details

❌ Internship/job scams that demand money

🧭 User-friendly “What should I do next?” guidance

🌐 Runs fully in the browser

🔗 Flask backend integrated with an AI NLP model

🧠 How It Works (Simple Explanation)

User pastes an email, SMS, or message into the website

The message is sent to a Flask backend API

An AI phishing detection model analyzes the text

The website displays:

Scam or Safe result

Risk-related warnings

Context-based safety advice

🏗️ Tech Stack

Frontend (Website)

HTML5

CSS3

JavaScript

Backend (AI Server)

Python

Flask

Flask-CORS

<div align="center">
  <img src="screenshots/output1.png" width="24%" />
  <img src="screenshots/output2.png" width="24%" />
  <img src="screenshots/output3.png" width="24%" />
  <img src="screenshots/output4.png" width="24%" />
</div>


⚙️ Setup Instructions

1️⃣ Backend Setup (Flask + AI)

cd backend

pip install -r requirements.txt

python app.py


The backend will run on:

http://127.0.0.1:5000

Hugging Face Transformers

DistilBERT phishing detection mode
