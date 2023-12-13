
import sys
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFontComboBox,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QStackedLayout,
    QStatusBar,
    QTimeEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.menu = QWidget()
        self.setCentralWidget(self.menu)
        self.stacked_layout = QStackedLayout()
        
        
        
        
        

        
        menu_layout = QGridLayout()
        date = QDateEdit()
        park_button = QPushButton("Park/Unpark")
        info_button = QPushButton("View Car Information")
        history_button = QPushButton("View Parking History")
        account_button = QPushButton("View Account")
        file_button = QPushButton("Load File")
        exit_button = QPushButton("Exit")
        
        menu_layout.addWidget(QLabel("Parking Garage"))
        menu_layout.addWidget(date, 0, 0)
        menu_layout.addWidget(park_button, 1, 0)
        menu_layout.addWidget(info_button, 2, 0)
        menu_layout.addWidget(history_button, 3, 0)
        menu_layout.addWidget(account_button, 4, 0)
        menu_layout.addWidget(file_button, 5, 0)
        menu_layout.addWidget(exit_button, 6, 0)
        



        # clicked.connect(self.info_menu)
        # clicked.connect(self.history_menu)
        # clicked.connect(self.account_menu)
        # clicked.connect(self.file_menu)
        # clicked.connect(self.close)
        
        #print(self.park_layout.itemAtPosition(5, 0))#.clicked.connect(print("hi"))
        
        park_layout = QGridLayout()
        park = QWidget()
        license_widget = QLineEdit()
        combo_widget = QComboBox()
        owner_widget = QLineEdit()
        entry_widget = QLineEdit()
        exit_widget = QLineEdit()
        
        license_widget.setPlaceholderText("License Number (ABC123)")
        park_layout.addWidget(license_widget, 0, 0)
        
        size_layout = QHBoxLayout()
        combo_widget.addItems(["1 - Small", "2 - Medium", "3 - Large"])
        label = QLabel("Size of the car ")
        size_layout.addWidget(label)
        size_layout.addWidget(combo_widget)
        park_layout.addLayout(size_layout, 1, 0)

        owner_widget.setPlaceholderText("Name of Owner")
        park_layout.addWidget(owner_widget, 2, 0)
        
        entry_widget.setPlaceholderText("Entry Time (HH:MM)")
        park_layout.addWidget(entry_widget, 3, 0)
        
        exit_widget.setPlaceholderText("Exit Time (HH:MM)")
        park_layout.addWidget(exit_widget, 4, 0)
        
        buttons = QDialogButtonBox()
        buttons.setCenterButtons(True)
        btn1 = QDialogButtonBox.StandardButton.Cancel
        btn2 = QDialogButtonBox.StandardButton.Apply
        buttons.setStandardButtons(btn1 | btn2)
        
        park_layout.addWidget(buttons, 5, 0)
        
        self.stacked_layout.addChildLayout(menu_layout)
        self.stacked_layout.addChildLayout(park_layout)
        self.stacked_layout.setCurrentIndex(0)
        self.menu.setLayout(self.stacked_layout)
        park_button.clicked.connect(lambda: self.menu.setLayout(park_layout))    
        buttons.button(btn1).clicked.connect(lambda: self.setCentralWidget(self.menu))
        


    
    def info_menu(self):
        pass
      
    def history_menu(self):
        pass
    
    def account_menu(self):
        pass
    
    def file_menu(self):
        pass
    
        
def main():
    garage_app = QApplication(sys.argv)
    garage_window = MainWindow()
    garage_window.show()
    sys.exit(garage_app.exec())

if __name__ == "__main__":
    main()
        # dialog_layout = QVBoxLayout()
        # form_layout = QFormLayout()
        # form_layout.addRow("Parking Garage", QLabel())
        # form_layout.addRow("License Number:", QLineEdit())
        # form_layout.addRow("Size:", QLineEdit())
        # form_layout.addRow("Owner:", QLineEdit())
        # form_layout.addRow("Hobbies:", QLineEdit())
        # dialog_layout.addLayout(form_layout)
        # buttons = QDialogButtonBox()
        # buttons.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        # dialog_layout.addWidget(buttons)
        # self.setLayout(dialog_layout)
        
        
        # self.setFixedSize(QtCore.QSize(400, 300))
        # label = QLabel("Hello, World!", parent=self)
        # label.setText("Hi")
        # font = label.font()
        # font.setPointSize(30)
        # label.setFont(font)
        # label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        # self.setCentralWidget(label)
        # self.label.setObjectName("label")
        # self.setGeometry(100, 100, 280, 80)
        # button = QPushButton("press.")
        # button.setFixedSize(QtCore.QSize(100, 50))
        # self.setCentralWidget(button)
        # button.pressed.connect(self.close)