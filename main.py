import json
from pathlib import Path

import filters
from processor import DatasetFilter, DataReader, DataWriter


def get_config(file_name):
    try:
        return json.loads(Path(file_name).read_text())
    except:
        raise Exception(f"Unable to read config {file_name}")


if __name__ == '__main__':
    try:
        config = get_config('config.json')
        reader = DataReader(config.get('input', 'in'))
        writer = DataWriter(config.get('output', 'out'))
        filters_list = config.get('filters', [])
        _filters = [filters.__dict__[value] for value in filters_list if value in filters.__dict__]

        for name, dataset in reader.datasets():

            filtered = DatasetFilter(dataset=dataset, filters=_filters).apply()

            writer.write(
                name,
                DatasetFilter(dataset=dataset, filters=_filters).apply()
            )
    except Exception as e:
        print(e)