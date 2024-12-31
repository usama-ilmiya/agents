import librosa
from fastdtw import fastdtw
import numpy as np


def extract_mfcc(file_path, sr=16000, n_mfcc=13):
    """
    Extract MFCC features from an audio file.
    """
    y, _ = librosa.load(file_path, sr=sr)
    return librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc).T


def calculate_dtw_distance(mfcc1, mfcc2):
    """
    Calculate DTW distance between two sets of MFCC features.
    """
    distance, _ = fastdtw(mfcc1, mfcc2, dist=lambda x, y: np.linalg.norm(x - y, ord=1))
    return distance


def process_audio_files(reference_path, recorded_path):
    """
    Compare MFCCs of two audio files using DTW.
    """
    ref_mfcc = extract_mfcc(reference_path)
    rec_mfcc = extract_mfcc(recorded_path)

    dtw_distance = calculate_dtw_distance(ref_mfcc, rec_mfcc)
    return {
        "dtw_distance": dtw_distance,
    }
