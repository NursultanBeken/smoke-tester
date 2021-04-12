"""Mongo data models."""

from mongoengine.fields import (Document, StringField, DateTimeField,
                                ListField, IntField, EmbeddedDocument,
                                EmbeddedDocumentListField, BooleanField,
                                DictField, FloatField, EmbeddedDocumentField)

class Endpoints(Document):
    """ URLs that need to be tested 
    
    Attributes:
        name (StringField): Endpoint name
        url (StringField): Endpoint URL address which will be tested
        num_requests (IntField): Number of requests.
        response_timeout (IntField): Stop waiting for a response after a given number of seconds
    """
    name = StringField(max_length=120, required=True)
    url = StringField(required=True)
    num_requests = IntField()
    response_timeout = IntField()

class SmokeTestResults(Document):
    """ Smoke test results """
    name = StringField(max_length=120, required=True)
    url = StringField(required=True)
    response_status = StringField(required=True)
    avg_response_time = FloatField()