import sys
import json
import pprint
from topolibrary.settings import MongoSettings
from topolibrary.model import Endpoints, SmokeTestResults
import pytest
from smoke.mongo_work import process_mongo_data, find_endpoint_by_url


DATABASE_NAME = "topograph"
DATABASE_HOST = "localhost"
DATABASE_PORT = 27017

test_urls = [
    {
        "name": "test301",
        "url": "https://httpbin.org/status/301"
    },
    {
        "name": "test200",
        "url": "https://httpbin.org/status/200"
    },
    {
        "name": "test3",
        "url": "https://httpbin.org"
    },
    {
        "name": "test404",
        "url": "https://httpbin.org/status/404"
    },
    {
        "name": "test503",
        "url": "https://httpbin.org/status/503"
    }, 
    {
        "name": "test6",
        "url": "https://httpbindsdsdsd.org"
    }               
]

def create_test_data():
    mongo_settings = MongoSettings(host=DATABASE_HOST)
    mongo_client = mongo_settings.connect()

    for item in test_urls:
        enpoint_obj = Endpoints(name = item["name"], url = item["url"])
        mongo_settings.save(enpoint_obj)
    
    mongo_settings.close()

def test_mongo_integration():

    mongo_settings = MongoSettings(host=DATABASE_HOST)
    mongo_client = mongo_settings.connect()

    for item in test_urls:
        enpoint_obj = Endpoints(name = item["name"], url = item["url"])
        mongo_settings.save(enpoint_obj)
    mongo_settings.close()
    
    process_mongo_data()   

    mongo_settings = MongoSettings(host=DATABASE_HOST)
    mongo_client = mongo_settings.connect()    
    for item in test_urls:
        endpoint = find_endpoint_by_url(enpoint_url = item["url"])
        if endpoint.name == "test200":
            assert endpoint.response_status == "OK"

    mongo_settings.close()

if __name__ == "__main__":
    create_test_data()
    test_mongo_integration()