import numpy as np
import matplotlib.pyplot as plt

# Function to generate a pseudo-random noise (PN) sequence
def generate_pn_sequence(length, seed=0):
    np.random.seed(seed)
    return np.random.choice([1, -1], size=length)

# Function to modulate the message using DSSS
def dsss_modulate(message, pn_sequence):
    return message * pn_sequence

# Function to demodulate the DSSS signal
def dsss_demodulate(dsss_signal, pn_sequence):
    return dsss_signal * pn_sequence

# Generate a sample message signal
message_length = 100
message = np.random.choice([1, -1], size=message_length)

# Generate a PN sequence
pn_sequence = generate_pn_sequence(message_length, seed=42)

# Modulate the message using DSSS
dsss_signal = dsss_modulate(message, pn_sequence)

# Demodulate the DSSS signal
demodulated_signal = dsss_demodulate(dsss_signal, pn_sequence)

# Plot the original message, PN sequence, DSSS signal, and demodulated signal
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.stem(message)
plt.title('Original Message')

plt.subplot(4, 1, 2)
plt.stem(pn_sequence)
plt.title('PN Sequence')

plt.subplot(4, 1, 3)
plt.stem(dsss_signal)
plt.title('DSSS Signal')

plt.subplot(4, 1, 4)
plt.stem(demodulated_signal)
plt.title('Demodulated Signal')

plt.tight_layout()

# Save the figure as an image file
plt.savefig('dsss_signal.png')

# Display the plot
plt.show()

# Verify that the demodulated signal matches the original message
print("Original Message:    ", message)
print("Demodulated Signal: ", demodulated_signal)
