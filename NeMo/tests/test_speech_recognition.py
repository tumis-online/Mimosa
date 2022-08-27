import pytest
from difflib import SequenceMatcher

from NeMo.src.asr.speech_recognition import EXAMPLE_SOUND_DIR, STTHandler

EXAMPLE_SOUND_FILE: str = "samples_thorsten-21.06-emotional_neutral.wav"
EXAMPLE_SOUND_FILE_TEXT: str = "Mißt wieder nichts geschafft."


def check_similarity(a: str, b: str) -> bool:
    """
    Checks whether two strings are similar.
    :param a: comparable string
    :param b: comparable string
    :return: true, if similarity ratio of strings is at least .9
    """
    similarity_threshold = 0.9
    return SequenceMatcher(None, a, b).ratio() >= similarity_threshold


class TestASR:
    """pytest class for NeMo ASR"""

    def test_stt_from_file(self) -> None:
        """Checks whether sound file is correctly recognized."""
        stt_handler = STTHandler()
        sample_file = f"{EXAMPLE_SOUND_DIR}{EXAMPLE_SOUND_FILE}"
        result = await stt_handler.stt_from_file(sample_file)
        assert check_similarity(result, EXAMPLE_SOUND_FILE_TEXT)
