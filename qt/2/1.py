import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QMainWindow, QDialog, QWidget
from PyQt6.QtGui import QFont, QPixmap, QIcon, QPolygon, QRegion
from PyQt6.QtCore import Qt, QPoint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Важная Яна ИТИ-21")  # Заголовок окна
        self.setFixedSize(400, 400)  # Размер окна
        self.setWindowIcon(QIcon('icon.png'))  # Убедитесь, что файл существует

        layout = QVBoxLayout()
        
        # Основной текст с пятью стилями
        label = QLabel(
            "Лабораторная работа №2\n"
            "Работа с окнами. Обработка сигналов и событий\n"
            "Выполнил студент группы ИТИ-21\n"
            "Важная Яна Ивановна"
        )
        label.setFont(QFont("Helvetica", 14, QFont.Weight.Bold))
        label.setStyleSheet("""
            color: blue;
            font-weight: bold;
            text-align: center;
        """)
        layout.addWidget(label)

        # Кнопка 1 - Открыть окно с изображением
        button1 = QPushButton("Открыть окно с изображением")
        button1.setToolTip("Открывает окно с изображением.")  # Подсказка при наведении
        button1.clicked.connect(self.open_window_with_image)
        layout.addWidget(button1)

        # Кнопка 2 - Открыть окно с функцией
        button2 = QPushButton("Открыть окно с функцией")
        button2.setToolTip("Открывает окно, выполняющее функцию.")  # Подсказка при наведении
        button2.clicked.connect(self.open_window_with_function)
        layout.addWidget(button2)

        # Контейнер для размещения элементов
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.center_window()

    def center_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def open_window_with_image(self):
        window = ParallelogramWindow(self)
        window.setWindowTitle("Окно с изображением")
        window.setFixedSize(400, 400)
        window.setWindowOpacity(0.4)  # Прозрачность 40%
        window.show()

    def open_window_with_function(self):
        window = KeyPressWindow(self)
        window.show()

class ParallelogramWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 500)
        self.apply_parallelogram_mask()

        # Загружаем фоновое изображение
        pixmap = QPixmap("fonn.jpg")  # Убедитесь, что файл существует
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 500, 500)

    def apply_parallelogram_mask(self):
        points = [
            QPoint(50, 0), QPoint(450, 0),
            QPoint(400, 500), QPoint(0, 500)
        ]
        polygon = QPolygon(points)
        self.setMask(QRegion(polygon))  # Применяем маску в виде параллелограмма

class KeyPressWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Окно с функцией")
        self.setFixedSize(400, 300)

        self.apply_parallelogram_mask()

        # Текстовое поле для вывода результатов
        self.label = QLabel("Нажмите любую клавишу", self)
        self.label.setFont(QFont("Arial", 12))
        self.label.setGeometry(50, 130, 300, 20)

    def apply_parallelogram_mask(self):
        points = [
            QPoint(50, 0), QPoint(350, 0),
            QPoint(300, 300), QPoint(0, 300)
        ]
        polygon = QPolygon(points)
        self.setMask(QRegion(polygon))  # Применяем маску в виде параллелограмма

    def keyPressEvent(self, event):
        key = event.text()  # Получаем символ клавиши
        self.label.setText(f"Вы нажали: {key}")  # Отображаем на экране

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
