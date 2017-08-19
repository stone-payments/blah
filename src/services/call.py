import mongoengine
import hashlib

from models.call import CallAnalysis
from models.call import Call
from services.speech_to_sentiment import transcribe_file

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def add_call(file_uri, metadata):
    file_hash = md5(file_uri)
    call = Call(
        file_hash=file_hash,
        file_uri=file_uri,
        metadata=metadata
    )
    try:
        call.save()
        out = {}
        for i in call:
            out[i] = str(call[i])
        return {"id": out['id'], "file_hash": file_hash, "analysis": [make_analysis(call)]}
    except mongoengine.errors.ValidationError as e:
        for key in e.errors:
            return [].append('{} - {}'.format(key, e.errors.get(key)))

def make_analysis(call):
    analysis = transcribe_file(call.file_uri)
    return save_analysis(call, 'speech_to_sentiment', analysis)

def save_analysis(call, provider, result):
    call_analysis = CallAnalysis(
        call=call,
        provider=provider,
        result=result
    )

    try:
        call_analysis.save()
        out = {}
        for i in call_analysis:
            if i == 'call':
                continue
            out[i] = str(call_analysis[i])
        return out

    except:
        return {}