from dataclasses import dataclass


@dataclass
class Targets:
    target: str = ""
    target_xml: str = ""
    target_json: str = ""

    comp_target: str = ""
    comp_target_xml: str = ""
    comp_target_json: str = ""

    score: float = 0
