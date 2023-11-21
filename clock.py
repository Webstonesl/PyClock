import PySide6.QtGui
from PySide6.QtWidgets import *
import sys
from PySide6.QtCore import QObject, Signal, Slot, QTimer
from PySide6.QtGui import QScreen, QFont
from PySide6 import QtCore
from datetime import datetime
app = QApplication(sys.argv)
class ClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel(self)

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Arial',10))

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateClock)
    def updateClock(self):
        self.label.setText(datetime.now().strftime("%H:%M:%S"))
    def resizeEvent(self, event) -> None:
        self.label.setGeometry(self.contentsRect())
        rect = self.contentsRect()
        
        
        self.label.setFont(QFont('Arial',min(rect.width()/4,rect.height())))
           
        return super().resizeEvent(event)

    def showOnScreen(self,scn:QScreen = None):
        if (scn != None):    
            self.setScreen(scn)
        self.showFullScreen()
        # self.show()
        self.timer.start()
        

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.setScreen(app.primaryScreen())
        self.setMinimumSize(800,100)
        self.setWindowTitle("Clock Window")
        
        self.cmb = QComboBox(self)
        layout.addWidget(self.cmb)
        label = QPushButton("Test!",self)
        layout.addWidget(label)
        label.clicked.connect(self.showClock)

        self.clock = ClockWindow()
        

    def showEvent(self, event) -> None:
        event.accept()
        self.cmb.clear()
        self.screens = app.screens()
        for scrn in self.screens:
            self.cmb.addItem(scrn.name(),scrn)
    

        return super().showEvent(event)
        
    def showClock(self):
        self.clock.showOnScreen(self.cmb.itemData(0))
    def closeEvent(self, event) -> None:

        return super().closeEvent(event)



if __name__ == "__main__":
    
    # label = QLabel("Test")
    # label.show()
    mw = MainWindow()
    mw.show()
    app.exec()