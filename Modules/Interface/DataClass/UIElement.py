import os
from dataclasses import dataclass

basedir = os.path.dirname(__file__)


@dataclass
class UIElements:
    main_window: None

    interaction_group_box: None
    target_load_button: None
    comp_target_load_button: None
    calculate_button: None
    clear_button: None

    label_group_box: None
    target_label_group_box: None
    comp_label_group_box: None
    result_label_group_box: None

    target_status_pixmap: None
    comp_target_status_pixmap: None

    target_label: str = ""
    target_code_label: str = ""

    comp_target_label: str = ""
    comp_target_code_label: str = ""

    result_label: str = ""

    styleSheet: str = "QGroupBox { background-color: palette(alternate-base);  border: 1px solid palette(midlight); margin-top: 0px; }"
