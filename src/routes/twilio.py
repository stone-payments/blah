from twilio.twiml.voice_response import Play, VoiceResponse
from twilio.rest import Client
from sanic.response import text

async def rec_message(request):
    print(str(request))
    response = VoiceResponse()
    print('=============================================')

    response.play('https://api.twilio.com/cowbell.mp3', loop=10)

    print(response)

    resp.record()
    return text(str(response))

async def twilio_recording(request):
    recording_url = request.values.get('RecordingUrl', None)
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(recording_url)
    resp = VoiceResponse()
    resp.say('Listein')
    res.play(recording_url)
    resp.say('Goodbye')
    return text(str(resp))