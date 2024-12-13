from PyQt6 import QtGui, QtWidgets, QtCore
import time
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # надпись
        self.label = QtWidgets.QLabel(
            "Лабораторная работа №1\n"
            "Введение в PyQt 6\n"
            "Выполнил студент группы ИТИ-21\n"
            "Арбуз арбуз", self
        )
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # центрируется
        # фотка
        self.image_label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap("lol.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # центрируется
        # Создаем кнопку
        self.button = QtWidgets.QPushButton("Закрыть окно", self)
        self.button.clicked.connect(QtWidgets.QApplication.instance().quit)
        # Размещаем элементы в вертикальном компоновщике
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def load_data(self, sp):
        for i in range(1, 11):  # Имитируем процесс
            time.sleep(1)  # Имитируем загрузку
            sp.showMessage(f"{i * 10}%",
                           QtCore.Qt.AlignmentFlag.AlignHCenter |
                           QtCore.Qt.AlignmentFlag.AlignBottom,
                           QtCore.Qt.GlobalColor.black)
            # Принудительно обрабатываем события
            QtWidgets.QApplication.instance().processEvents()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Создаем заставку
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("lom.jpg"))
    splash.showMessage("0%",
                       QtCore.Qt.AlignmentFlag.AlignHCenter |
                       QtCore.Qt.AlignmentFlag.AlignBottom,
                       QtGui.QColor("Black"))
    splash.show()  # Отображаем заставку
    # Принудительно обрабатываем события
    QtWidgets.QApplication.instance().processEvents()
    # Создаем основное окно
    window = MyWindow()
    window.setWindowTitle("Лабораторная работа №1")
    window.resize(400, 400)
    # Имитация процесса загрузки
    window.load_data(splash)
    # Отображаем основное окно
    window.show()
    # Закрываем заставку
    splash.finish(window)
    sys.exit(app.exec())