from __future__ import absolute_import, unicode_literals
import os

from mongoengine import connect
from mongoengine.connection import disconnect



class MongoSettings():
    ''' mongop settings '''
    def __init__(self, db_name=None, host=None, port=None):
        self.mongo_user = os.environ.get("MONGO_USER")
        self.mongo_pass = os.environ.get("MONGO_PASS")
        self.mongo_port = port if port is not None else os.environ.get("MONGO_PORT", 27017)
        self.mongo_host = host if host is not None else os.environ.get("MONGO_HOST", "host.docker.internal")
        self.mongo_db = db_name if db_name is not None else os.environ.get("MONGO_DB", "topograph")
        self.host = f"mongodb://{self.mongo_host}:{self.mongo_port}"
        self.client = connect(self.mongo_db, host=self.host, port=self.mongo_port, alias='default', connect=False)

    def connect(self):
        return self.client

    def save(self, document):
        document.save()

    def close(self):
        disconnect()