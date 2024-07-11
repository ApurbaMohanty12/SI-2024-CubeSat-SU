import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Generate a sample AM signal
fs = 1000  # Sampling frequency
t = np.arange(0, 1.0, 1.0/fs)  # Time vector

carrier_freq = 100  # Carrier frequency in Hz
mod_freq = 5  # Modulating frequency in Hz
mod_index = 0.5  # Modulation index

carrier = np.cos(2 * np.pi * carrier_freq * t)
modulating_signal = 1 + mod_index * np.cos(2 * np.pi * mod_freq * t)
am_signal = carrier * modulating_signal

# Demodulation (envelope detection)
demodulated_signal = np.abs(am_signal)

# Low-pass RC filter design using butterworth filter
def rc_low_pass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

cutoff_freq = 10  # Cutoff frequency of the RC filter in Hz
filtered_signal = rc_low_pass_filter(demodulated_signal, cutoff_freq, fs)

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, modulating_signal)
plt.title('Modulating Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 2)
plt.plot(t, carrier)
plt.title('Carrier Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 3)
plt.plot(t, am_signal)
plt.title('AM Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 4)
plt.plot(t, demodulated_signal, label='Demodulated Signal')
plt.plot(t, filtered_signal, label='Filtered Signal')
plt.title('Demodulated and Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('demodulated_and_filtered_signal.png')

# Display the plot (optional)
# plt.show()
