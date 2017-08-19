# [START def_transcribe_file]
def transcribe_audio(config,audio):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_sync_response]
    response = client.recognize(config, audio)
    # [END migration_sync_request]
    return str(response.results[0].alternatives[0])
    # [END migration_sync_response]
# [END def_transcribe_file]
