# python-ollama-local

## Overview

This project enables hands-free voice interactions through a local installation of the Llama2 language model. Users can provide voice commands, which are then processed by Llama2 for natural language understanding. The textual responses are converted into speech using the "edge-tts" tool, and the generated audio is played back sequentially.

## Requirements

Ensure you have the following Python libraries and tools installed:

- [ollama](https://github.com/jmorganca/ollama)
- [gtts](https://pypi.org/project/gTTS/): `pip install gtts`
- [pygame](https://pypi.org/project/pygame/): `pip install pygame`
- [langchain](https://pypi.org/project/langchain/): `pip install langchain`
- [speech_recognition](https://pypi.org/project/SpeechRecognition/): `pip install SpeechRecognition`

## Usage

1. **Clone the Repository:**
   ```
   git clone https://github.com/Marvin-VW/python-ollama-local/blob/main/main.py
   cd voice-interaction-project
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   ```
   python voice_interaction.py
   ```

## Features

- Captures voice commands from the microphone.
- Utilizes local Llama2 for natural language processing.
- Converts textual responses to speech using "edge-tts."
- Sequential playback of generated audio files.

## Contribution

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
