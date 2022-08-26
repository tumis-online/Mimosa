
.PHONY: build-docker

NEMO_ASR_IMAGE=nemo-asr
NEMO_ASR_TAG=0.1

help:
	@echo "make"
	@echo "    test"
	@echo "        test NeMo environment via pytest."
	@echo "    build-docker"
	@echo "        Build NeMo Docker images."
	@echo "    start-asr-server"
	@echo "        Start ASR Server."
	@echo "    start-tts-server"
	@echo "        Start TTS Server."

test:
	@echo "Running tests in docker container..."
	docker build . -t nemo-test:latest -f ../docker/Dockerfile.nemo_test
	docker run -it --rm --name nemo-test nemo-test:latest

build-docker:
	@echo "Building NeMo Docker Images..."
	docker build . -t ${NEMO_ASR_IMAGE}:${NEMO_ASR_TAG} \
				   -f ../docker/Dockerfile.nemo_asr

start-asr-server:
	@echo "Starting NeMo ASR Server..."
	docker run -d -p 5555:8000 ${NEMO_ASR_IMAGE}:${NEMO_ASR_TAG}

start-tts-server:
	@echo "Starting NeMo TTS Server..."
	docker run -d -p 5556:8000 ${NEMO_TTS_IMAGE}:${NEMO_TTS_TAG}