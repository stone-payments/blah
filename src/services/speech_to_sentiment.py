from google.cloud import speech

from services import speech_to_text
from services import text_to_sentiment
from services import audio_interface

def transcribe_file(speech_info):
    client = speech.SpeechClient()

    decoded_audio = audio_interface.decode(speech_info)
    response = speech_to_text.transcribe_audio(decoded_audio[0],decoded_audio[1])
    annotations = text_to_sentiment.analyze(response)
    sentiment_result = text_to_sentiment.get_result(annotations)
    
    return sentiment_result


