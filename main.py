from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Cloud Run! Your GitHub connection works!"}

@app.get("/healthz")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    # Cloud Run provides a dynamic PORT environment variable. We must listen on it.
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(main:app, host="0.0.0.0", port=port)
