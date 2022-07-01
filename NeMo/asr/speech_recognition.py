import logging
from os import path
from os.path import exists

import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
from nemo.collections.asr.models import asr_model

sound_dir = "../sounds/"
example_sound_dir = sound_dir + "examples/"
model: asr_model


async def stt_from_stream(stream):
    pass


async def stt_from_file(sample_file: path):
    """
    Takes sample file input and converts it into text.
    :param sample_file: mono and sampled at 16Khz
    :return:
    """
    if not exists(sample_file):
        logging.error(f"Could not locate sample file {sample_file}. Exiting asr...")
        exit(1)
    logging.info(f"Found sample file {sample_file}. Continuing asr...")
    transcriptions = model.transcribe([sample_file])
    print(transcriptions)

    # this will also trigger model download
    punctuation = nemo_nlp.models.PunctuationCapitalizationModel.from_pretrained(model_name='punctuation_en_distilbert')
    res = punctuation.add_punctuation_capitalization(queries=transcriptions)
    print(res)


async def example_to_text():
    # This will initiate pre-trained model download from NGC
    sample_file = f"{example_sound_dir}samples_thorsten-21.06-emotional_neutral.wav"
    await stt_from_file(sample_file)


async def main():
    model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("stt_de_citrinet_1024")
    await example_to_text()


if __name__ == '__main__':
    main()
