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

## To Do
- log_parser.vrl : support empty fields, ex) [event: ]
- Add data_dir (main.yaml) to make install
- Timer for merge_multiline transform
- End of file check?
