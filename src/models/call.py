from mongoengine import Document, StringField, DictField

class Call(Document):    
    file_hash = StringField(required=True)    
    file_uri = StringField()
    duration = StringField()   
    metadata = DictField()