import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Version of microphoneVisualizer that uses sounddevice. Problem: it doesn't look as right or smooth

# Audio settings
CHUNK = 1024
RATE = 44100

# Shared audio buffer
audio_data = np.zeros(CHUNK)

# Audio callback
def audio_callback(indata, frames, time, status):
    global audio_data
    audio_data = indata[:, 0]

# Start microphone stream
stream = sd.InputStream(
    channels=1,
    samplerate=RATE,
    blocksize=CHUNK,
    dtype='int16',
    callback=audio_callback
)
stream.start()

# Create plot
fig, ax = plt.subplots()
x = np.arange(CHUNK)

line, = ax.plot(x, audio_data)

ax.set_ylim(-32768, 32767)
ax.set_xlim(0, CHUNK)
ax.set_title("Microphone Audio Visualizer")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")

# Animation update
def update(frame):
    line.set_ydata(audio_data)
    return line,

ani = FuncAnimation(fig, update, interval=20, blit=True)

plt.show()

# Cleanup
stream.stop()
stream.close()