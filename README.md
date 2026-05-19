# Python - Physics - Destructive Sound Interference
This project was created as a part of a Physics presentation in which we use the different Python scripts to exemplify how a destructive sound interference works.\
Using two separate speakers, one to each side and pointing to each other, we can have in the middle of them a section where the sound wave is destructive, causing the phenomenon.
The microphone, then, is used to show visually the wave getting destroyed.

`microphoneVisualizer.py` - Shows in realtime using matplotlib the amplitude of the audio gathered by the microphone.\
`audioGenerator.py` - Generates a sine wave according to the settings below. Afterwards, it gets inverted, playing the normal wave on the left side, and the inverted wave on the right side.\
`invertAudioFile.py` - Receives an audio file, inverts it, and plays the original on the left side and the inverted on the right side.
