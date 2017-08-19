from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def transcribe_audio(config,audio):
    client = speech.SpeechClient()

    response = client.recognize(config, audio)
    return str(response.results[0].alternatives[0])
