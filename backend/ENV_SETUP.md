# Environment Variables for Vercel Deployment

When deploying to Vercel, you need to configure the following environment variables in your Vercel project settings:

## Required Environment Variables

### API Keys
- **GEMINI_API_KEY**: Your Google Gemini API key
  - Get it from: https://makersuite.google.com/app/apikey
  
- **OPENAI_API_KEY**: Your OpenAI API key (if using OpenAI provider)
  - Get it from: https://platform.openai.com/api-keys

### Configuration
- **AI_PROVIDER**: Set to either `gemini` or `openai`
  - Determines which AI service to use
  - Default: `gemini`

- **SECRET_KEY**: JWT secret key for authentication
  - Generate a secure random string
  - Example: Use `openssl rand -hex 32` to generate one

## How to Set Environment Variables in Vercel

1. Go to your Vercel dashboard: https://vercel.com/dashboard
2. Select your backend project
3. Go to **Settings** → **Environment Variables**
4. Add each variable:
   - Name: `GEMINI_API_KEY`
   - Value: Your actual API key
   - Environment: Select **Production**, **Preview**, and **Development**
5. Click **Save**
6. Repeat for all required variables

## Important Notes

- Never commit `.env` files to Git
- Environment variables are encrypted by Vercel
- Changes to environment variables require redeployment
- You can also set them via Vercel CLI: `vercel env add VARIABLE_NAME`
