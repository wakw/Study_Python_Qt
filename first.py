from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

# .QtWidgets控制控件窗口

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

window.show()  # 最上层控件（窗口）展示

app.exec_()  # 事件处理循环 等待用户输入 是一个死循环
