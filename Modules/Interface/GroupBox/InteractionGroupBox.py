from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QPushButton

from Modules.Interface.DataClass.UIElement import UIElements


class InitInteractionGroup:
    def __init__(self):
        self.init()

    @staticmethod
    def init():
        UIElements.interaction_group_box = QGroupBox()
        UIElements.interaction_group_box.setLayout(QGridLayout())
        UIElements.interaction_group_box.setStyleSheet(UIElements.styleSheet)
        UIElements.interaction_group_box.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        UIElements.target_load_button = QPushButton('Load target xml')
        UIElements.comp_target_load_button = QPushButton('Load comparison target xml')
        UIElements.calculate_button = QPushButton('Calculate')
        UIElements.clear_button = QPushButton('Clear')
        UIElements.calculate_button.setEnabled(False)

        from Modules.Handler.ButtonHandler import ButtonHandler
        UIElements.target_load_button.clicked.connect(ButtonHandler.target_load_button_clicked)
        UIElements.comp_target_load_button.clicked.connect(ButtonHandler.comp_target_load_button_clicked)
        UIElements.calculate_button.clicked.connect(ButtonHandler.calculate_button_clicked)
        UIElements.clear_button.clicked.connect(ButtonHandler.clear_button_clicked)

        UIElements.interaction_group_box.layout().addWidget(UIElements.target_load_button, 0, 0)
        UIElements.interaction_group_box.layout().addWidget(UIElements.comp_target_load_button, 0, 1)
        UIElements.interaction_group_box.layout().addWidget(UIElements.calculate_button, 0, 2)
        UIElements.interaction_group_box.layout().addWidget(UIElements.clear_button, 0, 3)
