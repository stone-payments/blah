# [START import_libraries]
import argparse
import speech_to_text
import text_to_sentiment
import audio_interface
from google.cloud import speech
# [END import_libraries]
# [START def_transcribe_file]
def transcribe_file(speech_info):

    client = speech.SpeechClient()

    decoded_audio = audio_interface.decode(speech_info)
    response = speech_to_text.transcribe_audio(decoded_audio[0],decoded_audio[1])
    annotations = text_to_sentiment.analyze(response)
    sentiment_result = text_to_sentiment.get_result(annotations)
    
    print ("Score: ", sentiment_result['score'])
    print ("Magnitude: ", sentiment_result['magnitude'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='FilePath or Link for audio file to be recognized')
    args = parser.parse_args()
    transcribe_file(args.path)



