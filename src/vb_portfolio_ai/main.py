from fastapi import FastAPI

app = FastAPI(
    title="VB Portfolio AI",
    description="Personal portfolio analysis and AI investment assistant",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "VB Portfolio AI",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
