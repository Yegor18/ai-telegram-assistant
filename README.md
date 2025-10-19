# 🤖 AI Telegram Bot Assistant

A full-stack Telegram bot that uses OpenAI for intelligent replies, summarizes articles, sets reminders, and logs everything to PostgreSQL. Includes a desktop interface (Electron + Vue) to visualize logs and analytics.

## 🚀 Features
- Ask questions via AI (`/ask`)
- Summarize articles (`/summarize <URL>`)
- Set reminders (`/remind`)
- View interaction history (`/history`)
- Logs all data in PostgreSQL
- Clean desktop UI for analytics

## ⚙️ Tech Stack
- Python (bot logic)
- PostgreSQL (database)
- OpenAI API
- Telegram Bot API
- Electron + Vue (UI)

## 🔧 Setup

```bash
git clone <repo>
cd ai_telegram_bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
