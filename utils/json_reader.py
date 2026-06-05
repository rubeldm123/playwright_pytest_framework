import json
from pathlib import Path

class JsonReader:

    DATA_FOLDER = Path(__file__).parent.parent / "data"

    @staticmethod
    def read_json(file_name):

        file_path = JsonReader.DATA_FOLDER / file_name

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)