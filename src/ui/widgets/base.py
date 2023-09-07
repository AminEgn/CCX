# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout


class BaseFrame(QFrame):
    """Base Frame"""

    def __init__(self, ui, *args, **kwargs):
        super().__init__(ui, *args, **kwargs)
        self.ui = ui
        self._bootstrap()
        self.entry()

    def _bootstrap(self):
        self._initialize()
        self._createLayout()
        self._createFrame()
        self._connectedSignals()
        self._setStyle()

    def entry(self):
        pass

    def _initialize(self):
        pass

    def _createLayout(self):
        self.generalLayout = QVBoxLayout()
        self.generalLayout.setAlignment(Qt.AlignTop)
        self.generalLayout.setSpacing(0)
        self.generalLayout.setContentsMargins(2, 5, 2, 2)
        self.setLayout(self.generalLayout)

    def _createFrame(self):
        pass

    def _connectedSignals(self):
        pass

    def _setStyle(self):
        pass
