import mongoengine
import hashlib

from models.call import CallAnalysis
from models.call import Call
from services.speech_to_sentiment import transcribe_file

_PROVIDERS = ['speech_to_sentiment']

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def call_already_exists(file_hash):
    calls = Call.objects(file_hash=file_hash)
    return calls.first()

def make_call(file_uri, file_hash, metadata):
    call = Call(
            file_hash=file_hash,
            file_uri=file_uri,
            metadata=metadata
        )
    messages = []
    try:
        call.save()
    except mongoengine.errors.ValidationError as e:
        for key in e.errors:
            messages.append('{} - {}'.format(key, e.errors.get(key)))
        call = None        
    return call, messages

def get_analysis_for_call(call):
    return CallAnalysis.objects(call=call)
    
def make_analysis(call, provider):
    if provider == 'speech_to_sentiment':
        analysis = transcribe_file(call.file_uri)
        return save_analysis(call, provider, analysis)

def save_analysis(call, provider, result):
    call_analysis = CallAnalysis(
        call=call,
        provider=provider,
        result=result
    )
    call_analysis.save()
    return call_analysis

def add_call(file_uri, metadata):
    file_hash = md5(file_uri)

    call = call_already_exists(file_hash)
    messages = []
    analysis = []
    if not call:
        call, messages = make_call(file_uri, file_hash, metadata)
        for provider in _PROVIDERS:
            al = make_analysis(call, provider)
            analysis.append(al)
    else:
        analysis = get_analysis_for_call(call)
    return (call, analysis, messages)