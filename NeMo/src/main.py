from os import path

from fastapi import FastAPI

from NeMo.src.asr import speech_recognition as asr

app = FastAPI()


stt_handler = asr.STTHandler()

requests = []


@app.put("/")
async def read_root() -> str:
    return "Connection to speech recognition API established."


@app.put("/asr/")
async def stt_from_file(audio_file_path: path) -> str:
    return await stt_handler.stt_from_file(audio_file_path)


@NotImplemented
@app.get("/tts/")
async def generate_speech_from_file(file_path: path) -> str:
    """
    Generates speech via tts from provided text file and save it to wav file.
    :param file_path: text file with sentence to convert to speech
    :return: file_name str
    """
    pass
