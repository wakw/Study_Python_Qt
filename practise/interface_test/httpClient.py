from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
import requests


def process_requests(method: str, url: str, params: dict = None):
    """
    处理请求

    Args:
        method: str
            GET POST PUT DELETE
        url: str
        params: dict
            参数
    """
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, data=params)
    elif method == 'PUT':
        response = requests.put(url)  # 参数不全
    elif method == 'DELETE':
        response = requests.delete(url)  # 参数不全
    return response


class InterfaceTest:
    def __init__(self):
        self.ui = QUiLoader().load('interface.ui')
        self.ui.messageHeaderAdd.clicked.connect(self.message_header_add)
        self.ui.messageHeaderDel.clicked.connect(self.message_header_del)
        self.ui.messageSend.clicked.connect(self.send_message)
        self.ui.logClear.clicked.connect(self.log_clear)

    def message_header_add(self):
        """添加一行"""
        row_count = self.ui.messageHeaderTabel.rowCount()
        self.ui.messageHeaderTabel.insertRow(row_count)

    def message_header_del(self):
        """删除一行 如果没有指定删除的行 默认删除最后一行"""
        del_row = self.ui.messageHeaderTabel.currentRow()
        if del_row == -1:
            row_count = self.ui.messageHeaderTabel.rowCount() - 1
        else:
            row_count = del_row
        self.ui.messageHeaderTabel.removeRow(row_count)

    def log_clear(self):
        """清空返回的消息 日志"""
        self.ui.logShow.clear()

    def read_message_tabel(self):
        """读取消息头表格数据"""
        data = {}
        for row in range(self.ui.messageHeaderTabel.rowCount()):
            key = self.ui.messageHeaderTabel.item(row, 0)
            value = self.ui.messageHeaderTabel.item(row, 1)
            if (key is None) or (value is None):  # 跳过空格
                continue
            data[key.text()] = value.text()

        return data

    def send_message(self):
        """向指定的url发送消息"""
        method = self.ui.httpMethod.currentText()
        url = self.ui.url.text()

        try:
            params = self.read_message_tabel()
            body = self.ui.messageBody.toPlainText()  # 消息体
            response = process_requests(method, url, params)
            header = response.headers

            # 显示日志
            self.ui.logShow.append("--------------- 发送请求 ---------------")
            self.ui.logShow.append(f"{method} {url}")
            for k, v in params.items():
                self.ui.logShow.append(f"{k}: {v}")
            self.ui.logShow.append(f"\n{body}\n")
            self.ui.logShow.append("--------------- 得到响应 ---------------")
            self.ui.logShow.append("Date: {}".format(header['Date']))
            self.ui.logShow.append("Server: {}".format(header['Server']))
            self.ui.logShow.append("Content-Type: {}".format(header['Content-Type']))
            self.ui.logShow.ensureCursorVisible()  # 自动翻滚到当前添加的这行 这种方法会在添加文本后 自动换行

        except BaseException as e:
            self.ui.logShow.append(str(e))  # 显示报错信息

        self.ui.logShow.append("\n")


app = QApplication([])
app.setWindowIcon(QIcon('logo.png'))  # 添加主窗口图标
interface_test = InterfaceTest()
interface_test.ui.show()
app.exec_()
