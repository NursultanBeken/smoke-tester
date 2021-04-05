import pytest
from smoke.smoke_test import fetch


# def test_response_status_ok():
#     """ test returned OK response status from get method """

#     request = fetch('https://httpbin.org/status/200', 3)
#     result = stats (request)
#     assert result['response_status'] == "OK"
    
#     request = fetch('https://httpbin.org/status/201', 3)
#     result = stats (request)
#     assert result['response_status'] == "OK"

#     request = fetch('https://httpbin.org/status/298', 3)
#     result = stats (request)
#     assert result['response_status'] == "OK"

#     for item in range(200, 299):
#         url = 'https://httpbin.org/status/' + str(item)
#         request = fetch(url, 3)
#         result = stats (request)
#         assert result['response_status'] == "OK"


# def test_response_status_fail():
    # """ test returned FAILED response status from get method """

    # request = fetch('https://httpbin.org/status/299', 3)
    # result = stats (request)
    # assert result['response_status'] == "FAILED"
    
    # request = fetch('https://httpbin.org/status/404', 3)
    # result = stats (request)
    # assert result['response_status'] == "FAILED"

    # request = fetch('https://httpbin.org/status/503', 3)
    # result = stats (request)
    # assert result['response_status'] == "FAILED"

    # request = fetch('https://httpbin.oaDGHADrg/status/503', 3)
    # result = stats (request)
    # assert result['response_status'] == "FAILED"

    # request = fetch('https://http', 3)
    # result = stats (request)
    # assert result['response_status'] == "FAILED"

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
    result = fetch('https://httpbin.oaDGHADrg/status/200', 3)
    assert result['response_code'] == 408      