import numpy as np
import matplotlib.pyplot as plt

def compute_frequency_response(signal, sample_rate=48000, plot=True):
    N = len(signal)
    freqs = np.fft.rfftfreq(N, d=1/sample_rate)
    spectrum = np.fft.rfft(signal)
    magnitude = np.abs(spectrum)

    if plot:
        plt.figure(figsize=(10, 4))
        plt.plot(freqs, 20 * np.log10(magnitude + 1e-10))
        plt.title("Frequency Response")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude (dB)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    return freqs, magnitude
