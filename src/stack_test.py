from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import(
    QMainWindow,
    QApplication,
    QWidget,
    QPushButton,
    QStackedWidget,
    QMenuBar,
    QStatusBar,
)
import sys

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(("MainWindow"))
        MainWindow.resize(512, 304)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(("centralwidget"))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 60, 161, 121))
        self.stackedWidget.setObjectName(("stackedWidget"))
        self.page = QWidget()
        self.page.setObjectName(("page"))
        self.wgtMainWindow = QPushButton(self.page)
        self.wgtMainWindow.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.wgtMainWindow.setObjectName(("wgtMainWindow"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(("page_2"))
        self.wgtbtnB = QPushButton(self.page_2)
        self.wgtbtnB.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.wgtbtnB.setObjectName(("wgtbtnB"))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
        self.menubar.setObjectName(("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.wgtMainWindow.setText(_translate("MainWindow", "Widget A", None))
        self.wgtbtnB.setText(_translate("MainWindow", "Widget B", None))


class ControlMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.wgtbtnB.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.wgtMainWindow.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())