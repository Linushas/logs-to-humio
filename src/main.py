import yaml
from pathlib import Path
import os
from config import CONFIG_DIR, OUTPUT_YAML, SINK, IGNORE_CHECKPOINTS

class LiteralString(str):
    pass

def literal_presenter(dumper:yaml.SafeDumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralString, literal_presenter, Dumper=yaml.SafeDumper)

def load_yaml(path:str):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def read_file(path:str):
    with open(path, 'r') as f:
        return f.read()

def main():
    config_dir = Path(CONFIG_DIR)
    data_dir = os.path.abspath("../vector_data")
    vector_config = load_yaml(config_dir / 'main.yaml')
    vector_config['data_dir'] = data_dir

    # sources
    vector_config['sources'] = load_yaml(config_dir / 'sources.yaml')
    vector_config['sources']['app_log']['ignore_checkpoints'] = IGNORE_CHECKPOINTS
    vector_config['sources']['app_log']['oldest_first'] = True
    
    transforms_dir = config_dir / 'transforms'
    transforms = {}

    # Merge multiline transform
    merge_multiline_config = load_yaml(transforms_dir / 'merge_multiline/merge_multiline.yaml')
    merge_multiline_source = read_file(transforms_dir / 'merge_multiline/merge_multiline_source.lua')
    merge_multiline_config['merge_multiline']['source'] = LiteralString(merge_multiline_source)
    merge_multiline_process = read_file(transforms_dir / 'merge_multiline/merge_multiline_process.lua')
    merge_multiline_config['merge_multiline']['hooks']['process'] = LiteralString(merge_multiline_process)
    merge_multiline_shutdown = read_file(transforms_dir / 'merge_multiline/merge_multiline_shutdown.lua')
    merge_multiline_config['merge_multiline']['hooks']['shutdown'] = LiteralString(merge_multiline_shutdown)
    transforms.update(merge_multiline_config)

    # Check empty transform
    transforms.update(load_yaml(transforms_dir / 'check_empty.yaml'))

    # Log parser remap transform
    log_parser_config = load_yaml(transforms_dir / 'log_parser.yaml')
    log_parser_vrl_path = transforms_dir / 'log_parser.vrl'
    if log_parser_vrl_path.exists():
        log_parser_vrl = read_file(log_parser_vrl_path)
        log_parser_config['log_parser']['source'] = LiteralString(log_parser_vrl)
    else:
        print(f"Warning: {log_parser_vrl_path} not found. 'log_parser' transform will be missing 'source'.")
    transforms.update(log_parser_config)

    # sinks
    vector_config['transforms'] = transforms
    vector_config['sinks'] = load_yaml(SINK)

    output_file = Path(OUTPUT_YAML)
    with open(output_file, 'w') as f:
        yaml.dump(vector_config, f, Dumper=yaml.SafeDumper, sort_keys=False, indent=2)

    print(f"{output_file} has been assembled successfully!")

if __name__ == '__main__':
    main()