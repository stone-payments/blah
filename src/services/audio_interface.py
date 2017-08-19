# [START import_libraries]
import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# [END import_libraries]

def decode (speech_info):
    if os.path.isfile(speech_info):
        return decode_from_local_path(speech_info)
    else:
         return decode_from_url(speech_info)   

def decode_from_url(speech_link):
    raise Exception("Via URL not implemented")

def decode_from_local_path(speech_local_path):
    # [START migration_audio_config_file]
    with io.open(speech_local_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='pt-BR')
    # [END migration_audio_config_file]
    return (config,audio)
