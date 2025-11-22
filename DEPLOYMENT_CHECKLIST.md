# 🚀 Quick Deployment Checklist

Use this checklist to deploy your app step-by-step.

## ✅ Pre-Deployment

- [ ] Code pushed to GitHub
- [ ] `.env` files are in `.gitignore` (already done ✓)
- [ ] Have your Gemini API key ready
- [ ] Generate a secret key: `openssl rand -hex 32`

---

## 🎯 Recommended: Vercel + Render (20 minutes)

### Step 1: Deploy Backend to Render (10 min)

1. [ ] Go to https://render.com and sign in with GitHub
2. [ ] Click **"New +"** → **"Web Service"**
3. [ ] Select your repository
4. [ ] Configure:
   - **Name**: `translator-backend`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. [ ] Add Environment Variables:
   ```
   GEMINI_API_KEY=your_actual_api_key
   SECRET_KEY=your_generated_secret_key
   ```
6. [ ] Click **"Create Web Service"**
7. [ ] Wait for deployment (5-10 minutes)
8. [ ] **Copy the backend URL** (e.g., `https://translator-backend.onrender.com`)

### Step 2: Deploy Frontend to Vercel (5 min)

1. [ ] Go to https://vercel.com and sign in with GitHub
2. [ ] Click **"Add New Project"**
3. [ ] Select your repository
4. [ ] Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. [ ] Add Environment Variable:
   ```
   VITE_API_URL=https://translator-backend.onrender.com
   ```
   (Use the URL from Step 1)
6. [ ] Click **"Deploy"**
7. [ ] Wait for deployment (2-3 minutes)
8. [ ] **Copy the frontend URL** (e.g., `https://your-app.vercel.app`)

### Step 3: Test Your Deployment (5 min)

1. [ ] Visit your frontend URL
2. [ ] Register a new account
3. [ ] Test text translation
4. [ ] Test voice translation (allow microphone access)
5. [ ] Test image translation
6. [ ] Test text-to-speech
7. [ ] Check translation history

---

## 🎉 You're Done!

Your app is now live at:
- **Frontend**: `https://your-app.vercel.app`
- **Backend API**: `https://translator-backend.onrender.com`
- **API Docs**: `https://translator-backend.onrender.com/docs`

### Share Your App

- Send the frontend URL to anyone
- Works on mobile browsers too!
- For best mobile experience: "Add to Home Screen"

---

## 🐛 Troubleshooting

### Backend not responding
- Check Render logs for errors
- Verify environment variables are set
- Check if service is running

### Frontend can't connect to backend
- Verify `VITE_API_URL` is correct
- Check browser console for CORS errors
- Ensure backend is deployed and running

### Voice/Image features not working
- Ensure you're using HTTPS (not HTTP)
- Check browser permissions for microphone
- Try a different browser

---

## 💡 Tips

- **Free Tier**: Both Vercel and Render have generous free tiers
- **Custom Domain**: You can add a custom domain later
- **Updates**: Push to GitHub → Auto-deploys to Vercel/Render
- **Logs**: Check Render dashboard for backend logs
- **Analytics**: Vercel provides analytics for free

---

## 📱 For Hackathon Demo

1. **Test on mobile**: Open frontend URL on your phone
2. **Prepare demo account**: Create a test account beforehand
3. **Test all features**: Ensure everything works before demo
4. **Have backup**: Keep localhost running as backup
5. **Share URL**: Easy to share with judges

Good luck! 🍀
