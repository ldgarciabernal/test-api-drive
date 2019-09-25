venv:
	virtualenv -p python3 venv

packages:
	pip install -r requirements.txt

tests:
	python -m test -h

up:
	source venv/bin/activate

down:
	deactivate

run:
	python src/main.pỳ