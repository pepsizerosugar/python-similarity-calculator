from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Modules.Interface.DataClass.UIElement import UIElements


def when_try_to_load_file():
    return QFileDialog.getOpenFileName(UIElements.main_window, "Open XML File", "", "XML Files (*.xml)")[0]


def when_load_success():
    QMessageBox.information(UIElements.main_window, "Info", "Loaded successfully!")


def when_no_file_selected():
    QMessageBox.warning(UIElements.main_window, "Warning", "No file selected!")


def when_get_error_at_load_xml():
    QMessageBox.critical(UIElements.main_window, 'Error', 'Error while loading xml file!')


def when_get_error_at_load_json():
    QMessageBox.critical(UIElements.main_window, 'Error', 'Error while loading json file!')


def when_xml_file_not_found():
    QMessageBox.critical(UIElements.main_window, 'Error', 'File not found!')


def when_json_file_not_found():
    QMessageBox.critical(UIElements.main_window, 'Error', 'JSON file not found!')


def when_xml_file_is_not_valid():
    QMessageBox.critical(UIElements.main_window, 'Error',
                         'XML file is not valid!\nPlease check the file and try again.')


def when_get_error_at_convert_to_json():
    QMessageBox.critical(UIElements.main_window, 'Error', 'Error while converting xml to json!')


def when_calculate_complete(score):
    QMessageBox.information(UIElements.main_window, 'Info', f'Similarity Score: {score}%')
