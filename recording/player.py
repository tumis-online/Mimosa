import pyaudio
import wave

from recording.audio_settings import AudioSettings


def play_sound_file(sound_file=AudioSettings.RECORD_FILE_NAME.value):
    """Plays sound_file as stream from wav file."""
    # Set chunk size of 1024 samples per data frame
    chunk = AudioSettings.CHUNK.value

    # Open the sound file
    wf = wave.open(sound_file, 'rb')

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Read data in chunks
    data = wf.readframes(chunk)

    # Play the sound by writing the audio data to the stream
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    # Close and terminate the stream
    stream.close()
    p.terminate()


if __name__ == '__main__':
    play_sound_file()
