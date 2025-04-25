from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # <- Import QUrl
import sys

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))  # <- Wrap string in QUrl
        self.setCentralWidget(self.browser)
        self.setWindowTitle("My Local Browser")
        self.showMaximized()

app = QApplication(sys.argv)
window = Browser()
app.exec_()
 