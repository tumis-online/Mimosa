from enum import Enum

import pyaudio


class AudioSettings(Enum):
    CHUNK = 1024  # Record in chunks of 1024 samples
    SAMPLE_FORMAT = pyaudio.paInt16  # 16 bits per sample
    CHANNELS = 1  # Mono
    SAMPLE_RATE = 16_000  # Record at 16.000 samples per second
    RECORDING_TIME = 5  # Recording time in s
    RECORD_FILE_NAME = "speech-recording.wav"
