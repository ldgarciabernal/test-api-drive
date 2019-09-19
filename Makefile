venv:
	virtualenv -p python3 venv

init:
	pip install -r requirements.txt

test:
	python -m test -h