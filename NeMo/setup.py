import os

from setuptools import setup

###############################################################################
#                             Dependency Loading                              #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


def req_file(filename, folder="requirements"):
    with open(os.path.join(folder, filename), encoding='utf-8') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters
    # Example: `\n` at the end of each line
    return [x.strip() for x in content]


install_requires = req_file("requirements.txt")

###############################################################################

setup(
    name='nemo_speech_recognition',

    version='1',

    description='Speech Recognition (ASR and TTS) tools',
    long_description='',

    author='Tim Dilger',
    author_email='tdilger@mailbox.org',
    # TODO add license
    license='undefined',
    install_requires=install_requires,
    packages=['src.asr', 'src.tts'],
    zip_safe=False,
)
