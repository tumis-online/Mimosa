import argparse
import asyncio
import logging

from NeMo.asr.speech_recognition import STTHandler
from recording import recorder


async def start_app():
    recorded_audio_file = await asyncio.run(recorder.start_recording())
    stt_handler = STTHandler()
    text_output = await stt_handler.stt_from_file(recorded_audio_file)
    logging.info(text_output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-v', '--verbose', help='', action='store_true')
    parser.add_argument('-d', '--debug', help='', action='store_true')
    parser.add_argument('-c', '--config', help='', nargs=1)
    args = parser.parse_args()

    level = logging.DEBUG if hasattr(args, 'debug') else logging.INFO
    start_app()
