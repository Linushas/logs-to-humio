# Vector configuration for Humio ingestion of Mule log data

## Install
```bash
git clone https://github.com/Linushas/logs-to-humio.git; cd logs-to-humio;
make install HUMIO_INGEST_TOKEN=[your-token-abc123] VECTOR_LOG_PATH=[/absolute/path/to/logs/*.log];
make venv; make assemble
```

## Start Vector
```bash
make run
```
