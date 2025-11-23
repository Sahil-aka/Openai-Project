import sys
import os

# Add the backend directory to the sys.path
# This allows importing modules from the backend folder
sys.path.append(os.path.join(os.path.dirname(__file__), '../backend'))

from fastapi import FastAPI
import traceback

app = FastAPI()

try:
    from main import app as backend_app
    handler = backend_app
except Exception as e:
    error_msg = str(e)
    tb = traceback.format_exc()
    print(f"Import Error: {error_msg}")
    
    @app.get("/{path:path}")
    def catch_all(path: str):
        return {
            "status": "error",
            "message": "Failed to import backend application",
            "error": error_msg,
            "traceback": tb.splitlines()
        }
    handler = app
