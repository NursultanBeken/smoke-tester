#!/usr/bin/env python3
"""
simple smoke test engine using requests
"""
import time
import requests
import json
from requests.exceptions import Timeout
from typing import List, Dict
from statistics import mean

def fetch(url, timeout):
    """Make the request and return the results"""
    started_at = time.monotonic()
    status_code = 0
    try:
        response = requests.get(
            url,
            timeout=timeout)
        status_code = response.status_code    
    except Timeout:
        status_code = 408
    except requests.exceptions.ConnectionError as ce:
        status_code = 503
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    request_time = time.monotonic() - started_at
    return { 
            "response_code": status_code,
            "request_time": request_time
            }


def smoke(url, requests, timeout):
    results = []
    for _ in range(requests):
        result = fetch(url, timeout)
        results.append(result)
    return results


def stats(requests: List[Dict]):
    avg_response_time = mean([r["request_time"] for r in requests])
    successful_requests = len([r for r in requests if r["response_code"] in range(200, 299)])
    failed_requests = len([r for r in requests if r["response_code"] not in range(200, 299)])

    response_status = "OK" if successful_requests >= failed_requests else "FAILED"

    return {"response_status": response_status, 
            "successful_requests": successful_requests,
            "failed_requests" : failed_requests,
            "avg_response_time": avg_response_time,
            }    

if __name__=="__main__":
    url = 'https://httpbinwqw.org/status/404'
    results = smoke(url, 3, 2)
    print(f'results = {results}')
    response_status, avg_response_time, successful_requests, failed_requests = stats(results)
    print(f'avg_response_time = {avg_response_time}, response_status = {response_status}, failed_requests = {failed_requests}')
