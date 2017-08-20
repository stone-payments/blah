from twilio.twiml.voice_response import Play, VoiceResponse
from twilio.rest import Client
from sanic.response import html

async def rec_message(request):
    print(str(request))
    response = VoiceResponse()
    response.say('Recording...', voice='woman')
    response.record()
    return html(str(response))

async def twilio_recording(request):
    recording_url = request.values.get('RecordingUrl', None)
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(recording_url)
    resp = VoiceResponse()
    resp.say('Listein')
    res.play(recording_url)
    resp.say('Goodbye')
    return text(str(resp))