from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok", "message": "Minimal Vercel deployment working"}

@app.get("/api/{path:path}")
def catch_all(path: str):
    return {"status": "ok", "path": path}

handler = app
