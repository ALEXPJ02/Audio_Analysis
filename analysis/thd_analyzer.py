
# Author: Alexandro Jauregui
import numpy as np
import matplotlib.pyplot as plt

def compute_thd(signal, sample_rate=48000, fundamental_freq=1000, max_harmonic=5, plot=False):
    N = len(signal)
    freqs = np.fft.rfftfreq(N, 1/sample_rate)
    spectrum = np.abs(np.fft.rfft(signal))

    # Find index of fundamental
    fundamental_idx = np.argmin(np.abs(freqs - fundamental_freq))
    fundamental_amp = spectrum[fundamental_idx]

    harmonic_amplitudes = []
    for n in range(2, max_harmonic + 1):
        harmonic_freq = fundamental_freq * n
        idx = np.argmin(np.abs(freqs - harmonic_freq))
        harmonic_amplitudes.append(spectrum[idx])

    harmonic_power = np.sum(np.square(harmonic_amplitudes))
    thd = np.sqrt(harmonic_power) / fundamental_amp

    if plot:
        plt.figure(figsize=(10, 4))
        plt.plot(freqs, 20 * np.log10(spectrum + 1e-10))
        plt.title("Frequency Spectrum")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude (dB)")
        plt.grid()
        plt.tight_layout()
        plt.show()

    return thd * 100  # return THD as percentage