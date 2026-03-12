# 🤖 Web Chatbot

A full-stack AI chatbot powered by **Google Gemini**, built with a **Next.js** frontend and a **FastAPI** backend using the `openai-agents` SDK.

---

## 🗂️ Project Structure

```
bot/
├── frontend/   # Next.js 16 + React 19 + Tailwind CSS
└── backend/    # FastAPI + openai-agents + Python (uv)
```

---

## ⚙️ Tech Stack

| Layer                     | Technology                                          |
| ------------------------- | --------------------------------------------------- |
| Frontend                  | Next.js 16, React 19, Tailwind CSS                  |
| Backend                   | FastAPI, Python 3.14+, openai-agents                |
| AI Model                  | Google Gemini 2.5 Flash (via OpenAI-compatible API) |
| Package Manager (backend) | [uv](https://github.com/astral-sh/uv)               |

---

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [Python 3.14+](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv) — install with `pip install uv`
- A **Google Gemini API key** — get one at [aistudio.google.com](https://aistudio.google.com/app/apikey)

---

### 🔑 Setting Up the Gemini API Key

1. Navigate to the `backend/` folder.
2. Create a `.env` file (or copy/rename `.env.example` if present):
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Replace `your_api_key_here` with your actual Gemini API key.

---

### ▶️ Running the App

Open **two terminals** — one for the backend and one for the frontend.

#### Terminal 1 — Backend (FastAPI)

```bash
cd backend
uv sync
uv run fastapi dev main.py
```

The API will be available at `http://localhost:8000`.

#### Terminal 2 — Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:3000`.

---

## 📡 API Endpoint

| Method | Endpoint | Description                    |
| ------ | -------- | ------------------------------ |
| POST   | `/chat`  | Send a message to the AI agent |

**Request body:**

```json
{ "message": "Hello!" }
```

**Response:**

```json
{ "response": "Hi! How can I help you?" }
```

---

## 📝 License

MIT
