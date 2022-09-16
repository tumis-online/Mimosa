# Build upon RASA GitHub Makefile: https://github.com/RasaHQ/rasa/blob/main/Makefile

.PHONY: clean test lint init docs build-docker

JOBS ?= 1

help:
	@echo "make"
	@echo "    clean"
	@echo "        Remove Python/build artifacts."
	@echo "    install"
	@echo "        Install by starting docker containers and start pipeline loop."
	@echo "    lint"
	@echo "        Lint code with flake8, and check if black formatter should be applied."
	@echo "    lint-docstrings"
	@echo "        Check docstring conventions in changed files."
	@echo "    test"
	@echo "        Run pytest on tests/."
	@echo "        Use the JOBS environment variable to configure number of workers (default: 1)."
	@echo "    docs"
	@echo "        Build the docs locally."
	@echo "    release"
	@echo "        Prepare a release."
	@echo "    build-docker"
	@echo "        Build Docker images for the application via docker-compose file."
	@echo "    stop-containers"
	@echo "        Stop the containers."

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf .mypy_cache/
	rm -rf dist/
	rm -rf docs/build
	rm -rf docs/.docusaurus

install:
	poetry run python -m pip install -U pip
	poetry install

install-docs:
	cd docs/ && yarn install

lint:
     # Ignore docstring errors when running on the entire project
	poetry run flake8 rasa tests --extend-ignore D
	poetry run black --check rasa tests
	make lint-docstrings

lint-docstrings:
# Lint docstrings only against the the diff to avoid too many errors.
# Check only production code. Ignore other flake errors which are captured by `lint`
# Diff of committed changes (shows only changes introduced by your branch
ifneq ($(strip $(BRANCH)),)
	git diff $(BRANCH)...HEAD -- rasa | poetry run flake8 --select D --diff
endif

	# Diff of uncommitted changes for running locally
	git diff HEAD -- rasa | poetry run flake8 --select D --diff

test: clean
	# OMP_NUM_THREADS can improve overall performance using one thread by process (on tensorflow), avoiding overload
	# TF_CPP_MIN_LOG_LEVEL=2 sets C code log level for tensorflow to error suppressing lower log events
	OMP_NUM_THREADS=1 TF_CPP_MIN_LOG_LEVEL=2 poetry run pytest tests -n $(JOBS) --cov rasa --ignore $(INTEGRATION_TEST_FOLDER)

install-docs:
	cd docs/ && npm install

docs:
	cd docs/ && npm run build

livedocs:
	cd docs/ && poetry run npm run start

release:
	poetry run python scripts/release.py

build-docker:
	# make -f NeMo/Makefile build-docker
	make -f RASA/Makefile build-docker
	@echo "Starting Docker containers via Docker Compose..."
	export IMAGE_NAME=rasa && \
	docker compose --project-directory . --env-file .env --file docker-compose.yml up

stop-containers:
	@echo "Removing Docker containers via Docker Compose..."
	docker compose --project-directory . --env-file .env --file docker/docker-compose.yml down