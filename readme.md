# Smoke test engine

What we want to test and how:
 - Check response status code
 - Check that response time is below a threshold
 - Reposnse body check


### Requirements to the tool:

1. should support cli
2. should support config file with the list of endpoints
3. GET request
4. POST request with some data
5. assert response code
6. assert response body
7. create report
8. return report in json file
9. flag to show how many times to try
10. add logging
11. add max retries or max time to wait for response
12. Authentication
13. Check that response time is below a threshold
14. Multithreaded test-running


### Usage
Example execute:
```
python -m smoke.cli https://httpbin.org/status/200 -t 2 -r 3 -j output.json
```
