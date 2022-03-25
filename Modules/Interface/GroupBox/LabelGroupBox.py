from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel

from Modules.Interface.DataClass.UIElement import UIElements


class InitTargetLabelGroup:
    def __init__(self):
        self.init()

    def init(self):
        self.init_label_group_box()

    def init_label_group_box(self):
        UIElements.label_group_box = QGroupBox()
        UIElements.label_group_box.setLayout(QGridLayout())
        UIElements.label_group_box.setStyleSheet(UIElements.styleSheet)
        UIElements.label_group_box.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.init_target_label_group_box()
        self.init_comp_target_label_group_box()

        UIElements.label_group_box.layout().addWidget(UIElements.target_label_group_box, 0, 0)
        UIElements.label_group_box.layout().addWidget(UIElements.comp_label_group_box, 0, 1)

    @staticmethod
    def init_target_label_group_box():
        UIElements.target_label_group_box = QGroupBox()
        UIElements.target_label_group_box.setLayout(QGridLayout())
        UIElements.target_label_group_box.setStyleSheet(UIElements.styleSheet)

        target_label_group = QGroupBox()
        target_label_group.setLayout(QGridLayout())
        target_label_group.setStyleSheet(UIElements.styleSheet)
        target_label_group.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        target_code_group = QGroupBox()
        target_code_group.setLayout(QGridLayout())
        target_code_group.setStyleSheet(UIElements.styleSheet)
        target_code_group.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)

        UIElements.target_label = QLabel()
        UIElements.target_code_label = QLabel()

        target_label_group.layout().addWidget(UIElements.target_label, 0, 0)
        target_code_group.layout().addWidget(UIElements.target_code_label, 0, 0)
        UIElements.target_label_group_box.layout().addWidget(target_label_group, 0, 0)
        UIElements.target_label_group_box.layout().addWidget(target_code_group, 1, 0)

    @staticmethod
    def init_comp_target_label_group_box():
        UIElements.comp_label_group_box = QGroupBox()
        UIElements.comp_label_group_box.setLayout(QGridLayout())
        UIElements.comp_label_group_box.setStyleSheet(UIElements.styleSheet)

        comp_label_group = QGroupBox()
        comp_label_group.setLayout(QGridLayout())
        comp_label_group.setStyleSheet(UIElements.styleSheet)
        comp_label_group.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        comp_code_group = QGroupBox()
        comp_code_group.setLayout(QGridLayout())
        comp_code_group.setStyleSheet(UIElements.styleSheet)
        comp_code_group.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)

        UIElements.comp_target_label = QLabel()
        UIElements.comp_target_code_label = QLabel()

        comp_label_group.layout().addWidget(UIElements.comp_target_label, 0, 0)
        comp_code_group.layout().addWidget(UIElements.comp_target_code_label, 0, 0)
        UIElements.comp_label_group_box.layout().addWidget(comp_label_group, 0, 0)
        UIElements.comp_label_group_box.layout().addWidget(comp_code_group, 1, 0)
