SRC := /Users/nbekenov/git_repos/smoke-tester

setup:
	# Create python virtualenv & source it
	# source ~/.devops/bin/activate
	python3 -m venv ~/.env

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W ${SRC}/smoke/*.py

test:
	python -m pytest -s -vvv tests/ --junitxml=reports/unit.xml

all: lint test