from PySide2.QtWidgets import QApplication, QTextBrowser
from PySide2.QtUiTools import QUiLoader
import time
from threading import Thread
from PySide2.QtCore import Signal, QObject


class MySignals(QObject):
    """
    使用 Signal ，防止信号僵死
    """
    # text_print = Signal(QTextBrowser, str)  # 定义信号
    text_print = Signal(str)  # 定义信号


class InfoExtract:
    """
    医院信息抓取系统
    联系
    """

    def __init__(self):
        self.ui = QUiLoader().load('layout.ui')
        self.ui.buttonCrawl.clicked.connect(self.crawl_data)

        self.ms = MySignals()
        self.ms.text_print.connect(self.printToGui)  # 自定义信号的处理函数

    def printToGui(self, text):
        self.ui.progressBox.append(str(text))
        self.ui.progressBox.ensureCursorVisible()  # 一直滚动到最下面 最新可见

    def crawl_data(self):
        def run():
            for i in range(1, 20):
                self.ms.text_print.emit(f"爬取到白月黑羽 - {i}")
                time.sleep(1)

        t = Thread(target=run)
        t.start()


app = QApplication([])
fun = InfoExtract()
fun.ui.show()
app.exec_()
