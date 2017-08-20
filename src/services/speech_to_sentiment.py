from google.cloud import speech

from services import speech_to_text
from services import text_to_sentiment
from services import audio_interface

def transcribe_file(speech_info):
    client = speech.SpeechClient()
    config, audio = audio_interface.decode(speech_info)
    response = speech_to_text.transcribe_audio(config, audio)
    annotations = text_to_sentiment.analyze(response)
    sentiment_result = text_to_sentiment.get_result(annotations)

    sentiment_result["simplified"] = get_simplified_analisys(sentiment_result)

    sentiment_result['transcription'] = response

    return sentiment_result


def get_simplified_analisys(sentiment_result):
    score = sentiment_result["score"]*10
    magnitude = sentiment_result["magnitude"]*10

    balanced_score = score*magnitude

    if (balanced_score >= -12 and balanced_score < 12):
        return "neutral"
    elif(balanced_score >= 12 and balanced_score < 37):
        return "positive"
    elif(balanced_score >= 37):
        return "very positive"
    elif (balanced_score >= -37 and balanced_score < -12):
        return "negative"
    elif (balanced_score < -37):
        return "very negative"
