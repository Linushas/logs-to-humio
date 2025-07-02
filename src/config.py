CONFIG_DIR = "../config"
OUTPUT_YAML = "../vector.yaml"
CONSOLE_SINK = CONFIG_DIR+"/console_sink.yaml"
HUMIO_SINK = CONFIG_DIR+"/sinks.yaml"

DEBUG = False

SINK = CONSOLE_SINK if DEBUG else HUMIO_SINK
IGNORE_CHECKPOINTS = DEBUG