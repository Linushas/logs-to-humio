# Vector configuration for Humio ingestion of Mule log data

## Install
1. Install Vector: https://vector.dev/docs/setup/installation/

2. 
```bash
git clone https://github.com/Linushas/logs-to-humio.git; cd logs-to-humio;
make install HUMIO_INGEST_TOKEN=[your-token-abc123] VECTOR_LOG_PATH=[/absolute/path/to/logs/*.log];
make venv; make assemble
```

3. Set **data_dir** in **config/main.yaml**, then run: ```make```

## Start Vector
```bash
make run
```

## To Do
- Timer for merge_multiline transform
- End of file check?
