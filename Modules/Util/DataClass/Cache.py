from dataclasses import dataclass


@dataclass
class Cache:
    data: dict = None
    score: float = 0
    json_path: str = "Resources/converted_json/"

    difference_element_list: list = None
