install:
	#install
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	#format
	black *.py src/*.py
lint:
	#pylint
	pylint --disable=R,C *.py src/*.py
test:
	#testing
	python3 -m pytest -vv --cov=src --cov=main test_*.py
build:
	#build containers
	docker compose up --build
deploy:
	#deploy
all: install format lint test deploy
