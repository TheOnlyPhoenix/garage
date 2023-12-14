import main as cli
from garage import Garage
from car import Car
from gui_input import *
import sys
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialogButtonBox,
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)
class Ui_MainWindow(object):
    def setup_Ui(self, MainWindow):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Accent, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Accent, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 23, 23))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Accent, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        
        MainWindow.setObjectName("mainwindow")
        MainWindow.setWindowTitle("QMainWindow")
        MainWindow.setMinimumSize(270, 240)
        self.status_bar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.status_bar)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName("main_widget")
        self.stacked_widget = QStackedWidget(self.central_widget)
        self.stacked_widget.setObjectName("stacked widget")
        ##################################################################
        self.date = QWidget()
        self.date_layout = QVBoxLayout()
        self.date_line = QLineEdit(self.date)
        self.date_line.setPlaceholderText("Date (YYYY-MM-DD)")
        self.date_layout.addWidget(self.date_line)
        self.date_accept = QPushButton("Continue",self.date)
        self.date_layout.addWidget(self.date_accept)
        self.date.setLayout(self.date_layout)
        self.stacked_widget.addWidget(self.date)
        ##################################################################
        self.menu = QWidget()
        self.menu_layout = QGridLayout()
        self.park_button = QPushButton("Park/Unpark", self.menu)
        self.info_button = QPushButton("View Car Information", self.menu)
        self.history_button = QPushButton("View Parking History", self.menu)
        self.account_button = QPushButton("View Account", self.menu)
        self.file_button = QPushButton("Load File", self.menu)
        self.exit_button = QPushButton("Exit", self.menu)

        self.menu_layout.addWidget(QLabel("Parking Garage"))
        self.menu_layout.addWidget(self.park_button, 1, 0)
        self.menu_layout.addWidget(self.info_button, 2, 0)
        self.menu_layout.addWidget(self.history_button, 3, 0)
        self.menu_layout.addWidget(self.account_button, 4, 0)
        self.menu_layout.addWidget(self.file_button, 5, 0)
        self.menu_layout.addWidget(self.exit_button, 6, 0)

        self.menu.setLayout(self.menu_layout)
        self.stacked_widget.addWidget(self.menu)
        ##################################################################
        self.park = QWidget()
        self.park_layout = QGridLayout()
        self.park_license_widget = QLineEdit(self.park)
        self.park_size_box = QComboBox(self.park)
        self.park_owner = QLineEdit(self.park)
        self.park_entry_time = QLineEdit(self.park)
        self.park_exit_time = QLineEdit(self.park)
        self.park_size_box.setPlaceholderText("Choose size")
        
        self.park_license_widget.setPlaceholderText("License Number (ABC123)")
        self.park_layout.addWidget(self.park_license_widget, 0, 0)
        
        size_layout = QHBoxLayout()
        self.park_size_box.addItems(["1 - Small", "2 - Medium", "3 - Large"])
        label = QLabel("Size of the car ")
        size_layout.addWidget(label)
        size_layout.addWidget(self.park_size_box)
        self.park_layout.addLayout(size_layout, 1, 0)
        self.park_owner.setPlaceholderText("Name of Owner")
        self.park_layout.addWidget(self.park_owner, 2, 0)
        self.park_entry_time.setPlaceholderText("Entry Time (HH:MM)")
        self.park_layout.addWidget(self.park_entry_time, 3, 0)
        self.park_exit_time.setPlaceholderText("Exit Time (HH:MM)")
        self.park_layout.addWidget(self.park_exit_time, 4, 0)
        self.park_buttons = QDialogButtonBox()
        self.park_buttons.setCenterButtons(True)
        self.park_button_ok = QDialogButtonBox.StandardButton.Ok
        self.park_button_cancel = QDialogButtonBox.StandardButton.Cancel
        self.park_buttons.setStandardButtons(self.park_button_cancel | self.park_button_ok)
        self.park_layout.addWidget(self.park_buttons, 5, 0)
        
        self.park.setLayout(self.park_layout)
        self.stacked_widget.addWidget(self.park)
        ##################################################################
        self.info = QWidget()
        self.info_layout = QVBoxLayout()
        self.info_split_layouts = QHBoxLayout()
        self.info_split_layout_L = QVBoxLayout()
        self.info_split_layout_R = QVBoxLayout()
        
        self.info_license_dropdown = QComboBox(self.info)
        self.info_license_dropdown.setPlaceholderText("Select car")
        self.num_label = QLabel("License Number:",self.info)
        self.size_label = QLabel("Size:",self.info)
        self.owner_label = QLabel("Owner:",self.info)
        self.time_label = QLabel("Time Parked:",self.info)
        self.debt_label = QLabel("Debt:",self.info)
        widgets = [self.num_label, self.size_label, self.owner_label, self.time_label, self.debt_label]
        for widget in widgets:
            self.info_split_layout_L.addWidget(widget)
        
        self.num_display = QLabel(self.info)
        self.size_display = QLabel(self.info)
        self.owner_display = QLabel(self.info)
        self.time_display = QLabel(self.info)
        self.debt_display = QLabel(self.info)
        
        widgets = [self.num_display, self.size_display, self.owner_display, self.time_display, self.debt_display]
        for widget in widgets:
            self.info_split_layout_R.addWidget(widget)
        
        self.info_back_button = QPushButton("Go back", self.info)
        self.info_split_layouts.addLayout(self.info_split_layout_L)
        self.info_split_layouts.addLayout(self.info_split_layout_R)        
        
        self.info_layout.addWidget(self.info_license_dropdown)
        self.info_layout.addLayout(self.info_split_layouts)
        self.info_layout.addWidget(self.info_back_button)
        self.info.setLayout(self.info_layout)
        self.stacked_widget.addWidget(self.info)
        ##################################################################
        self.history = QWidget()
        self.history_layout = QVBoxLayout()
        self.history_split_layouts = QHBoxLayout()
        self.history_split_layout_L = QVBoxLayout()
        self.history_split_layout_R = QVBoxLayout()
        self.page_buttons_layout = QHBoxLayout()    
        
        self.history_license_dropdown = QComboBox(self.history)
        self.history_license_dropdown.setPlaceholderText("Select car")
        self.page_button_L = QPushButton("<", self.history)
        self.page_button_R = QPushButton(">", self.history)
        self.history_back_button = QPushButton("Go back", self.history)
        
        self.entry_label = QLabel("Entry Time:",self.history)
        self.exit_label = QLabel("Exit Time:",self.history)
        self.time_label = QLabel("Time Parked:",self.history)
        self.debt_label = QLabel("Debt:",self.history)
        widgets = [self.entry_label, self.exit_label, self.time_label, self.debt_label]
        for widget in widgets:
            self.history_split_layout_L.addWidget(widget)
        
        self.entry_display = QLabel(self.history)
        self.exit_display = QLabel(self.history)
        self.time_display = QLabel(self.history)
        self.debt_display = QLabel(self.history)
        widgets = [self.entry_display, self.exit_display, self.time_display, self.debt_display]
        for widget in widgets:
            self.history_split_layout_R.addWidget(widget)
            
        self.page_buttons_layout.addWidget(self.page_button_L)
        self.page_buttons_layout.addWidget(self.history_back_button)
        self.page_buttons_layout.addWidget(self.page_button_R)
        
        self.history_split_layouts.addLayout(self.history_split_layout_L)
        self.history_split_layouts.addLayout(self.history_split_layout_R)
        self.history_layout.addWidget(self.history_license_dropdown)
        self.history_layout.addLayout(self.history_split_layouts)
        self.history_layout.addLayout(self.page_buttons_layout)
        self.history.setLayout(self.history_layout)
        self.stacked_widget.addWidget(self.history)
        ##################################################################
        self.account = QWidget()
        self.account_layout = QVBoxLayout()
        self.debt_layout = QGridLayout()
        
        self.account_license_dropdown = QComboBox(self.account)
        self.account_license_dropdown.setPlaceholderText("Select car")
        self.debt_label = QLabel("Debt:", self.account)
        self.pay_label = QLabel("Pay:", self.account)
        self.debt_display = QLabel(self.account)
        self.pay_amount = QLineEdit(self.account)
        self.pay_amount.setPlaceholderText("Amount")
        self.account_back_button = QPushButton("Go back", self.account)
        
        self.debt_layout.addWidget(self.debt_label, 0, 0)
        self.debt_layout.addWidget(self.debt_display, 0, 1)
        self.debt_layout.addWidget(self.pay_label, 1, 0)
        self.debt_layout.addWidget(self.pay_amount, 1, 1)
        
        self.account_layout.addWidget(self.account_license_dropdown)
        self.account_layout.addLayout(self.debt_layout)
        self.account_layout.addWidget(self.account_back_button)
        self.account.setLayout(self.account_layout)
        self.stacked_widget.addWidget(self.account)
        ##################################################################       
        
        ##################################################################
        MainWindow.setCentralWidget(self.central_widget)
        self.stacked_widget.setCurrentIndex(0)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def load_file(self):
        self.file_input, _ = QFileDialog.getOpenFileName(self.menu, "Open File", "","All Files (*);;Python Files (*.py)")
        print(_)
    def save_file(self):        
        self.save_file, _ = QFileDialog.getSaveFileName()
   
class ControlMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setup_Ui(self)
        self.garage = Garage()
        
        # Change menu page
        self.ui.park_button.clicked.connect(self.park_menu)
        self.ui.info_button.clicked.connect(self.info_menu)
        self.ui.history_button.clicked.connect(self.history_menu)
        self.ui.account_button.clicked.connect(self.account_menu)
        self.ui.file_button.clicked.connect(self.ui.load_file)
        self.ui.exit_button.clicked.connect(self.close)

        
        self.ui.park_buttons.button(self.ui.park_button_cancel).clicked.connect(lambda: self.ui.stacked_widget.setCurrentIndex(1))
        self.ui.info_back_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentIndex(1))
        self.ui.history_back_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentIndex(1))
        self.ui.account_back_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentIndex(1))

        self.ui.date_accept.clicked.connect(self.check_date)
        
        #self.ui.park_buttons.button(self.ui.park_button_ok).clicked.connect(lambda: self.get_car_input)
        
    def park_menu(self):
        self.ui.stacked_widget.setCurrentIndex(2)
        
    def info_menu(self):
        self.ui.stacked_widget.setCurrentIndex(3)
        
    def history_menu(self):
        self.ui.stacked_widget.setCurrentIndex(4)
        
    def account_menu(self):
        self.ui.stacked_widget.setCurrentIndex(5)
        
    def check_date(self, go):
        self.date_input = str(self.ui.date_line.text())
        
        if (re.match(r'^\d{4}-\d{2}-\d{2}$', self.date_input)):
            self.ui.stacked_widget.setCurrentIndex(1)
            self.ui.status_bar.clearMessage()
        else: 
            self.error_msg("\'Date\'")
            

    def error_msg(self, e):
        self.ui.status_bar.showMessage(f"Invalid {e} input", 0)

        
    def get_car_input(self):
        self.ui.park_license_widget.editingFinished(lambda: self.license_input(self.ui.park_license_widget.text()))
        
        size = self.ui.park_size_box.currentIndex + 1
        owner = input_type(self.ui.park_owner.text(), str)
        entry_time = time_input(self.ui.park_entry_time.text())
        exit_time = time_input(self.ui.park_exit_time.text())
        
        #self.garage.append_to_dict
    
    def license_input(self, user_input : str):
        """Asks the user for input. If the program is unable to match a regular expression to '^[A-Z]{3}\d{3}$', the program will ask the user again.
        """
        if (re.match(r'^[A-Z]{3}\d{3}$', user_input)):
            self.license_num = user_input
        else:
            self.error_msg("\'License Number\'")
def main():
    garage_app = QApplication(sys.argv)
    garage_window = ControlMainWindow()
    garage_window.show()
    sys.exit(garage_app.exec())

if __name__ == '__main__':
    main()