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
    # Get the dynamic port provided by Cloud Run, defaulting to 8080 locally
    port = int(os.environ.get("PORT", 8080))
    
    # FIX IS HERE: "main:app" must be a string in quotes!
    uvicorn.run("main:app", host="0.0.0.0", port=port)
