import numpy as np
import matplotlib.pyplot as plt

# Generate a signal
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time vector
f1 = 5  # Frequency of the signal
signal = np.sin(2 * np.pi * f1 * t)  # Signal

# Compute the FFT of the signal
fft_signal = np.fft.fft(signal)

# Frequency domain representation
freqs = np.fft.fftfreq(len(signal)) * fs

# Define the cutoff frequency for the low-pass filter
cutoff_frequency = 20  # Adjust as needed

# Apply the low-pass filter
fft_signal_filtered = fft_signal.copy()
fft_signal_filtered[np.abs(freqs) > cutoff_frequency] = 0

# Compute the inverse FFT to obtain the filtered signal
filtered_signal = np.fft.ifft(fft_signal_filtered)

# Plot the original and filtered signals
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal.real, label='Filtered Signal', color='orange')
plt.title('Filtered Signal (Low-pass)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
