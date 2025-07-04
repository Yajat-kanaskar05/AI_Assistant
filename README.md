# Jarvis AI Assistant

A voice-controlled AI assistant that can perform various tasks through voice commands.

## Features

- Voice activation using the wake word "Jarvis"
- Opens websites (YouTube, Google, Stack Overflow)
- Play music from YouTube using voice commands
- Voice feedback for commands
- Continuous listening mode

## OpenAI API Key (for AI Assistant Feature)
-To enable the AI assistant features powered by OpenAI

## Requirements

- Python 3.x
- speech_recognition
- pyttsx3
- webbrowser (built-in)

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install speech_recognition pyttsx3
```

## Usage

Run the main script:
```bash
python main.py
```

1. Wait for "Initializing Jarvis"
2. Say "Jarvis" to activate
3. After activation, give commands like:
   - "Open YouTube"
   - "Open Google"
   - "Open Stack Overflow"
   - "Play [song name]" 

## Music Playback
The assistant can play music from YouTube. Simply say "Play" followed by the song name. Available songs can be configured by the person preference in musiclib.py file.



