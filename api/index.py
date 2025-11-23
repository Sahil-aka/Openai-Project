import sys
import os

# Add the backend directory to the sys.path
# This allows importing modules from the backend folder
sys.path.append(os.path.join(os.path.dirname(__file__), '../backend'))

from main import app

# Vercel expects a variable named 'app' or 'handler'
handler = app
