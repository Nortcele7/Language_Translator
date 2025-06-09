#1. Importing the required modules

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os 
import asyncio 

#2. Creating recognizer and microphone instances

recog1 = spr.Recognizer()
# recog1 is an instance of Recognizer class that is used to recognize the audio
# given from microphone

mc = spr.Microphone()
# mc is an instance of microphone class that is used to accept audio which is to be recognized by recognizer



def recognize_speech(recog, source):
    recog.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog.listen(source)
    recognized_text = recog.recognize_google(audio)
    return recognized_text

async def translate_and_speak():
    translator = Translator()
    lang1 = "en"
    lang2 = "es"

    with mc as source:
        print("Speak Hello to start the translation")
        text = recognize_speech(recog1, source)

    if text and 'hello' in text:
        with mc as source:
            print("Speak to translate: ")
            spoken_sentence = recognize_speech(recog1, source)
    
        if spoken_sentence:
            print(f"Translating {spoken_sentence}from {lang1} to {lang2} ......\n")

            translated = await translator.translate(spoken_sentence, src=lang1, dest=lang2)

            translated_text = translated.text

            speak = gTTS(text=translated_text, lang=lang2, slow=False)

            speak.save("captured_voice.mp3")

            os.system("start captured_voice.mp3")

        else:
            print("Spoken snetence not recognized")

    else:
        print("Hello was not recognized \n Speak hello again to initiate the translation")



asyncio.run(translate_and_speak())
