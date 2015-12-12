import librosa
import os
import numpy as np

MEOWP3S = "../meowp3s"
HIGHMEOW = os.path.join(MEOWP3S, "high_meow.wav")
MEDMEOW = os.path.join(MEOWP3S, "med_meow.wav")
LOWMEOW = os.path.join(MEOWP3S, "low_meow.wav")


def get_beats(y, fs):
    _, beats = librosa.beat.beat_track(y=y, sr=fs)
    beats_in_seconds = librosa.frames_to_time(beats, sr=fs)
    return beats_in_seconds


def make_meow_track(beats, audio_length, fs):
    high_meow, _ = librosa.load(HIGHMEOW, fs)
    med_meow, _ = librosa.load(MEDMEOW, fs)
    low_meow, _ = librosa.load(LOWMEOW, fs)

    high_len = len(high_meow)
    med_len = len(med_meow)
    low_len = len(low_meow)

    bass_drum = np.zeros((audio_length, ))
    snare_drum = np.zeros((audio_length, ))
    high_drum = np.zeros((audio_length, ))

    beats_in_samples = np.round(beats*fs)

    offset = int(low_len*0.75)
    for i in beats_in_samples[::2]:
        if int(i)-offset >= 0 and int(i)+low_len-offset < audio_length:
            bass_drum[int(i)-offset: int(i)+low_len-offset] = low_meow

    offset = 0
    for i in beats_in_samples[1::2]:
        if int(i)-offset >= 0 and int(i)+med_len-offset < audio_length:
            snare_drum[int(i)-offset: int(i)+med_len-offset] = med_meow

    offset = int(high_len*0)
    offbeats_in_samples = (beats_in_samples[:-1] + beats_in_samples[1:])/2
    for i in offbeats_in_samples:
        if int(i)-offset >= 0 and int(i)+high_len-offset < audio_length:
            high_drum[int(i)-offset: int(i)+high_len-offset] = high_meow

    return bass_drum + snare_drum + high_drum


def add_meow_track_to_audio(audio_path, output_path):
    y, fs = librosa.load(audio_path)
    audio_length = len(y)
    beats_in_seconds = get_beats(y, fs)
    meow_track = make_meow_track(beats_in_seconds, audio_length, fs)
    mix = y/np.max(y) + 0.5*meow_track/np.max(meow_track)
    librosa.output.write_wav(output_path, mix, fs)
