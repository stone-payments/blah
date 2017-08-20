from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from sanic.response import text

async def rec_message(request):
    print(str(request))
    response = VoiceResponse()
    response.say("Hello Hello Hello Hello Hello Hello.")
    response.record(maxLength="30", action='/twilio-record')
    response.hangup()
    return text(str(response))

async def twilio_recording(request):
    recording_url = request.values.get('RecordingUrl', None)
    resp = VoiceResponse()
    resp.say('Goodbye')

    return text(str(resp))