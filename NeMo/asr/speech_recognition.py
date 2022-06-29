import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp

# This will initiate pre-trained model download from NGC
asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("stt_de_citrinet_1024")
transcriptions = asr_model.transcribe(['samples_thorsten-21.06-emotional_neutral.wav'])
print(transcriptions)

# this will also trigger model download
punctuation = nemo_nlp.models.PunctuationCapitalizationModel.from_pretrained(model_name='punctuation_en_distilbert')
res = punctuation.add_punctuation_capitalization(queries=transcriptions)
print(res)