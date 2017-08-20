from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from sanic.response import json


async def rec_message(request):
    print(str(request))
    response = VoiceResponse()
    response.say("Deixe sua mensagem.")
    response.record()
    response.hangup()
    return str(response)