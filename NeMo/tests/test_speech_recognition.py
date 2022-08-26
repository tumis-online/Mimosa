import pytest

from NeMo.src.asr.speech_recognition import EXAMPLE_SOUND_DIR, STTHandler

EXAMPLE_SOUND_FILE: str = "samples_thorsten-21.06-emotional_neutral.wav"
EXAMPLE_SOUND_FILE_TEXT: str = ""


class TestASR:
    """pytest class for NeMo ASR"""

    def test_stt_from_file(self) -> None:
        """Checks whether sound file is correctly recognized."""
        stt_handler = STTHandler()
        sample_file = f"{EXAMPLE_SOUND_DIR}{EXAMPLE_SOUND_FILE}"
        result = await stt_handler.stt_from_file(sample_file)
        assert result == EXAMPLE_SOUND_FILE_TEXT
