import asyncio
import logging
from os import path
from os.path import exists

import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
from nemo.collections.asr.models import asr_model

sound_dir = "../sounds/"
example_sound_dir = sound_dir + "examples/"
pretrained_punctuation_model = "punctuation_en_distilbert"
pretrained_asr_model = "stt_de_citrinet_1024"
nemo_asr_model: asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained(pretrained_asr_model)


# Handles Speech to Text from file or from stream
class STTHandler:

    def __init__(self, model=asr_model):
        self.model = model

    @NotImplemented
    async def stt_from_stream(self, stream):
        """TODO Realise according to https://github.com/NVIDIA/NeMo/blob/main/tutorials/asr/Streaming_ASR.ipynb.
            Makes use of load_buffers_to_data_layers.py
        """
        pass

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
        transcriptions = self.model.transcribe([sample_file])
        logging.debug(f"transcriptions: \n{transcriptions}")

        # this will also trigger model download
        punctuation = nemo_nlp.models.PunctuationCapitalizationModel\
            .from_pretrained(model_name=pretrained_punctuation_model)
        res = punctuation.add_punctuation_capitalization(queries=transcriptions)
        logging.info(f"Given input: '{res}'")
        return res


async def main():
    stt_handler = STTHandler(nemo_asr_model)
    sample_file = f"{example_sound_dir}samples_thorsten-21.06-emotional_neutral.wav"
    await stt_handler.stt_from_file(sample_file)


if __name__ == '__main__':
    asyncio.run(main())
