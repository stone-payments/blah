from mongoengine import Document, StringField, DictField, ReferenceField

class Call(Document):
    file_hash = StringField(required=True)
    file_uri = StringField()
    metadata = DictField()

    def to_json(self):
        return {
            'id': str(self.id),
            'file_hash' : self.file_hash,
            'metadata' : self.metadata
        }

class CallAnalysis(Document):
    call = ReferenceField(Call)
    provider = StringField()
    result = DictField()

    def to_json(self):
        data = {
            'id': str(self.id),
            'provider': self.provider
        }
        if self.provider == 'speech_to_sentiment':
            data['result'] = {
                'magnitude': self.result.get('magnitude'),
                'score': self.result.get('score'),
                'simplified' : self.result.get('simplified'),
                'transcription': self.result.get('transcription')
            }
        return data