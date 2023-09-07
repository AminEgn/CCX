# pyqt
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton


class BaseButton(QPushButton):
    """Base Button"""
    HEIGHT = 0
    MIN_WIDTH = 0
    MAX_WIDTH = 0

    def __init__(self, *args, **kwargs):
        self.icon = kwargs.pop('icon', '')
        self.iconSize = kwargs.pop('iconSize', ())
        self.colour = kwargs.pop('colour', '')
        super().__init__(*args, **kwargs)
        self._bootstrap()

    def _bootstrap(self):
        self._createButton()
        self._setStyle()

    def _createButton(self):
        self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        if self.HEIGHT:
            self.setFixedHeight(self.HEIGHT)

        if self.MIN_WIDTH:
            self.setMinimumWidth(self.MIN_WIDTH)

        if self.MAX_WIDTH:
            self.setMaximumWidth(self.MAX_WIDTH)

        if self.icon:
            self.setIcon(QtGui.QIcon(self.icon))
            self.setIconSize(QSize(*self.iconSize))

    def _setStyle(self):
        pass


class ActionButton(BaseButton):
    """Action Button"""
    HEIGHT = 30
    MIN_WIDTH = 40
    MAX_WIDTH = 210
