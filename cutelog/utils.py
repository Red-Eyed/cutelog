import PySide2
from PySide2.QtCore import QMetaObject, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QDesktopWidget, QMessageBox
from text_view_dialog import TextViewDialog


def show_info_dialog(parent, title, text):
    show_dialog(parent, title, text, QMessageBox.Information)


def show_warning_dialog(parent, title, text):
    show_dialog(parent, title, text, QMessageBox.Warning)


def show_critical_dialog(parent, title, text):
    show_dialog(parent, title, text, QMessageBox.Critical)


def show_dialog(parent, title, text, icon):
    m = QMessageBox(parent)
    m.setWindowModality(Qt.NonModal)
    m.setText(text)
    m.setWindowTitle(title)
    m.setAttribute(Qt.WA_DeleteOnClose, True)
    m.setIcon(icon)
    m.show()
    center_widget_on_screen(m)


def show_textview_dialog(parent, title, text, icon=QMessageBox.Information):
    d = TextViewDialog(parent, text)
    d.setWindowModality(Qt.NonModal)
    d.setAttribute(Qt.WA_DeleteOnClose, True)
    d.setWindowTitle(title)
    d.open()


def center_widget_on_screen(widget):
    rect = widget.frameGeometry()
    center = QDesktopWidget().availableGeometry().center()
    rect.moveCenter(center)
    widget.move(rect.topLeft())


def loadUi(uifile, baseinstance=None):
    loader = QUiLoader(baseinstance, None)
    widget = loader.load(uifile)
    QMetaObject.connectSlotsByName(widget)
    return widget
