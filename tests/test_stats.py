import pytest
from smoke.smoke_test import smoke, stats


def test_response_status_ok():
    url = 'https://httpbin.org/status/200'
    requests = 5
    timeout = 3
    request_dicts = smoke(url, requests, timeout)
    results = stats(request_dicts)
    assert results["response_status"] == "OK"

def test_response_status_fail():
    url = 'https://httpbinwqw.org/status/404'
    requests = 5
    timeout = 3
    request_dicts = smoke(url, requests, timeout)
    results = stats(request_dicts)
    assert results["response_status"] == "FAILED"