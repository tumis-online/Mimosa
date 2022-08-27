"""API for serving the latest (or specified) model."""
import glob
from os import path
from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse

MODEL_DIR_PATH: str = "models"
MODEL_FILE_NAME: str = "rasa-nlu-model.tar.gz"
MODEL_FILE_TYPE = r'\*tar.gz'

app = FastAPI()


def get_latest_model(model_dir_path=MODEL_DIR_PATH) -> str:
    """Search for latest model in model dir."""
    files = glob.glob(model_dir_path + MODEL_FILE_TYPE)
    latest_model_file = max(files, key=path.getctime)
    return latest_model_file


@app.get("/")
def read_root():
    model_path = get_latest_model()
    return FileResponse(path=model_path, media_type='application/gzip')


@app.get("/models/{model_id}")
def read_model(model_name: Union[str, None] = None):
    return FileResponse(path=MODEL_DIR_PATH, filename=model_name, media_type='application/gzip')
