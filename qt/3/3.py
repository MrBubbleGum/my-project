import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,
    QLineEdit, QDialog, QFormLayout, QSpinBox, QComboBox, QDateEdit
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QDate

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройки главного окна
        self.setWindowTitle("Важная Я. И., ИТИ-21")
        self.setGeometry(200, 200, 600, 400)

        # Главный виджет и компоновка
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout()

        # Текст в главном окне
        label = QLabel(
            "Лабораторная работа №3\n"
            "Основные компоненты. Размещение компонентов в окнах\n"
            "Выполнил студент группы ИТИ-21\n"
            "Важная Яна Ивановна"
        )
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Кнопки
        btn_survey = QPushButton("Открыть анкету")
        btn_survey.setToolTip("Открывает окно с анкетой")
        btn_survey.clicked.connect(self.open_survey_window)
        layout.addWidget(btn_survey)

        btn_function = QPushButton("График функции")
        btn_function.setToolTip("Открывает окно для вычисления значения функции")
        btn_function.clicked.connect(self.open_function_window)
        layout.addWidget(btn_function)

        btn_region = QPushButton("Проверка области")
        btn_region.setToolTip("Открывает окно для проверки попадания в область")
        btn_region.clicked.connect(self.open_region_check_window)
        layout.addWidget(btn_region)

        # Установка компоновки
        main_widget.setLayout(layout)

    # Открытие окна с анкетой
    def open_survey_window(self):
        survey_dialog = SurveyWindow(self)
        survey_dialog.exec()

    # Открытие окна с графиком функции
    def open_function_window(self):
        function_dialog = FunctionWindow(self)
        function_dialog.exec()

    # Открытие окна с проверкой области
    def open_region_check_window(self):
        region_dialog = RegionCheckWindow(self)
        region_dialog.exec()


class SurveyWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Анкета")
        self.setGeometry(300, 300, 400, 300)

        # Создание формы
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        form_layout.addRow("Ваше имя:", self.name_input)

        self.age_input = QSpinBox()
        self.age_input.setRange(1, 100)
        form_layout.addRow("Возраст:", self.age_input)

        self.birth_date = QDateEdit()
        self.birth_date.setCalendarPopup(True)
        self.birth_date.setDate(QDate.currentDate())
        form_layout.addRow("Дата рождения:", self.birth_date)

        self.color_input = QComboBox()
        self.color_input.addItems(["Розовый", "Синий", "Зеленый"])
        form_layout.addRow("Любимый цвет:", self.color_input)

        # Кнопка отправки
        submit_button = QPushButton("Отправить")
        submit_button.clicked.connect(self.submit_form)
        form_layout.addWidget(submit_button)

        self.setLayout(form_layout)

    def submit_form(self):
        print(f"Имя: {self.name_input.text()}")
        print(f"Возраст: {self.age_input.value()}")
        print(f"Дата рождения: {self.birth_date.date().toString()}")
        print(f"Любимый цвет: {self.color_input.currentText()}")
        self.accept()


class FunctionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("График функции")
        self.setGeometry(300, 300, 600, 200)

        layout = QVBoxLayout()

        # Поля ввода
        self.x_input = QLineEdit()
        layout.addWidget(QLabel("Введите значение X:"))
        layout.addWidget(self.x_input)

        self.result_label = QLabel("Значение Y:")
        layout.addWidget(self.result_label)

        # Кнопки
        solve_button = QPushButton("Решить")
        solve_button.clicked.connect(self.solve_function)
        layout.addWidget(solve_button)

        clear_button = QPushButton("Очистить")
        clear_button.clicked.connect(self.clear_inputs)
        layout.addWidget(clear_button)

        exit_button = QPushButton("Выход")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)

    def solve_function(self):
        try:
            x = float(self.x_input.text())
            y = self.calculate_function_y(x)
            self.result_label.setText(f"Значение Y: {y}")
            self.show_graph()  # Отображаем график в отдельном окне
        except ValueError:
            self.result_label.setText("Ошибка: некорректный ввод")

    def clear_inputs(self):
        self.x_input.clear()
        self.result_label.setText("Значение Y:")

    def calculate_function_y(self, x):
        if -8 <= x <= 0:
            return -2
        elif 0 < x <= 6:
            return x - 2
        elif x > 6:
            return (x - 6) ** 2
        return 0

    def show_graph(self):
        graph_window = GraphWindow()
        graph_window.exec()  # Открываем как модальное окно


class GraphWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("График функции")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()
        self.graph_label = QLabel()
        self.graph_pixmap = QPixmap("1.png")  # Укажите путь к изображению
        self.graph_label.setPixmap(self.graph_pixmap)
        layout.addWidget(self.graph_label)

        self.setLayout(layout)


class RegionCheckWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Проверка области")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        # Поля ввода
        self.x_input = QLineEdit()
        layout.addWidget(QLabel("Введите значение X:"))
        layout.addWidget(self.x_input)

        self.r_input = QLineEdit()
        layout.addWidget(QLabel("Введите радиус R:"))
        layout.addWidget(self.r_input)

        self.result_label = QLabel("Результат:")
        layout.addWidget(self.result_label)

        # Кнопки
        check_button = QPushButton("Определить")
        check_button.clicked.connect(self.check_region)
        layout.addWidget(check_button)

        clear_button = QPushButton("Очистить")
        clear_button.clicked.connect(self.clear_inputs)
        layout.addWidget(clear_button)

        exit_button = QPushButton("Выход")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)

        # Для графика
        self.point_x = None
        self.point_r = None

    def check_region(self):
        try:
            self.point_x = float(self.x_input.text())
            self.point_r = float(self.r_input.text())
            if self.is_point_in_region(self.point_x, self.point_r):
                self.result_label.setText("Точка попадает в область")
            else:
                self.result_label.setText("Точка не попадает в область")
            self.show_graph()  # Отображаем график области
        except ValueError:
            self.result_label.setText("Ошибка: некорректный ввод")

    def clear_inputs(self):
        self.x_input.clear()
        self.r_input.clear()
        self.result_label.setText("Результат:")
        self.point_x = None
        self.point_r = None

    def is_point_in_region(self, x, r):
        if -r <= x <= 0 and -r <= r:
            return True
        elif 0 < x <= r and 0 <= x <= r:
            return True
        elif x > r and (x - r) ** 2 + r ** 2 <= r ** 2:
            return True
        else:
            return False

    def show_graph(self):
        graph_window = GraphRegionWindow()
        graph_window.exec()  # Открываем как модальное окно


class GraphRegionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("График области")
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()
        self.graph_label = QLabel()
        self.graph_pixmap = QPixmap("2.png")  # Укажите путь к изображению
        self.graph_label.setPixmap(self.graph_pixmap)
        layout.addWidget(self.graph_label)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())