import os
from pydub import AudioSegment
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import torchaudio

# Paths
video_path = "input.mp4"
wav_path = "converted.wav"

# Convert video to wav
audio = AudioSegment.from_file(video_path)
audio = audio.set_frame_rate(16000).set_channels(1)
audio.export(wav_path, format="wav")

# Load Whisper
processor = WhisperProcessor.from_pretrained("openai/whisper-large")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")
model.eval()
if torch.cuda.is_available():
    model = model.to("cuda")

# Load audio
waveform, rate = torchaudio.load(wav_path)
inputs = processor(waveform.squeeze(), sampling_rate=rate, return_tensors="pt")

# Move to GPU if available
if torch.cuda.is_available():
    inputs = {k: v.to("cuda") for k, v in inputs.items()}

# Transcribe
with torch.no_grad():
    generated_ids = model.generate(inputs["input_features"])
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

# Save output
os.makedirs("output", exist_ok=True)
with open("output/transcript.txt", "w") as f:
    f.write(transcription)

print("\n📝 Transcription complete! Check output/transcript.txt\n")