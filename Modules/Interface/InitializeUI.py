from PyQt5.QtWidgets import QGridLayout, QWidget

from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.GroupBox.InteractionGroupBox import InitInteractionGroup
from Modules.Interface.GroupBox.LabelGroupBox import InitTargetLabelGroup


class InitUI:
    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout()
        self.main_widget = None

    def init_layout(self):
        # set style
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # init groupbox
        InitInteractionGroup().__init__()
        InitTargetLabelGroup().__init__()

        # add elements to layout
        self.main_layout.addWidget(UIElements.interaction_group_box, 0, 0)
        self.main_layout.addWidget(UIElements.label_group_box, 1, 0)

        self.init_widget()

    def init_widget(self):
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        UIElements.main_window.setCentralWidget(self.main_widget)
