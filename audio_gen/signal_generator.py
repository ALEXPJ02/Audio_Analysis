import numpy as np

def generate_sine_wave(freq=1000, duration=5.0, sample_rate=48000, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return amplitude * np.sin(2 * np.pi * freq * t)

def generate_sweep(start_freq=20, end_freq=20000, duration=5.0, sample_rate=48000, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sweep = amplitude * np.sin(2 * np.pi * t * (start_freq + (end_freq - start_freq) * t / (2 * duration)))
    return sweep

def generate_white_noise(duration=5.0, sample_rate=48000, amplitude=0.5):
    samples = int(sample_rate * duration)
    return amplitude * np.random.normal(0, 1, samples)

def generate_grey_noise(duration=5.0, sample_rate=48000, amplitude=0.5):
    white = generate_white_noise(duration, sample_rate, amplitude)
    # Apply equal-loudness contour weighting (simplified)
    freqs = np.fft.rfftfreq(len(white), 1 / sample_rate)
    fft = np.fft.rfft(white)
    weighting = np.sqrt(1.0 / (freqs + 1))  # Avoid div by 0
    grey_fft = fft * weighting
    grey = np.fft.irfft(grey_fft)
    return np.real(grey[:len(white)])