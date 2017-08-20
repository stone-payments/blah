from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from sanic.response import text

async def rec_message(request):
    print(str(request))
    resp = VoiceResponse()
    print('=============================================')
    resp.say("Hello Hello Hello Hello Hello Hello.")

    resp.record()
    return text(str(resp))

async def twilio_recording(request):
    recording_url = request.values.get('RecordingUrl', None)
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(recording_url)
    resp = VoiceResponse()
    resp.say('Listein')
    res.play(recording_url)
    resp.say('Goodbye')
    return text(str(resp))