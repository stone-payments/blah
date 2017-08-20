import io
import os
import urllib.request
import subprocess
import uuid

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def decode(speech_info):
    if os.path.isfile(speech_info):
        return decode_from_local_path(speech_info)
    else:
        return decode_from_url(speech_info)

def decode_from_url(speech_link):
    #TODO implement random file name
    unique_filename = str(uuid.uuid4())
    urllib.request.urlretrieve(speech_link, '/tmp/{}.mp3'.format(unique_filename))
    subprocess.call(['ffmpeg', '-i', '/tmp/{}.mp3'.format(unique_filename), '/tmp/{}.wav'.format(unique_filename)])

    return decode_from_local_path('/tmp/{}.wav'.format(unique_filename))
def decode_from_local_path(speech_local_path):
    with io.open(speech_local_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='pt-BR')
    return (config, audio)
