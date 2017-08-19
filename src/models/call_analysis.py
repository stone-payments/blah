from mongoengine import Document, StringField, DictField

class CallAnalysis(Document):
    call = ReferenceField(Call)
    provider = StringField()
    result = DictField()