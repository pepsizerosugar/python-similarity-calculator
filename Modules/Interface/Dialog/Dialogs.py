from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Modules.Interface.DataClass.UIElement import UIElements


def when_try_to_load_file():
    return QFileDialog.getOpenFileName(UIElements.main_window, "Open XML File", "", "XML Files (*.xml)")[0]


def when_target_load_success():
    QMessageBox.information(UIElements.main_window, "Success", "Target loaded successfully!")


def when_comparison_target_load_success():
    QMessageBox.information(UIElements.main_window, "Success", "Comparison target loaded successfully!")


def when_no_file_selected():
    QMessageBox.warning(UIElements.main_window, "Warning", "No file selected!")


def when_get_error_at_convert_to_json():
    QMessageBox.critical(UIElements.main_window, 'Error', 'Error while converting xml to json!')


def when_both_target_and_comparison_target_are_the_same():
    return QMessageBox.question(UIElements.main_window, 'Warning',
                                'Target and Compare Target are same.\nAre you sure to continue?',
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


def when_cancel_same_target():
    QMessageBox.warning(UIElements.main_window, 'Warning', 'Cancel')


def when_calculate_complete(score):
    QMessageBox.information(UIElements.main_window, 'Result', f'Similarity Score: {score}%')
