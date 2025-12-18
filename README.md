# Hybrid AI-Powered Code Generator

A robust,  web application designed to automate the generation of programming scripts and algorithms. This project utilizes a **Hybrid System Architecture** that combines the power of Large Language Models (LLMs) with a high-reliability local fallback library.



## 🌟 Key Features
- **AI Intelligence Layer**: Integrates the **Google Gemini 2.0 API** to generate complex, custom code logic based on natural language queries.
- **Failover Mechanism (Graceful Degradation)**: Implements an automatic switch to a **Local JSON-based Library** if the API quota is exhausted or the system is offline.
- **Universal Safety Net**: A tertiary logic layer that provides functional boilerplate code for unrecognized queries when AI is unavailable.
- **Cross-Language Support**: Capable of generating both **Python** and **JavaScript** templates.
- **Production-Ready**: Optimized for cloud deployment using **Gunicorn**.

## 🛠️ Tech Stack
- **Backend**: Python 3.12, Flask
- **AI Engine**: Google GenAI SDK (Gemini API)
- **Deployment**: Gunicorn, Render/Heroku
- **Frontend**: Clean HTML5 & CSS3
- **Local Data**: JSON Template Engine

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/)

