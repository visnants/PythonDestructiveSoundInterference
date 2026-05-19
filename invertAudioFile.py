import sys
import numpy as np
import sounddevice as sd
import soundfile as sf

# This script receives an audio file, inverts it, and plays the original on the left side, and the inverted on the right side.
#
# Usage:
#     python phase_invert_stereo.py input.wav


def main():
    if len(sys.argv) < 2:
        print("Usage: python phase_invert_stereo.py input.wav")
        sys.exit(1)

    filename = sys.argv[1]

    # Load audio file
    audio, samplerate = sf.read(filename)

    # Convert stereo -> mono if needed
    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    # Create phase-inverted version
    inverted = -audio

    # Build stereo output:
    # Left  = original
    # Right = inverted
    stereo = np.column_stack((audio, inverted))

    print("Playing...")
    print("Left speaker  = original")
    print("Right speaker = phase inverted")

    # Play audio
    sd.play(stereo, samplerate)
    sd.wait()


if __name__ == "__main__":
    main()