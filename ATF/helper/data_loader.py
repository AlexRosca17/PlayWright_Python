import json
import os
from typing import Any


def load_test_data(file: str, dataset_id: str) -> dict[str, Any]:
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", file)
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)[dataset_id]
