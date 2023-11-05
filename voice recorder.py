import pyaudio
import wave

# Define the audio settings
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono recording
RATE = 44100  # Sample rate
CHUNK = 1024  # Number of frames per buffer
RECORD_SECONDS = 5  # Duration of recording
OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Create an input stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record audio
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved as {OUTPUT_FILENAME}")
