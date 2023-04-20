PYTHON := python
SHELL := /bin/bash

.PHONY: all
all: deps db-up run

.PHONY: deps
deps:
	pip install -r app/requirements.txt

.PHONY: run
run:
	source .env;
	$(PYTHON) app/main.py;

.PHONY: db-up
db-up:
	docker-compose up -d

.PHONY: db-down
db-down:
	docker-compose down