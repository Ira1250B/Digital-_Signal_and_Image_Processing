
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import butter, sosfilt
from pydub import AudioSegment

# 1. Load MP3 song
filename = r"C:\Users\bhoga\Downloads\Tum Se Hi - Mohit Chauhan.mp3"  

y, sr = librosa.load(filename, sr=None)

print("Sample Rate:", sr)
print("Duration:", round(len(y) / sr, 2), "seconds")


# Function to save audio as MP3
def save_mp3(filename, audio):
    audio = np.clip(audio, -1, 1)
    sf.write("temp_audio.wav", audio, sr)

    sound = AudioSegment.from_wav("temp_audio.wav")
    sound.export(filename, format="mp3")


# Function to display spectrogram
def plot_spectrogram(signal, title):
    D = librosa.amplitude_to_db(
        np.abs(librosa.stft(signal)), ref=np.max
    )

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(
        D, sr=sr, x_axis="time", y_axis="hz", cmap="viridis"
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.tight_layout()
    plt.show()


# PART A - LOW PASS FILTER

cutoff_frequencies = [500, 1500, 4000]

for cutoff in cutoff_frequencies:

    # Design Butterworth low-pass filter
    sos = butter(
        6, cutoff, btype="low",
        fs=sr, output="sos"
    )

    # Apply filter
    filtered = sosfilt(sos, y)

    # Save MP3
    save_mp3(f"lowpass_{cutoff}Hz.mp3", filtered)

    # Plot spectrogram
    plot_spectrogram(
        filtered,
        f"Low-Pass Filter - {cutoff} Hz"
    )

    print(f"Saved: lowpass_{cutoff}Hz.mp3")


# PART B - BAND PASS FILTER

# Design band-pass filter for vocal frequency range
sos = butter(
    6, [300, 3400],
    btype="bandpass",
    fs=sr,
    output="sos"
)

# Estimate vocals
vocals = sosfilt(sos, y)

# Estimate background music
background = y - vocals

# Display spectrograms
plot_spectrogram(y, "Original Audio")
plot_spectrogram(vocals, "Estimated Vocals (300-3400 Hz)")
plot_spectrogram(background, "Estimated Background Music")

# Save both as MP3
save_mp3("estimated_vocals.mp3", vocals)
save_mp3("estimated_background.mp3", background)

print("All filtered MP3 files saved successfully!")
