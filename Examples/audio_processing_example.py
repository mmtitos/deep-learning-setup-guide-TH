import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load example audio
y, sr = librosa.load(librosa.example('trumpet'), duration=3)

# Display waveform
librosa.display.waveshow(y, sr=sr)
plt.title("Example waveform from Librosa")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
