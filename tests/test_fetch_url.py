import pytest
from smoke.smoke_test import fetch


def test_respose_code():
    """ test returned response code from get method """
    for item in range(200, 301):
        url = 'https://httpbin.org/status/' + str(item)
        result = fetch(url, 3)
        assert result['response_code'] == item
    
    result = fetch('https://nbekenov.com', 3)
    assert result['response_code'] == 200    

    # test redirect to 404
    result = fetch('https://httpbin.org/status/301', 3)
    assert result['response_code'] == 404

    # test successfull response
    result = fetch('https://httpbin.org/status/200', 3)
    assert result['response_code'] == 200

    # test ConnectionError
    result = fetch('https://http', 3)
    assert result['response_code'] == 503
    
    # test Timeout
    result = fetch('https://httpbin.org/status/503', 3)
    assert result['response_code'] == 503      