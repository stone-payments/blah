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
    
    sentiment_result["simplified"] = get_simplified_analisys(sentiment_result)

    return sentiment_result


def get_simplified_analisys(sentiment_result):
    score = sentiment_result["score"]*100
    magnitude = sentiment_result["magnitude"]*100

    balanced_score = score*magnitude    
    print(balanced_score)

    if (balanced_score >= -15 and balanced_score < 15):
        return "neutral"
    elif(balanced_score >= 15 and balanced_score < 40):
        return "positive"
    elif(balanced_score >= 40):
        return "very positive"
    elif (balanced_score >= -40 and balanced_score < -15):
        return "negative"
    elif (balanced_score < -40):
        return "very negative"
        


