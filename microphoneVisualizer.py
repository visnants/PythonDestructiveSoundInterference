import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This script shows in realtime using matplotlib the amplitude of the audio gathered by the microphone.

# Audio settings
CHUNK = 1024             # Number of audio samples per frame
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100             # Samples per second

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open microphone stream
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

# Create matplotlib figure
fig, ax = plt.subplots()
x = np.arange(0, CHUNK)
line, = ax.plot(x, np.random.rand(CHUNK), lw=2)

# Set plot limits
ax.set_ylim(-10000, 10000) # Values chosen to make the visualization better, technically the true value would be -32,768 to 32,767 (int16 size)
ax.set_xlim(0, CHUNK)
ax.set_title("Microphone Audio Visualizer")
fig.canvas.manager.set_window_title("Microphone Audio Visualizer")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")

# Update function for animation
def update(frame):
    data = stream.read(CHUNK, exception_on_overflow=False)

    # Convert bytes to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Update plot
    line.set_ydata(audio_data)

    return line,

# Animate
ani = FuncAnimation(fig, update, interval=20, blit=True)

plt.show()

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()