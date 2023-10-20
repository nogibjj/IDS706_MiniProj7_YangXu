install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv --nbval --cov=script --cov=mini_proj_7 **/test_*.py

format:
	black *.py **/*.py

lint:
	ruff check *.py **/*.py

all: install lint format test
