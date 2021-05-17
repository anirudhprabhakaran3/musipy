import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from math import ceil

def load_wav(path):
    """
        Function to load WAV file into the
        project. Uses scipy.io.wavfile.read

        Input -> Path of the WAV file
        Output -> Sample rate of audio, and Numpy
                  array containing data
    """
    sample_rate, audio = read(path)

    audio = np.array(audio, dtype=float)

    return sample_rate, audio

def write_wav(audio, sample_rate, path):
    """
        Function to write WAV file to system.
        Uses scipy.io.wavfile.write

        Input -> Audio array, sample rate and path
                 to save to.
    """
    write(path, sample_rate, audio)

def plot_wav(audio):
    """
        Function that plots audio data
        Uses matplotlib.pyplot.

        Input -> Audio array
        Output -> Matplotlib diagram
    """
    plt.plot(audio)
    plt.show()

def find_length(audio, sample_rate, round=False):
    """
        Function that returns length of the
        audio file.

        Input -> Audio array, sample rate, whether
                 the output should be a rounded integer
                 or float value
        Output -> Float value of length of audio
                  in seconds
    """
    length = len(audio) / sample_rate

    if(round):
        return ceil(length)
    else:
        return length