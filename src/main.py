import yaml
from pathlib import Path

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def main():
    config_dir = Path('../config')
    vector_config = load_yaml(config_dir / 'main.yaml')
    vector_config['sources'] = load_yaml(config_dir / 'sources.yaml')
    transforms_dir = config_dir / 'transforms'
    transforms = {}
    
    merge_multiline_config = load_yaml(transforms_dir / 'merge_multiline.yaml')
    merge_multiline_lua = read_file(transforms_dir / 'merge_multiline.lua')
    merge_multiline_config['merge_multiline']['source'] = merge_multiline_lua
    transforms.update(merge_multiline_config)
    
    transforms.update(load_yaml(transforms_dir / 'check_empty.yaml'))

    log_parser_config = load_yaml(transforms_dir / 'log_parser.yaml')
    log_parser_vrl = read_file(transforms_dir / 'log_parser.vrl')
    log_parser_config['log_parser']['source'] = log_parser_vrl
    transforms.update(log_parser_config)

    vector_config['transforms'] = transforms
    vector_config['sinks'] = load_yaml(config_dir / 'sinks.yaml')
    
    with open('../vector.yaml', 'w') as f:
        yaml.dump(vector_config, f, sort_keys=False, indent=2)

    print("vector.yaml has been assembled successfully!")

if __name__ == '__main__':
    main()