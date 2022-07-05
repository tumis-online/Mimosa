# Setting up NeMo docker container
# if training, loading tts german data
# lets download the files we need to run this tutorial
#
# !mkdir /NeMo
# !cd /NeMo && wget https://raw.githubusercontent.com/nvidia/NeMo/$BRANCH/scripts/dataset_processing/tts/openslr/get_data.py
# !cd /NeMo && wget https://raw.githubusercontent.com/nvidia/NeMo/$BRANCH/examples/tts/fastpitch.py
# !cd /NeMo && wget https://raw.githubusercontent.com/nvidia/NeMo/$BRANCH/examples/tts/hifigan_finetune.py
# !cd /NeMo && wget https://raw.githubusercontent.com/nvidia/NeMo/$BRANCH/scripts/dataset_processing/tts/extract_sup_data.py
# !cd /NeMo && wget https://raw.githubusercontent.com/NVIDIA/NeMo/$BRANCH/examples/tts/conf/de/fastpitch_align_22050.yaml
# !cd /NeMo && wget https://raw.githubusercontent.com/NVIDIA/NeMo/$BRANCH/examples/tts/conf/hifigan/hifigan.yaml
# !cd /NeMo && wget https://raw.githubusercontent.com/NVIDIA/NeMo/$BRANCH/nemo_text_processing/text_normalization/de/data/whitelist.tsv
#
# !mkdir /Data && \
#     cd /Data && \
#     wget https://us.openslr.org/resources/95/thorsten-de_v02.tgz && \
#     tar -zxvf thorsten-de_v02.tgz