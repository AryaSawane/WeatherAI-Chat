🌤️ WeatherAI Chat Application

An AI-powered Weather Application that provides real-time weather information along with a chat-based interface for user-friendly interacktion. The application integrates weather data APIs with an intelligent assistant to answer weather-related queries in a simple and conversational manner.

✨ Features
🎯 Natural language processing - "weather in pune", "is it raining in delhi?"

🤖 AI Agent - LangChain + Claude 3.5 Sonnet with weather tool calling

💬 Real-time chat UI - Smooth animations, auto-scroll, loading states

⚡ Production-ready - CORS configured, proper error handling

🚀 Full-stack - Separate backend/frontend architecture

🛠 Tech Stack
   Frontend
🔹 React 18          - Chat UI + State Management
🔹 Axios             - API Communication
🔹 CSS3              - Modern Animations + Responsive

  Backend
🔹 FastAPI 0.115     - REST API Server
🔹 Uvicorn           - ASGI Server
🔹 Pydantic          - Request Validation
🔹 CORS Middleware   - Cross-origin Support
🔹 Python 3.11       - Runtime

  AI Pipeline
🔹 LangChain 0.3     - Agent Framework
🔹 OpenRouter API    - LLM Gateway
🔹 Claude 3.5 Sonnet - Tool-calling Model

📁 Project Structure
WeatherAI-Chat/
├── backend/
│   ├── main.py          # FastAPI + LangChain agent
│   ├── requirements.txt # Dependencies
│   └── .env             # API keys (gitignore)
└── frontend/
    ├── src/
    │   ├── App.js       # React chat UI
    │   └── App.css      # Modern chat styling
    └── package.json     # React dependencies
├── .gitignore           # Protects secrets
└── README.md





