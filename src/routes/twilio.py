from twilio.twiml.voice_response import Play, VoiceResponse
from twilio.rest import Client
from sanic.response import text, html
from services.call import add_call

async def rec_message(request):
    response = VoiceResponse()
    response.say('Recording...', voice='woman')
    response.record(recording_status_callback='/twilio-record')
    # response.record(recording_status_callback='https://requestb.in/12vdrvo1')
    return html(str(response))

async def twilio_recording(request):
    recording_url = request.form.get('RecordingUrl', None)
    metadata = {"type": "inbound_call", "provider": "twilio"}
    print(add_call(recording_url, metadata))
    return text('ok')