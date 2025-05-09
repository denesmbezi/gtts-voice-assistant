import io
import pygame
from gtts import gTTS


def speak(text):
    with io.BytesIO() as file:
        gTTS(text=text, lang='en').write_to_fp(file)  # Fixed bug here
        file.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


if __name__ == "__main__":
    print("What should I say?")
    text = input(" >> ")
    speak(text)
