# Smoke test engine

[![CircleCI](https://circleci.com/gh/NursultanBeken/smoke-tester.svg?style=svg)](https://circleci.com/gh/NursultanBeken/smoke-tester)

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
```bash
python -m smoke.cli https://httpbin.org/status/200 -t 2 -r 3 -j output.json

# run mongo in docker contrainer
docker container run --name smoke-mongo -d --rm -p 27017:27017 mongo:4.4.4
python -m smoke.mongo_client
```

### TO_DO: 
* pull URL from Mongo DB
* write result back to DB
* set a cron job to run the smoke-test
* dockerize the app


## two collections:

1. url endpoints
2. results from testing

topograph/cicd - import mongodb settings 