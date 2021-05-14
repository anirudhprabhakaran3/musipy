import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

def load_wav(path):
    """
        This funciton loads a WAV file
        into the program.

        Input -> path to the WAV file
        Output -> array with WAV file data, 
                  frame rate of the audio
    """
    wav_file = wave.open(path)
    samples = wav_file.getnframes()
    audio = wav_file.readframes(samples)

    audio = np.frombuffer(audio, dtype=np.int16)
    audio = audio.astype(np.float32)

    frame_rate = wav_file.getframerate()

    return audio, frame_rate

def plot_wav(audio, frame_rate):
    """
        This function plots the waveform
        of the audio file.

        Input -> Audio, Frame Rate
        Output -> Plot of the wave
    """
    temp_audio = audio[1:100000]

    plt.plot(temp_audio)
    plt.show()