from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QPushButton, QSizePolicy, QTextEdit

from Modules.Handler.ButtonHandler import ButtonHandler
from Modules.Interface.DataClass.UIElement import UIElements

UIElements.data = {}


class InitLabelGroup:
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.init_label_group_box()

    def init_label_group_box(self):
        UIElements.label_group_box = QGroupBox()
        UIElements.label_group_box.setLayout(QGridLayout())
        UIElements.label_group_box.setStyleSheet(UIElements.styleSheet)
        UIElements.label_group_box.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.init_each_label_group_box(["target", "comp_target"])

        UIElements.label_group_box.layout().addWidget(UIElements.data["target"]["target_label_group_box"], 0, 1)
        UIElements.label_group_box.layout().addWidget(UIElements.data["comp_target"]["comp_target_label_group_box"], 0, 2)

    @staticmethod
    def init_each_label_group_box(args):
        for arg in args:
            UIElements.data[arg] = {}
            UIElements.data[arg][arg + "_label_group_box"] = QGroupBox()
            UIElements.data[arg][arg + "_label_group_box"].setLayout(QGridLayout())
            UIElements.data[arg][arg + "_label_group_box"].setStyleSheet(UIElements.styleSheet)

            label_group = QGroupBox()
            label_group.setLayout(QGridLayout())
            label_group.setStyleSheet(UIElements.styleSheet)
            label_group.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

            code_group = QGroupBox()
            code_group.setLayout(QGridLayout())
            code_group.setStyleSheet(UIElements.styleSheet)
            code_group.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

            UIElements.data[arg][arg + "_load_button"] = QPushButton('Load')
            UIElements.data[arg][arg + "_label"] = QLabel("Waiting for load xml file")
            UIElements.data[arg][arg + "_code_label"] = QTextEdit()
            scroll_area = QtWidgets.QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(UIElements.data[arg][arg + "_code_label"])

            UIElements.data[arg][arg + "_load_button"].setMaximumSize(UIElements.data[arg][arg + "_load_button"].sizeHint())

            if arg == "target":
                UIElements.data[arg][arg + "_load_button"].clicked.connect(ButtonHandler.target_load_button_clicked)
            else:
                UIElements.data[arg][arg + "_load_button"].clicked.connect(ButtonHandler.comp_target_load_button_clicked)

            label_group.layout().addWidget(UIElements.data[arg][arg + "_load_button"], 0, 0)
            label_group.layout().addWidget(UIElements.data[arg][arg + "_label"], 0, 1)
            code_group.layout().addWidget(scroll_area, 0, 0)
            UIElements.data[arg][arg + "_label_group_box"].layout().addWidget(label_group, 0, 0)
            UIElements.data[arg][arg + "_label_group_box"].layout().addWidget(code_group, 1, 0)
