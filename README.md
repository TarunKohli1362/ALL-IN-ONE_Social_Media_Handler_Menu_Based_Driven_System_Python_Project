# 🛠️ Python Automation Toolkit

This is a **menu-driven Python project** that combines multiple automation tasks into a single program.

---

## 📌 Features
1. Post on Instagram (info/demo via Zapier/Instabot)
2. Send Email (real implementation using Gmail SMTP)
3. Send SMS (mock)
4. Post on LinkedIn (stores post content in Excel sheet for Zapier integration)
5. Tweet on Twitter (mock)
6. Send WhatsApp Message (mock)

---

## ⚙️ Setup Instructions

1. Install required dependencies:
   pip install openpyxl

2. For email functionality:
   - Use a valid Gmail account
   - Generate an **App Password** from Google Account Security settings
   - Enter details when prompted

3. For LinkedIn integration:
   - Content is saved locally in `linkedin_posts.xlsx`
   - You can connect this sheet to **Zapier** for auto-posting

---

## ▶️ Run the Program
   python3 automation_toolkit.py

---

## 📌 Notes
- Email is fully functional via Gmail SMTP.
- LinkedIn, Instagram, WhatsApp, and Twitter are implemented as **mock/demo or Zapier-based integrations** for learning purposes.
- Extendable for real APIs like Twilio (WhatsApp), Twitter API v2, or Instagram Graph API.

---

## 🎯 Learning Outcome
This project shows how Python can be used as a **Central Automation Hub**, combining social media automation, communication tools, and external integrations in a single menu-driven program.

