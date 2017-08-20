from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from sanic.response import text

async def rec_message(request):
    print(str(request))
    response = VoiceResponse()
    print('=============================================')
    response.say("Hello Hello Hello Hello Hello Hello.")
    response.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    response.record(maxLength="30", action='/twilio-record')
    return text(str(response))

async def twilio_recording(request):
    recording_url = request.values.get('RecordingUrl', None)
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(recording_url)
    resp = VoiceResponse()
    resp.say('Goodbye')
    resp.hangup()
    return text(str(resp))