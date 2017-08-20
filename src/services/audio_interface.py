import io
import os
import urllib.request
import subprocess

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
    urllib.request.urlretrieve(speech_link, '/tmp/foo.mp3')
    subprocess.call(['ffmpeg', '-i', '/tmp/foo.mp3', '/tmp/foo.wav'])

    return decode_from_local_path('/tmp/foo.wav')
def decode_from_local_path(speech_local_path):
    with io.open(speech_local_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='pt-BR')
    return (config, audio)
