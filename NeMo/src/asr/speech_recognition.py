"""Takes formatted wav file as input and processes to text."""

import asyncio
import logging
from os import path
from os.path import exists

import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
from nemo.collections.asr.models import asr_model

SOUND_DIR = "../sounds/"
EXAMPLE_SOUND_DIR = SOUND_DIR + "examples/"


# Handles Speech to Text from file or from stream
class STTHandler:
    pretrained_punctuation_model: str
    pretrained_asr_model: str
    nemo_asr_model: asr_model

    def __init__(self):
        self.pretrained_punctuation_model = "punctuation_en_distilbert"
        self.pretrained_asr_model = "stt_de_citrinet_1024"
        self.nemo_asr_model = \
            nemo_asr.models.EncDecCTCModelBPE.from_pretrained(self.pretrained_asr_model)

    @NotImplemented
    async def stt_from_stream(self, stream) -> str:
        """TODO Realise according to https://github.com/NVIDIA/NeMo/blob/main/tutorials/asr/Streaming_ASR.ipynb.
            Makes use of load_buffers_to_data_layers.py
        """
        raise NotImplementedError

    async def stt_from_file(self, sample_file: path) -> str:
        """
        Takes sample file input and converts it into text.
        :param sample_file: mono and sampled at 16Khz
        :return: text output
        """
        if not exists(sample_file):
            logging.error(f"Could not locate sample file {sample_file}. Exiting asr...")
            exit(1)
        logging.info(f"Found sample file {sample_file}. Continuing asr...")
        transcriptions = self.nemo_asr_model.transcribe([sample_file])
        logging.debug(f"transcriptions: \n{transcriptions}")

        # this will also trigger model download
        punctuation = nemo_nlp.models.PunctuationCapitalizationModel\
            .from_pretrained(model_name=self.pretrained_punctuation_model)
        res = punctuation.add_punctuation_capitalization(queries=transcriptions)
        logging.info(f"Given input: '{res}'")
        return res


async def main():
    stt_handler = STTHandler()
    sample_file = f"{EXAMPLE_SOUND_DIR}samples_thorsten-21.06-emotional_neutral.wav"
    await stt_handler.stt_from_file(sample_file)


if __name__ == '__main__':
    asyncio.run(main())
