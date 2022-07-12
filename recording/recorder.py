import asyncio
import logging

import pyaudio
import wave

from recording.audio_settings import AudioSettings


def get_devices(pa_interface: pyaudio) -> dict:
    """Returns recording device info.
    :param pa_interface: pyaudio interface
    :returns tuple of id and recording device
    """
    device_info = pa_interface.get_host_api_info_by_index(0)
    num_devices: int = device_info.get("deviceCount")
    print(num_devices)
    input_devices = {}
    for i in range(0, num_devices):
        if (pa_interface.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            device_id = i
            device_name = pa_interface.get_device_info_by_host_api_device_index(0, i).get('name')
            input_devices[i] = {device_id: device_name}
    return input_devices


async def stream_sound(pa_interface: pyaudio, sample_format: int,
                       channels: int, sample_rate: int, chunk: int) -> []:
    """
    Open stream to
    :param pa_interface: pyaudio interface
    :param sample_format:
    :param channels:
    :param sample_rate:
    :param chunk:
    :return: array to store frames
    """
    stream = pa_interface.open(
        format=sample_format,
        channels=channels,
        rate=sample_rate,
        frames_per_buffer=chunk,
        input=True
    )
    frames = []  # Initialize array to store frames

    # Store data in chunks for x seconds
    # TODO might be set as variable for speakers with lower speech rate.
    seconds = AudioSettings.RECORDING_TIME
    for i in range(0, int(sample_rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    return frames


async def start_recording():
    """Recording with audio device."""
    sample_format = AudioSettings.SAMPLE_FORMAT
    channels = AudioSettings.CHANNELS
    sample_rate = AudioSettings.SAMPLE_RATE
    chunk = AudioSettings.CHUNK

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    devices = get_devices(pa_interface=p)
    if logging.DEBUG:
        for device_id, device_name in devices:
            logging.debug("Input Device id ", device_id, " - ", device_name)

    logging.info("Recording...")

    frames = await stream_sound(pa_interface=p, sample_format=sample_format, channels=channels,
                                sample_rate=sample_rate, chunk=chunk)

    # Terminate the PortAudio interface
    p.terminate()

    logging.info("Finished recording.")

    # Save the recorded data as a WAV file
    filename = AudioSettings.RECORD_FILE_NAME
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    logging.info(f"Saved audio input in {filename}.")


if __name__ == '__main__':
    asyncio.run(start_recording())
