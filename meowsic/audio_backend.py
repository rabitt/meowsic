import librosa
import sox

def get_beats(audio_path):
    y, sr = librosa.load(audio_path)
    _, beats = librosa.beat.beat_track(y=y, sr=sr)
    return beats

def add_meow_track(audio_path, meow_track_path, output_audio):
    sox.mix([meow_track_path, audio_path], output_audio)