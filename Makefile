install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_main.py

format:
	black *.py

lint:
	pylint --disable=R,C main.py

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 432096997023.dkr.ecr.us-east-1.amazonaws.com
	docker build -t ids_group_proj .
	docker tag ids_group_proj:latest 432096997023.dkr.ecr.us-east-1.amazonaws.com/ids_group_proj:latest
	docker push 432096997023.dkr.ecr.us-east-1.amazonaws.com/ids_group_proj:latest

all: install format lint test deploy
