import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os
import asyncio


lang1 = input("Enter the source language: ")
lang2 = input("Enter the destination language: ")

recog1 = spr.Recognizer()
mc = spr.Microphone()


def convert_audio_to_text(recog, source):
    recog.adjust_for_ambient_noise(source, duration=0.2)

    audio = recog.listen(source)

    recognized_text = recog.recognize_google(audio)

    return recognized_text


async def translate_and_speak():

    translator = Translator()

    with mc as source:
        print("Speak Hello to initiate the translator")
        text = convert_audio_to_text(recog1, source)

    if text and 'hello' in text:

        print(f"Speak to translate from {lang1} to {lang2}")

        with mc as source:
            spoken_text = convert_audio_to_text(recog1, source)

        if spoken_text:
            translated = await translator.translate(spoken_text, src=lang1, dest=lang2)
            translated_text = translated.text

            print(translated_text)

            speak = gTTS(text=translated_text, lang=lang2, slow=False)

            speak.save('translated.mp3')

            os.system('start translated.mp3')

        else:
            print("Spoken Text not recognized")

    else:
        print("Hello not recognized")

asyncio.run(translate_and_speak())
