from PyQt5.QtWidgets import QGroupBox, QGridLayout, QPushButton, QSizePolicy

from Modules.Interface.DataClass.UIElement import UIElements


class InitInteractionGroup:
    def __init__(self):
        super().__init__()
        self.init()

    @staticmethod
    def init():
        UIElements.interaction_group_box = QGroupBox()
        UIElements.interaction_group_box.setLayout(QGridLayout())
        UIElements.interaction_group_box.setStyleSheet(UIElements.styleSheet)
        UIElements.interaction_group_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        UIElements.calculate_button = QPushButton('Calculate')
        UIElements.clear_button = QPushButton('Clear')
        UIElements.calculate_button.setEnabled(False)

        from Modules.Handler.ButtonHandler import ButtonHandler
        UIElements.calculate_button.clicked.connect(ButtonHandler.calculate_button_clicked)
        UIElements.clear_button.clicked.connect(ButtonHandler.clear_button_clicked)

        UIElements.interaction_group_box.layout().addWidget(UIElements.calculate_button, 0, 1)
        UIElements.interaction_group_box.layout().addWidget(UIElements.clear_button, 0, 2)
