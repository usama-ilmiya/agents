import librosa
from fastapi import FastAPI
from pra.routes import audio_processing

app = FastAPI(
    title="Audio Processing API",
    description="API for pronunciation comparison and word recognition using DTW and Whisper.",
    version="1.0.0",
)

# Include routes
app.include_router(audio_processing.router, prefix="/audio", tags=["Audio Processing"])
