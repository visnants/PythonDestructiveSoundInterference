import numpy as np
import sounddevice as sd

# This script generates a sine wave according to the settings below.
# Afterwards, it gets inverted, playing the normal wave on the left side, and the inverted wave on the right side.


# Settings
frequency = 440.0
duration = 5.0
sample_rate = 44100
volume = 0.5


# Time array
t = np.linspace(
    0,
    duration,
    int(sample_rate * duration),
    endpoint=False
)


# Left channel
left = volume * np.sin(2 * np.pi * frequency * t)

# Right channel (inverted)
right = -left


# Stereo signal
# shape = (samples, 2)
stereo_audio = np.column_stack((left, right))

# Play
print("Playing...")
sd.play(stereo_audio, sample_rate)
sd.wait()

print("Done")