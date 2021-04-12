import sys
import json
import pprint
from topolibrary.settings import MongoSettings
from topolibrary.model import Endpoints, SmokeTestResults
from .smoke_test import smoke, stats

DATABASE_NAME = "topograph"
DATABASE_HOST = "localhost"
DATABASE_PORT = 27017


def get_urls(Document):
    
    url_list = []
    for doc in Document.objects:
        url_list.append(doc.url)
    return url_list  

def list_data(Document):
    for doc in Document.objects:
        print(f' {doc.name} - {doc.url}')


def find_endpoint_by_url(enpoint_url):
    endpoint =  SmokeTestResults.objects(url=enpoint_url).first()
    return endpoint

def checkIfDocExists(enpoint_url):
    if SmokeTestResults.objects(url=enpoint_url):
        print(f'{enpoint_url} exists')
        return True
    else:
        return False    

# def createNewEndpoint(name, url, num_requests, response_timeout):
#     endpoint_obj = Endpoints()
#     endpoint_obj.name = name
#     endpoint_obj.url = url
#     endpoint_obj.num_requests = num_requests
#     endpoint_obj.response_timeout = response_timeout
#     return endpoint_obj


def process_mongo_data():
    # connect to database 
    mongo_settings = MongoSettings(host=DATABASE_HOST)
    mongo_client = mongo_settings.connect()
    print('connected to mongodb')

    # get the list of urls to test
    for doc in Endpoints.objects:
        print(f'Testing URL: {doc.url}')

        num_requests = doc.num_requests if doc.num_requests is not None else 1
        response_timeout  = doc.response_timeout if doc.response_timeout is not None else 5
        
        request_dicts = smoke(doc.url, requests=num_requests, timeout=response_timeout)
        results = stats(request_dicts)
        
        existing_endpoint_obj = find_endpoint_by_url(doc.url)
        # if does not exist, then create a new one
        if existing_endpoint_obj:
            print(f'Endpoint {doc.name} already exists. Updating response status ...')
            existing_endpoint_obj.response_status = results['response_status']
            existing_endpoint_obj.avg_response_time = results['avg_response_time']
            mongo_settings.save(existing_endpoint_obj)
        else:
            print(f'Creating new endpoint {doc.name} ...')
            new_endpoint_obj = SmokeTestResults(name = doc.name)
            new_endpoint_obj.url = doc.url
            new_endpoint_obj.response_status = results['response_status']
            new_endpoint_obj.avg_response_time = results['avg_response_time']
            mongo_settings.save(new_endpoint_obj)
    
    mongo_settings.close()

if __name__ == "__main__":
    process_mongo_data()    