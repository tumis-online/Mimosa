import json
import nemo
import nemo_text_processing
import torch
import librosa
import numpy as np

from pathlib import Path
from tqdm.notebook import tqdm

from phonemizer.backend import EspeakBackend
import json


"""Start FastPitch Model (en)"""

# Load Tacotron2
from nemo.collections.tts.models import FastPitchModel
spec_generator = FastPitchModel.from_pretrained("tts_en_fastpitch")

# Load vocoder
from nemo.collections.tts.models import Vocoder
model = Vocoder.from_pretrained(model_name="tts_hifigan")

# Generate audio
import soundfile as sf
parsed = spec_generator.parse("You can type your sentence here to get nemo to produce speech.")
spectrogram = spec_generator.generate_spectrogram(tokens=parsed)
audio = model.convert_spectrogram_to_audio(spec=spectrogram)

# Save the audio to disk in a file called speech.wav
sf.write("speech.wav", audio.to('cpu').numpy(), 22050)

"""End FastPitch Model"""



backend = EspeakBackend('de')

data_de = "data/thorsten-de"

input_manifest_filepaths = [
    data_de + "/train_manifest",
    data_de + "/test_manifest",
    data_de + "/val_manifest"]

for input_manifest_filepath in input_manifest_filepaths:
    output_manifest_filepath = input_manifest_filepath+"_phonemes"
    records = []
    n_text = []
    with open(input_manifest_filepath + ".json", "r") as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            records.append(d)
            n_text.append(d['normalized_text'])

    phonemized = backend.phonemize(n_text)

    new_records = []
    for i in range(len(records)):
        records[i]["is_phoneme"] = 0
        new_records.append(records[i])
        phoneme_record = records[i].copy()
        phoneme_record["normalized_text"] = phonemized[i]
        phoneme_record["is_phoneme"] = 1
        new_records.append(phoneme_record)

    with open(output_manifest_filepath + ".json", "w") as f:
        for r in new_records:
            f.write(json.dumps(r) + '\n')