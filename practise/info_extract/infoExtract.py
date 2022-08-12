from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import time
from threading import Thread


class InfoExtract:
    """
    医院信息抓取系统
    联系
    """

    def __init__(self):
        self.ui = QUiLoader().load('layout.ui')
        self.ui.buttonCrawl.clicked.connect(self.crawl_data)

    def crawl_data(self):
        def run():
            for i in range(1, 6):
                self.ui.progressBox.append(f"爬取到白月黑羽 - {i}")
                time.sleep(1)

        t = Thread(target=run)
        t.start()


app = QApplication([])
fun = InfoExtract()
fun.ui.show()
app.exec_()
