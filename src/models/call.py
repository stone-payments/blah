from mongoengine import Document, StringField, DictField, ReferenceField

class Call(Document):
    file_hash = StringField(required=True)
    file_uri = StringField()
    metadata = DictField()

class CallAnalysis(Document):
    call = ReferenceField(Call)
    provider = StringField()
    result = DictField()