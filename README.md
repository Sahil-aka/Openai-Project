# Live Multimodal Language Translation System

A real-time translation system supporting text, voice, and image inputs with AI-powered translation using Google Gemini. Built for the OpenAI Hackathon with support for Indian languages.

## 🌟 Features

- **Text Translation**: Instant translation between multiple languages
- **Voice Translation**: Real-time speech-to-text and translation
- **Image Translation**: OCR and translation of text in images
- **Text-to-Speech**: Audio output in target language
- **User Authentication**: Secure login and registration
- **Translation History**: Track all your translations
- **Dark/Light Mode**: Toggle between themes
- **Responsive Design**: Works on desktop and mobile
- **Indian Language Support**: Hindi, Marathi, Bengali, Tamil, Telugu, Gujarati, Kannada, Malayalam, Punjabi, Urdu, Odia, Assamese

## 🛠️ Tech Stack

**Frontend:**
- React 19
- Vite
- Vanilla CSS

**Backend:**
- FastAPI (Python)
- SQLAlchemy
- Google Gemini AI
- JWT Authentication

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Google Gemini API Key

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/openai-project.git
   cd openai-project
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
   pip install -r requirements.txt
   ```

3. **Create `.env` file in backend directory**
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

4. **Run Backend**
   ```bash
   uvicorn main:app --reload
   ```

5. **Frontend Setup** (in new terminal)
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

6. **Access the app**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## 📦 Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions.

**Quick Deploy:**
- Frontend: [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)
- Backend: [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## 📝 Environment Variables

### Backend
- `GEMINI_API_KEY`: Your Google Gemini API key
- `SECRET_KEY`: JWT secret key (generate with `openssl rand -hex 32`)
- `DATABASE_URL`: Database connection string (optional, defaults to SQLite)

### Frontend
- `VITE_API_URL`: Backend API URL (e.g., `http://localhost:8000` for local)

## 🎯 Usage

1. **Register/Login**: Create an account or login
2. **Select Translation Mode**: Choose text, voice, or image
3. **Select Target Language**: Pick from supported languages
4. **Translate**: Enter/upload content and get instant translation
5. **Listen**: Use text-to-speech to hear the translation
6. **View History**: Check your past translations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

Built for the OpenAI Hackathon

## 🙏 Acknowledgments

- Google Gemini AI for translation capabilities
- OpenAI for inspiration
- FastAPI and React communities

