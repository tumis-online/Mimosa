# Build upon RASA GitHub Makefile: https://github.com/RasaHQ/rasa/blob/main/Makefile

.PHONY: test build-docker

JOBS ?= 1

RASA_ACTION_SERVER_IMAGE=rasa-action-server
RASA_ACTION_SERVER_TAG=0.2
RASA_NLU_SERVER_IMAGE=rasa-nlu-server
RASA_NLU_SERVER_TAG=0.2
RASA_MODEL_SERVER_IMAGE=rasa-model-server
RASA_MODEL_SERVER_TAG=0.2
RASA_NLU_TRAIN_IMAGE=rasa-nlu-train
RASA_NLU_TRAIN_TAG=0.1

help:
	@echo "make"
	@echo "    test"
	@echo "        Run RASA test"
	@echo "    build-docker"
	@echo "        Build Docker images for the application via docker-compose file."
	@echo "	   train-nlu"
	@echo "	       Starts docker container training RASA NLU and saves model into RASA.models volume."
	@echo "    start-model-server"
	@echo "        Starts RASA model server on port 8080 providing models of RASA.models volume."

test:
	@echo $(pwd)
	@echo "Validating environment and test NLUin RASA test container..."
	docker build . -t rasa-test:latest -f docker/Dockerfile.rasa_test
	docker run -d -v -it --rm rasa-test:latest
	# rasa data validate -vv --config config.yml --data data/ --domain domain/
	# rasa test -vv --config config.yml --domain domain/ --model models/ --nlu data/nlu/ --stories data/stories/ nlu

build-docker:
	echo "Building RASA Action Server Docker Image..."
	docker build . -t ${RASA_ACTION_SERVER_IMAGE}:${RASA_ACTION_SERVER_TAG} \
				   -f docker/Dockerfile.rasa_action_server
	docker build . -t ${RASA_ACTION_SERVER_IMAGE}:${RASA_ACTION_SERVER_TAG} \
               -f docker/Dockerfile.rasa_action_server

train-nlu:
	docker build . -t ${RASA_NLU_TRAIN_IMAGE}:${RASA_NLU_TRAIN_TAG} \
				   -f docker/Dockerfile.rasa_nlu_train
	docker run -d -v RASA.models:/RASA/models ${RASA_NLU_TRAIN_IMAGE}:${RASA_NLU_TRAIN_TAG}

start-model-server:
	docker run -v RASA.models:/RASA/models \
			   -p 8080:80 \
			   ${RASA_MODEL_SERVER_IMAGE}:${RASA_MODEL_SERVER_TAG}
