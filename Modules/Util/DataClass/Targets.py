from dataclasses import dataclass


@dataclass
class Targets:
    data: dict = None
    score: float = 0
    json_path: str = "Resources/json/"

    difference_element_list: list = None
