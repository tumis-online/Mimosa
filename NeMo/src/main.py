from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from NeMo.src.asr import speech_recognition as asr
from NeMo.src.tts import text_to_speech as tts

app = FastAPI()


class SpeechRecognitionHandler(BaseModel):
    stt_handler: asr.STTHandler


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/asr/", response_model=SpeechRecognitionHandler)
async def start_stt_handler():
    stt_handler = asr.STTHandler()
    return stt_handler


@app.get("/tts/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
