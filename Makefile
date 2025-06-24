PYTHON = python3
VENV_DIR = src/venv
VENV_BIN = $(VENV_DIR)/bin

all: assemble

assemble:
	@. $(VENV_BIN)/activate; \
	cd src && $(PYTHON) main.py

run:
	@HUMIO_INGEST_TOKEN=$(shell cat config/humio_ingest_token.txt) \
	VECTOR_LOG_PATH=$(shell cat config/path_to_logs.txt) \
	vector --config vector.yaml

.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV_DIR)
	@. $(VENV_BIN)/activate; \
	pip install -r src/requirements.txt

.PHONY: clean
clean:
	@rm -rf $(VENV_DIR)