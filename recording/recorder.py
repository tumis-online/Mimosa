import logging

import pyaudio
import wave

from recording.audio_settings import AudioSettings


def start_recording():
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    logging.info('Recording...')

    sample_format = AudioSettings.SAMPLE_FORMAT
    channels = AudioSettings.CHANNELS
    sample_rate = AudioSettings.SAMPLE_RATE
    chunk = AudioSettings.CHUNK
    filename = AudioSettings.RECORD_FILE_NAME

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=sample_rate,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for x seconds
    # TODO might be set as variable
    seconds = AudioSettings.RECORDING_TIME
    for i in range(0, int(sample_rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    logging.info('Finished recording.')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    start_recording()
