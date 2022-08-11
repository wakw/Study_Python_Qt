from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


# PySide2.QtWidgets控制控件窗口

def handleCalc():
    info = textEdit.toPlainText()  # 获取文本内容
    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    # 弹出对话框
    QMessageBox.about(window,
                      '统计结果',
                      f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                      )


# 提供整个图形界面程序的底层管理功能
app = QApplication([])

window = QMainWindow()  # 主窗口对象
window.resize(500, 400)  # 窗口宽高
window.move(300, 310)  # 出现在显示器屏幕的位置 窗口左上角坐标 宽高
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)  # 文本控件 副控件 主控件是window
textEdit.setPlaceholderText("请输入薪资表")  # 提示文本
textEdit.move(10, 25)  # 编辑框左上角坐标 相对于主窗口window的位置
textEdit.resize(300, 350)  # 宽高

button = QPushButton('统计', window)  # 按钮
button.move(380, 80)
button.clicked.connect(handleCalc)  # 把 button 被 点击（clicked） 的信号（signal）， 连接（connect）到了 handleCalc 这样的一个 slot上

window.show()  # 最上层控件（窗口）展示

app.exec_()  # 事件处理循环 等待用户输入 是一个死循环
