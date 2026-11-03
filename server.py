import os
import secrets
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

APP_TOKEN = os.getenv("APP_TOKEN", "")
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "")

app = FastAPI(title="Myanmar AI Voice Studio API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN] if FRONTEND_ORIGIN else [],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization", "X-App-Token"],
)

class TTSRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)
    voice_id: str = "male1"
    speed: float = Field(default=1.0, ge=0.5, le=2.0)
    pitch: float = Field(default=1.0, ge=0.5, le=2.0)

def require_token(token: str | None):
    if not APP_TOKEN:
        raise HTTPException(status_code=503, detail="Server setup is incomplete.")
    if not token or not secrets.compare_digest(token, APP_TOKEN):
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/health")
def health():
    return {"status": "ok", "service": "Myanmar AI Voice Studio API"}

@app.post("/api/tts")
def text_to_speech(payload: TTSRequest, x_app_token: str | None = Header(default=None)):
    require_token(x_app_token)
    # Add a real Burmese TTS provider here. Keep provider keys in server environment variables.
    raise HTTPException(status_code=501, detail="TTS provider has not been configured yet.")

@app.post("/api/voice-clone")
def voice_clone(x_app_token: str | None = Header(default=None)):
    require_token(x_app_token)
    # Add a voice-cloning provider and consent checks before enabling this endpoint.
    raise HTTPException(status_code=501, detail="Voice cloning provider has not been configured yet.")
