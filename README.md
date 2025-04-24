# Email Alerts on WhatsApp using Twilio

A Python-based automation tool that connects **Gmail** with **WhatsApp** using the **Twilio API** to deliver real-time notifications for important emails — without needing to constantly check your inbox.

## 📌 Project Info
- **College:** G. Narayanamma Institute of Technology and Science (For Women)
- **Department:** Information Technology
- **Academic Year:** January 2025 – May 2025
- **Team:** Akkipelli Srilekha, Challa Sarayu, Potta Nandini

## 🚀 Features
- ✅ Real-time Gmail monitoring using Gmail API
- ✅ Keyword & sender-based intelligent email filtering
- ✅ Batch alerts (groups 3 important emails per WhatsApp message)
- ✅ Daily message limit tracking (Twilio Sandbox: 9 msgs/day)
- ✅ Duplicate alert prevention
- ✅ Unread email threshold warning
- ✅ Simple Tkinter GUI for configuration

## 🛠️ Tech Stack
- Python 3.x
- Gmail API (OAuth 2.0)
- Twilio WhatsApp API
- Tkinter (GUI)

## 📦 Installation

```bash
pip install google-auth google-auth-oauthlib google-api-python-client twilio
```

## ⚙️ Setup

1. Enable Gmail API in [Google Cloud Console](https://console.cloud.google.com/)
2. Download `credentials.json`
3. Create a [Twilio account](https://www.twilio.com/) and connect WhatsApp Sandbox
4. Run the GUI:

```bash
python gui.py
```

## 📁 Project Structure

```
email-whatsapp-alerts/
├── authenticate_gmail.py    # Gmail OAuth2 authentication
├── email_filter.py          # Keyword-based email filtering
├── whatsapp_sender.py       # Twilio WhatsApp integration
├── batch_manager.py         # Batch alert management
├── daily_limit.py           # Daily message limit tracker
├── gui.py                   # Tkinter GUI
├── email_alerts_runtime.py  # Main runtime logic
└── requirements.txt
```

## 🔒 System Architecture

```
Gmail Inbox → Gmail API → Filter Module → Batch Manager → Twilio API → WhatsApp
```

## 📊 Results
- Email detection to WhatsApp delivery: **5–10 seconds**
- Zero duplicate alerts in 100+ email test
- Lightweight: under 10% CPU, runs on 4GB RAM

<!-- init -->
# update 1 - 2025-01-11
# update 2 - 2025-01-11
# update 17 - 2025-01-20
# update 22 - 2025-01-23
# update 33 - 2025-01-29
# update 46 - 2025-02-06
# update 48 - 2025-02-07
# update 54 - 2025-02-09
# update 57 - 2025-02-10
# update 61 - 2025-02-14
# update 63 - 2025-02-15
# update 64 - 2025-02-16
# update 107 - 2025-03-17
# update 115 - 2025-03-22
# update 145 - 2025-04-12
# update 146 - 2025-04-12
# update 164 - 2025-04-20
# update 171 - 2025-04-24