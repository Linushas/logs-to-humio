PYTHON = python3
SRC_DIR = src
CONFIG_DIR = config
VENV_DIR = $(SRC_DIR)/venv
VENV_BIN = $(VENV_DIR)/bin
VECTOR_CONFIG = vector.yaml
VECTOR_DATA_DIR = vector_data

all: assemble

assemble:
	@. $(VENV_BIN)/activate; \
	cd src && $(PYTHON) main.py

run:
	@HUMIO_INGEST_TOKEN=$(shell cat $(CONFIG_DIR)/humio_ingest_token.txt) \
	VECTOR_LOG_PATH=$(shell cat $(CONFIG_DIR)/path_to_logs.txt) \
	vector -c $(VECTOR_CONFIG)

.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV_DIR)
	@. $(VENV_BIN)/activate; \
	pip install -r $(SRC_DIR)/requirements.txt

.PHONY: clean
clean:
	@rm -rf $(VENV_DIR)

clear_vector_data:
	@rm -rf $(VECTOR_DATA_DIR)/**