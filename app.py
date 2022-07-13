import argparse
import aiohttp
import asyncio
import logging

from NeMo.src.asr import speech_recognition as asr
from NeMo.src.tts import text_to_speech as tts
from recording import recorder

LOCALHOST = "127.0.0.1"
urls = [
    ''
]


async def start_app():
    recorded_audio_file = await asyncio.run(recorder.start_recording())
    async with aiohttp.ClientSession() as session:
        async with session.get(urls[0]) as resp:
            response = await resp.json()
            print(response)
            print(response['name'])
    # response = requests.get(urls[0])
    # response_text = None
    # if response.status_code == 200:
    #     response_text = response.text
    logging.info(response.status_code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-v', '--verbose', help='', action='store_true')
    parser.add_argument('-d', '--debug', help='', action='store_true')
    parser.add_argument('-c', '--config', help='', nargs=1)
    args = parser.parse_args()

    level = logging.DEBUG if hasattr(args, 'debug') else logging.INFO
    start_app()
