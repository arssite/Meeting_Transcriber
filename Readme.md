
# 🎙️ Meeting Transcriber (Whisper-based)

A simple Docker-based Python app to convert meeting **video or audio files** into text transcripts using the powerful [Whisper Large](https://huggingface.co/openai/whisper-large) model from Hugging Face.

---

## 📦 Folder Structure

```

meeting-transcriber/
├── Dockerfile
├── docker-compose.yml
├── input.mp4                 # Replace this with your meeting video/audio
├── main.py
├── requirements.txt
├── output/                   # Transcribed text will appear here
│   └── transcript.txt
└── README.md

````

---

## 🚀 How to Run

### 1. 📥 Prerequisites

- Docker
- Docker Compose

Install Docker Desktop from:  
👉 https://www.docker.com/products/docker-desktop/

---

### 2. 📂 Replace Meeting File

Replace the `input.mp4` file with your **meeting video/audio** file.  
Either rename your file to `input.mp4` or update the `main.py` script.

---

### 3. 🧱 Build and Run the App

```bash
docker-compose up --build
````

This will:

* Convert the video/audio to WAV format
* Load Whisper Large model
* Transcribe the audio
* Save the result to `output/transcript.txt`

---

### 4. ▶️ Re-run Transcription (Next Time)

```bash
docker-compose up
```

---

### 5. 📄 Output

Check the transcribed text at:

```
output/transcript.txt
```

---

## 🧠 Tech Used

| Component        | Tool                        |
| ---------------- | --------------------------- |
| Model            | Whisper Large (HuggingFace) |
| Framework        | Python                      |
| Audio Handling   | Pydub + Torchaudio          |
| Containerization | Docker + Docker Compose     |

---

## 📝 Notes

* If you're running this on **Windows**, ensure Docker Desktop is installed and WSL2 is enabled.
* This app uses `pydub` which requires `ffmpeg` — it is already included inside the container.

---

