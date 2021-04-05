import click
import sys
import json
from typing import TextIO
from .smoke_test import smoke, stats

@click.command()
@click.option("--requests", "-r", default=1, help="Number of requests")
@click.option("--json-file", "-j", default=None, help="Path to output json file")
@click.option("--timeout", "-t", default=5, help="Stop waiting for a response after a given number of seconds")
@click.argument("url")
def cli(requests, json_file, timeout, url):
    output_file = None
    if json_file:
        try:
            output_file = open(json_file, "w")
        except:
            print(f"Unable to open file {json_file}")
            sys.exit(1)
    request_dicts = smoke(url, requests, timeout)
    results = stats(request_dicts)
    display(url, results, output_file)

def display(url, results, json_file):
    if json_file:
        # Write to a file
        json.dump(
            {
                "endpoint": url,
                "response_status": results['response_status'],
                # "response_code": results['response_code'],
                "avg_response_time": results['avg_response_time'],
                "successful_requests": results['successful_requests'],
                "failed_requests": results['failed_requests']
            },
            json_file,
        )
        json_file.close()
        print(".... Done!")
    else:
        # Print to screen
        print(".... Done!")
        print("--- Results ---")
        print(f"Tested endpoint         \t{url}")
        print(f"Smoke test result status\t{results['response_status']}")
        # print(f"Response code           \t{results['response_code']}")
        print(f"Average response time   \t{results['avg_response_time']}s")
        print(f"Successful Requests      \t{results['successful_requests']}")
        print(f"Failed Requests         \t{results['failed_requests']}")        


if __name__ == '__main__':
    cli()