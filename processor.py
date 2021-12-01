import json
from pathlib import Path


class DataWriter:

    def __init__(self, _path):
        self.path = Path(_path)
        if not self.path.exists():
            try:
                self.path.mkdir()
            except:
                raise Exception("Unable to create output dir")

    def write(self, file_name: str, data: dict):
        with open(Path(self.path, file_name), "w") as _file:
            _file.write(json.dumps(data))


class DataReader:

    def __init__(self, _path):
        self.path = Path(_path)

    def datasets(self):
        for _file in self.path.glob("*.json"):
            try:
                parsed = json.loads(_file.read_text())
                yield (_file.name, parsed) if isinstance(parsed, dict) else (
                    _file.name, Exception(f"This file is wrong: {_file.name}"))
            except Exception as e:
                yield _file.name, Exception(f"This file is wrong. {e}")


class DatasetFilter:

    def __init__(self, dataset=None, filters=None):
        self.data = dataset or {}
        self.filters = filters or []

    def apply(self):
        if not isinstance(self.data, dict):
            raise Exception("Dataset is not a dictionary")

        result = {}

        for item in self.data.items():
            for filter_func in self.filters:
                try:
                    item = filter_func(item)
                except Exception as e:
                    raise Exception(f"Filtering failure in: {e}")

            result.update({item[0]: item[1]}) if item else None

        return result
