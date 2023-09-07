# internal
from . import widgets

# pyqt
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets


class UI(QtWidgets.QMainWindow):
    """User Interface"""

    def __init__(self, lang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lang = lang
        self._bootstrap()

    def _bootstrap(self):
        self._createUI()
        self._connectedSignals()
        self._setStyle()

    def _createUI(self):
        # central widget
        self._centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self._centralWidget)
        # general layout
        self.generalLayout = QtWidgets.QStackedLayout()
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        self.generalLayout.setSpacing(0)
        self.generalLayout.setAlignment(Qt.AlignTop)
        self._centralWidget.setLayout(self.generalLayout)

    def _createFrames(self):
        pass

    def _connectedSignals(self):
        pass

    def _setStyle(self):
        pass
