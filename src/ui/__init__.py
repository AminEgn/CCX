# internal
from . import widgets
from .components import ActionButton

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
        self.setMinimumSize(900, 460)
        # central widget
        self._centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self._centralWidget)
        # general layout
        self.generalLayout = QtWidgets.QStackedLayout()
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        self.generalLayout.setSpacing(0)
        self.generalLayout.setAlignment(Qt.AlignTop)
        self._centralWidget.setLayout(self.generalLayout)
        # instance
        self._createFrames()

    def _createMenu(self):
        self._menuWidget = QtWidgets.QWidget(self)
        self._menuLayout = QtWidgets.QVBoxLayout()
        self._menuWidget.setLayout(self._menuLayout)
        # buttons
        self.btnCustomer = ActionButton("Customer")
        self.btnGroup = ActionButton("Group")
        self.btnSettings = ActionButton("Settings")
        self._menuButtons = (
            self.btnCustomer,
            self.btnGroup,
            self.btnSettings,
        )
        for btn in self._menuButtons:
            self._menuLayout.addWidget(btn)

        # attach
        self._landingLayout.addWidget(self._menuWidget)

    def _createLanding(self):
        self._landingWidget = QtWidgets.QWidget(self)
        self._landingLayout = QtWidgets.QHBoxLayout()
        self._landingWidget.setLayout(self._landingLayout)
        # instance
        self.dashboardFrame = widgets.DashboardFrame(self)
        self._createMenu()
        # attach
        # - landing
        self._landingLayout.addWidget(self.dashboardFrame)
        # - general
        self.generalLayout.addWidget(self._landingWidget)

    def _createFrames(self):
        self._createLanding()

    def _connectedSignals(self):
        pass

    def _setStyle(self):
        pass
