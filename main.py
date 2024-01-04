from gtts import gTTS
import os
import pygame
from langchain.llms import Ollama
import speech_recognition as sr

#safely deleted all files if there was an error running last time
for mp3_file in os.listdir("mp3_files"):
    if mp3_file.endswith(".mp3"):
        mp3_file_path = os.path.join("mp3_files", mp3_file)
        os.remove(mp3_file_path)

def play(file_path):
    #play mp3s with the pygame mixer
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error while playing {file_path}: {e}")

    finally:
        pygame.mixer.music.stop()

def generate_mp3(output_folder):
    # For every line in output generate an mp3 file
    with open("output.txt", "r", encoding="utf-8") as input_file:
        for line_number, line in enumerate(input_file):
            line = line.strip()

            # Skip empty lines
            if line == "":
                continue

            voice = "en-US-EricNeural"
            mp3_file_path = os.path.join(output_folder, f"output_{line_number+10}.mp3")
            command = f'edge-tts --voice "{voice}" --text "{line}" --write-media "{mp3_file_path}"'
            os.system(command)
            print(f"Generated MP3 for line {line_number}: {mp3_file_path}")

def speak():

    output_folder = "mp3_files"

    #generate mp3 file for tts
    generate_mp3(output_folder)

    try:
        #play every mp3 file
        mp3_files = [file for file in os.listdir(output_folder) if file.endswith(".mp3")]

        mp3_files.sort()
        print(mp3_files)

        for mp3_file in mp3_files:
            mp3_file_path = os.path.join(output_folder, mp3_file)
            play(mp3_file_path)

        pygame.mixer.quit()

    except Exception as e:
        print(f"Error while playing: {e}")

    finally:
        #delete all played mp3 files
        for mp3_file in os.listdir(output_folder):
            if mp3_file.endswith(".mp3"):
                mp3_file_path = os.path.join(output_folder, mp3_file)
                os.remove(mp3_file_path)

def take_command():

    #recognize the command with the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en')

    except Exception as e:
        print(e)
        return ""
    
    return query

ollama = Ollama(base_url='http://localhost:11434', model='llama2') #change model as needed

while True:

    pygame.init()
    pygame.mixer.init()

    #recognize command
    query = take_command()
    print("Command: "+query)

    #send command to ai (e.g. llama2)
    text_ollama = ollama(query)
    
    with open("output.txt", "w", encoding="utf-8") as output_file:
        sentences = text_ollama.split(". ")
        for sentence in sentences:
            output_file.write(sentence.strip() + "\n")

    #read out the response from the ai
    speak()