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
        # List files to debug structure
        files = []
        try:
            for root, dirs, filenames in os.walk("."):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
        except Exception as walk_err:
            files.append(f"Error listing files: {walk_err}")

        return {
            "status": "error",
            "message": "Failed to import backend application",
            "error": error_msg,
            "traceback": tb.splitlines(),
            "cwd": os.getcwd(),
            "sys_path": sys.path,
            "files": files[:50] # Limit to first 50 files
        }
    handler = app
