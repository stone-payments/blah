from twilio.twiml.voice_response import Play, VoiceResponse
from twilio.rest import Client
from sanic.response import text, html

async def rec_message(request):
    response = VoiceResponse()
    response.say('Recording...', voice='woman')
    # response.record(recording_status_callback='/twilio-record')
    response.record(recording_status_callback='https://requestb.in/12vdrvo1')
    return html(str(response))

async def twilio_recording(request):
    print(request)
    recording_url = request.values.get('RecordingUrl', None)
    print(recording_url)
    return text('ok')