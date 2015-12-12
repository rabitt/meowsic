import librosa
import sox
import os
import numpy as np

MEOWP3S = "../meowp3s"
HIGHMEOW = os.path.join(MEOWP3S, "high_meow.wav")
MEDMEOW = os.path.join(MEOWP3S, "med_meow.wav")
LOWMEOW = os.path.join(MEOWP3S, "low_meow.wav")


def get_beats(audio_path):
    y, fs = librosa.load(audio_path)
    _, beats = librosa.beat.beat_track(y=y, sr=fs)
    audio_length = len(y)
    beats_in_seconds = librosa.frames_to_time(beats, sr=fs)
    return beats_in_seconds, audio_length, fs


def make_meow_track(beats, audio_length, fs):
    high_meow, _ = librosa.load(HIGHMEOW, fs)
    med_meow, _ = librosa.load(MEDMEOW, fs)
    low_meow, _ = librosa.load(LOWMEOW, fs)

    high_len = len(high_meow)
    med_len = len(med_meow)
    low_len = len(low_meow)

    bass_drum = np.zeros((audio_length, ))

    print beats
    beats_in_samples = np.round(beats*fs)
    print beats_in_samples

    offset = int(low_len*0.75)
    for i in beats_in_samples:
        bass_drum[int(i)-offset: int(i)+low_len-offset] = low_meow

    

    # librosa.output(bass_drum, "/Users/rachelbittner/Desktop/test.wav")
    librosa.output.write_wav(
        "/Users/rachelbittner/Desktop/test.wav", bass_drum, fs)
    return bass_drum

def add_meow_track_to_audio(audio_path, meow_track_path, output_audio):
    sox.mix([meow_track_path, audio_path], output_audio)