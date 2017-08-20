from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from sanic.response import text

async def rec_message(request):
    print(str(request))
    response = VoiceResponse()
    response.say("Deixe sua mensagem.")
    response.record(maxLength="30")
    response.hangup()
    return text(str(response))
