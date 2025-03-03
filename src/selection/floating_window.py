from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal

class FloatingWindow(QWidget):
    """划词功能的悬浮窗口UI实现"""
    
    # 定义信号
    question_submitted = pyqtSignal(str)
    window_closed = pyqtSignal()
    
    def __init__(self, selected_text: str = ""):
        super().__init__()
        self.setWindowFlags(
            Qt.Window |
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setup_ui(selected_text)
    
    def setup_ui(self, selected_text: str) -> None:
        """设置UI组件
        
        Args:
            selected_text: 用户选中的文本内容
        """
        layout = QVBoxLayout()
        
        # 文本输入框
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("输入你的问题或直接点击提问")
        self.text_edit.setText(selected_text)
        layout.addWidget(self.text_edit)
        
        # 提问按钮
        ask_button = QPushButton("提问")
        ask_button.clicked.connect(self.submit_question)
        layout.addWidget(ask_button)
        
        self.setLayout(layout)
    
    def submit_question(self) -> None:
        """提交问题"""
        question = self.text_edit.toPlainText().strip()
        if question:
            self.question_submitted.emit(question)
            self.close()
    
    def closeEvent(self, event) -> None:
        """窗口关闭事件"""
        self.window_closed.emit()
        super().closeEvent(event)
    
    def mousePressEvent(self, event) -> None:
        """鼠标按下事件，用于实现窗口拖动"""
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event) -> None:
        """鼠标移动事件，用于实现窗口拖动"""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()