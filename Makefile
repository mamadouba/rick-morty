SHELL := /bin/bash

initdb:
	poetry run rick_morty/scripts/db.py 

runserver:
	poetry run uvicorn --host 0.0.0.0 --port 8001 rick_morty.main:app

test:
	poetry run pytest tests

createdb:
	docker run --name postgres -p 5432:5432 \
	-e POSTGRES_USER=test \
	-e POSTGRES_PASSWORD=test \
	-e POSTGRES_DB=test -d postgres:latest

build:
	docker build . -t rick-morty 

run:
	docker run -d --name rick-morty -p 8000:8000 rick-morty 
