# Deployment Guide - Live Multimodal Translation System

This guide will help you deploy your application to production. Your app consists of:
- **Frontend**: React + Vite
- **Backend**: FastAPI (Python)
- **Database**: SQLite (for development, consider PostgreSQL for production)

## 📋 Pre-Deployment Checklist

- [x] Code pushed to GitHub
- [ ] Environment variables configured
- [ ] Production build tested locally
- [ ] API keys secured
- [ ] Database configured for production

---

## 🚀 Recommended Deployment Options

### Option 1: Vercel (Frontend) + Render (Backend) ⭐ **RECOMMENDED**

This is the easiest and most reliable option for your stack.

#### **Frontend Deployment (Vercel)**

1. **Go to [Vercel](https://vercel.com)**
   - Sign up/login with your GitHub account

2. **Import Your Repository**
   - Click "Add New Project"
   - Select your GitHub repository
   - Vercel will auto-detect it's a Vite project

3. **Configure Build Settings**
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

4. **Add Environment Variables**
   - Add this variable:
     ```
     VITE_API_URL=https://your-backend-url.onrender.com
     ```
   - (You'll get the backend URL after deploying to Render)

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete
   - You'll get a URL like: `https://your-app.vercel.app`

#### **Backend Deployment (Render)**

1. **Go to [Render](https://render.com)**
   - Sign up/login with your GitHub account

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Service**
   - **Name**: `openai-translator-backend` (or your choice)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables**
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=sqlite:///./sql_app.db
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (first deploy takes 5-10 minutes)
   - You'll get a URL like: `https://your-backend.onrender.com`

6. **Update Frontend Environment**
   - Go back to Vercel
   - Update `VITE_API_URL` with your Render backend URL
   - Redeploy frontend

---

### Option 2: Railway (Full Stack) 🚂

Deploy both frontend and backend on Railway.

1. **Go to [Railway](https://railway.app)**
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository

3. **Deploy Backend**
   - Railway will detect your Python app
   - Add environment variables:
     ```
     GEMINI_API_KEY=your_api_key
     SECRET_KEY=your_secret_key
     PORT=8000
     ```
   - Set start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

4. **Deploy Frontend**
   - Add a new service from the same repo
   - Set root directory to `frontend`
   - Build command: `npm run build`
   - Start command: `npm run preview`
   - Add environment variable:
     ```
     VITE_API_URL=https://your-backend.railway.app
     ```

5. **Generate Domains**
   - Railway will provide URLs for both services
   - Update CORS settings in backend to allow frontend domain

---

### Option 3: Render (Full Stack) 🎨

Deploy both on Render using separate services.

1. **Deploy Backend** (same as Option 1)

2. **Deploy Frontend as Static Site**
   - Go to Render Dashboard
   - Click "New +" → "Static Site"
   - Connect your repository
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/dist`
   - Add environment variable:
     ```
     VITE_API_URL=https://your-backend.onrender.com
     ```

---

## 🔧 Configuration Files

### Create `vercel.json` in project root

```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/dist",
  "framework": "vite",
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

### Create `render.yaml` in project root (for Render Blueprint)

```yaml
services:
  - type: web
    name: translator-backend
    env: python
    region: oregon
    buildCommand: pip install -r backend/requirements.txt
    startCommand: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: GEMINI_API_KEY
        sync: false
      - key: SECRET_KEY
        sync: false
      - key: DATABASE_URL
        value: sqlite:///./sql_app.db

  - type: web
    name: translator-frontend
    env: static
    buildCommand: cd frontend && npm install && npm run build
    staticPublishPath: frontend/dist
    envVars:
      - key: VITE_API_URL
        value: https://translator-backend.onrender.com
```

---

## 🗄️ Database Configuration

### For Production (PostgreSQL)

If you want to use PostgreSQL instead of SQLite:

1. **Add to `requirements.txt`**:
   ```
   psycopg2-binary
   ```

2. **Update `backend/database.py`**:
   ```python
   import os
   
   DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
   
   # Fix for Render PostgreSQL URL
   if DATABASE_URL.startswith("postgres://"):
       DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
   
   engine = create_engine(DATABASE_URL)
   ```

3. **On Render**:
   - Create a PostgreSQL database
   - Copy the Internal Database URL
   - Add it as `DATABASE_URL` environment variable

---

## 🔐 Environment Variables Setup

### Backend Environment Variables

Create these in your hosting platform:

| Variable | Description | Example |
|----------|-------------|---------|
| `GEMINI_API_KEY` | Your Google Gemini API key | `AIza...` |
| `SECRET_KEY` | JWT secret for authentication | Generate with `openssl rand -hex 32` |
| `DATABASE_URL` | Database connection string | `sqlite:///./sql_app.db` or PostgreSQL URL |

### Frontend Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API URL | `https://your-backend.onrender.com` |

---

## ✅ Post-Deployment Steps

1. **Test Your Deployment**
   - Visit your frontend URL
   - Try registering a new user
   - Test translation features
   - Check voice input/output

2. **Update CORS Settings**
   - In `backend/main.py`, update allowed origins:
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://your-app.vercel.app",
           "http://localhost:5173"
       ],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

3. **Monitor Logs**
   - Check backend logs for errors
   - Monitor API usage and costs

4. **Set Up Custom Domain** (Optional)
   - Both Vercel and Render support custom domains
   - Follow their documentation to add your domain

---

## 📱 Mobile Access

Your app will be accessible on mobile browsers via the deployment URL. For the hackathon demo:

1. **Share the URL**: Send the Vercel URL to your phone
2. **Add to Home Screen**: On mobile browser, use "Add to Home Screen" for app-like experience
3. **Test Features**: Ensure voice input works on mobile browsers

---

## 🐛 Troubleshooting

### Frontend can't connect to backend
- Check `VITE_API_URL` is set correctly
- Verify CORS settings in backend
- Check backend is running (visit backend URL)

### Backend crashes on startup
- Check all environment variables are set
- Review logs for missing dependencies
- Verify database connection

### Voice features not working
- Ensure HTTPS (required for microphone access)
- Check browser permissions
- Test on different browsers

### Build fails
- Clear cache and rebuild
- Check Node.js version compatibility
- Verify all dependencies are installed

---

## 💰 Cost Estimation

### Free Tier Limits

- **Vercel**: Free for personal projects, unlimited bandwidth
- **Render**: 750 hours/month free (enough for one service)
- **Railway**: $5 free credit/month

### Recommended for Hackathon

Use **Vercel (frontend) + Render (backend)** - both free tiers are sufficient for a hackathon demo!

---

## 🎯 Quick Start (Fastest Deployment)

1. **Deploy Backend to Render** (10 minutes)
   - New Web Service → Connect GitHub → Configure as shown above
   
2. **Deploy Frontend to Vercel** (5 minutes)
   - New Project → Import from GitHub → Add backend URL

3. **Test** (5 minutes)
   - Visit frontend URL
   - Test all features

**Total Time: ~20 minutes** ⚡

---

## 📞 Need Help?

- **Vercel Docs**: https://vercel.com/docs
- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app

Good luck with your hackathon! 🚀
