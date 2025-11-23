# Vercel Backend Deployment Guide

## Quick Start

The backend is configured for Vercel deployment. Follow these steps:

### 1. Login to Vercel
```bash
vercel login
```
Visit the URL shown and authenticate.

### 2. Set Environment Variables
Before deploying, add these in Vercel Dashboard (Settings → Environment Variables):

- `GEMINI_API_KEY` - Your Google Gemini API key
- `OPENAI_API_KEY` - Your OpenAI API key (optional)
- `AI_PROVIDER` - Set to `gemini` or `openai`
- `SECRET_KEY` - JWT secret (generate with `openssl rand -hex 32`)

### 3. Deploy
```bash
cd backend
vercel --prod --yes
```

### 4. Update Frontend
After deployment, update your frontend's `VITE_API_URL` environment variable to point to the new backend URL.

## Files Created
- `vercel.json` - Vercel configuration
- `api/index.py` - ASGI entry point
- `ENV_SETUP.md` - Detailed environment variable documentation

## Important Notes
⚠️ **Database**: SQLite will reset on each deployment. For production, migrate to PostgreSQL or another cloud database.
⚠️ **CORS**: Currently allows all origins. Restrict in production.
