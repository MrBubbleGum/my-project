import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, 
    QWidget, QColorDialog, QFontDialog, QInputDialog, QDialog, QMenu, 
    QMenuBar, QStatusBar, QToolBar, QAction, QSplitter, QLabel, QMdiArea, 
    QMdiSubWindow, QPlainTextEdit
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторная работа 6 - Важная Яна Ивановна ИТИ-21")
        self.setGeometry(100, 100, 600, 400)

        # Основной виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной макет
        layout = QVBoxLayout(central_widget)

        # Кнопка "Диалоговые окна"
        btn_dialogs = QPushButton("Диалоговые окна")
        btn_dialogs.setToolTip("Открыть окно с диалогами")
        btn_dialogs.clicked.connect(self.open_dialog_window)
        layout.addWidget(btn_dialogs)

        # Кнопка "SDI-программа"
        btn_sdi = QPushButton("SDI-программа")
        btn_sdi.setToolTip("Открыть SDI программу")
        btn_sdi.clicked.connect(self.open_sdi_program)
        layout.addWidget(btn_sdi)

        # Кнопка "MDI-программа"
        btn_mdi = QPushButton("MDI-программа")
        btn_mdi.setToolTip("Открыть MDI программу")
        btn_mdi.clicked.connect(self.open_mdi_program)
        layout.addWidget(btn_mdi)

    def open_dialog_window(self):
        dialog_window = DialogWindow(self)
        dialog_window.exec_()

    def open_sdi_program(self):
        sdi_window = SDIWindow(self)
        sdi_window.show()

    def open_mdi_program(self):
        mdi_window = MDIWindow(self)
        mdi_window.show()


class DialogWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Окно сведений о программе")
        self.setGeometry(100, 100, 400, 200)

        # Основной макет
        layout = QVBoxLayout(self)

        # Текст с информацией
        label = QLabel("ФИО: Важная Яна Ивановна\nГруппа: ИТИ-21")
        layout.addWidget(label)

        # Кнопка для открытия многостраничного мастера
        btn_master = QPushButton("Открыть многостраничный мастер")
        btn_master.clicked.connect(self.open_master)
        layout.addWidget(btn_master)

    def open_master(self):
        master = MasterWindow(self)
        master.exec_()


class MasterWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Мастер")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)

        # Кнопка для открытия окна подтверждения
        btn_confirm = QPushButton("Открыть окно подтверждения")
        btn_confirm.clicked.connect(self.open_confirmation_dialog)
        layout.addWidget(btn_confirm)

        # Кнопка для ввода целого числа
        btn_int_input = QPushButton("Открыть окно для ввода целого числа")
        btn_int_input.clicked.connect(self.open_int_input_dialog)
        layout.addWidget(btn_int_input)

        # Кнопка для выбора цвета
        btn_color = QPushButton("Открыть окно для выбора цвета")
        btn_color.clicked.connect(self.open_color_dialog)
        layout.addWidget(btn_color)

        # Кнопка для выбора шрифта
        btn_font = QPushButton("Открыть окно для выбора шрифта")
        btn_font.clicked.connect(self.open_font_dialog)
        layout.addWidget(btn_font)

    def open_confirmation_dialog(self):
        reply = QMessageBox.question(self, "Подтверждение", "Вы уверены?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("Подтверждено")

    def open_int_input_dialog(self):
        num, ok = QInputDialog.getInt(self, "Ввод целого числа", "Введите целое число:")
        if ok:
            print(f"Введено число: {num}")

    def open_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(f"Выбран цвет: {color.name()}")

    def open_font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            print(f"Выбран шрифт: {font.family()}")


class SDIWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("SDI-программа")
        self.setGeometry(100, 100, 800, 600)

        # Создание меню
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        file_menu = self.menu_bar.addMenu("Файл")
        edit_menu = self.menu_bar.addMenu("Правка")

        # Добавление действий в меню "Файл"
        new_action = QAction("Новый", self)
        new_action.triggered.connect(self.restart_sdi)
        file_menu.addAction(new_action)

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Добавление действий в меню "Правка"
        copy_action = QAction("Копировать", self)
        copy_action.triggered.connect(self.copy_text)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Вставить", self)
        paste_action.triggered.connect(self.paste_text)
        edit_menu.addAction(paste_action)

        change_orientation_action = QAction("Изменить ориентацию панелей", self)
        change_orientation_action.triggered.connect(self.change_panel_orientation)
        edit_menu.addAction(change_orientation_action)

        # Создание панели инструментов
        toolbar = QToolBar("Панель инструментов")
        self.addToolBar(toolbar)

        # Создание панели 1
        self.panel1 = QSplitter(Qt.Horizontal)
        self.panel1.addWidget(QLabel("Панель 1"))
        self.setCentralWidget(self.panel1)

        # Создание кнопок для панели 1
        btn_console = QPushButton("Вывести сообщение в консоль", self)
        btn_console.clicked.connect(self.print_to_console)
        self.panel1.addWidget(btn_console)

        # Создание панели 2
        self.panel2 = QSplitter(Qt.Vertical)
        self.panel2.addWidget(QLabel("Панель 2"))
        self.panel1.addWidget(self.panel2)

        # Кнопка для разделения панели
        btn_split = QPushButton("Разделить панель", self)
        btn_split.clicked.connect(self.split_panel)
        self.panel2.addWidget(btn_split)

        # Панель 3
        self.panel3 = QSplitter(Qt.Horizontal)
        self.panel3.addWidget(QLabel("Панель 3"))
        self.panel2.addWidget(self.panel3)

        # Панель 4
        self.panel4 = QSplitter(Qt.Horizontal)
        self.panel4.addWidget(QLabel("Панель 4"))
        self.panel3.addWidget(self.panel4)

        # Строка состояния
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # Кнопка для изменения состояния меню
        btn_toggle_menu = QPushButton("Отключить меню", self)
        btn_toggle_menu.clicked.connect(self.toggle_menu)
        self.panel4.addWidget(btn_toggle_menu)

        # Кнопка для вывода/очистки строки состояния
        btn_toggle_status = QPushButton("Сообщение в строке состояния", self)
        btn_toggle_status.clicked.connect(self.toggle_status_message)
        self.panel4.addWidget(btn_toggle_status)

    def print_to_console(self):
        print("Сообщение выведено в консоль")

    def split_panel(self):
        # Создаем новый QSplitter и добавляем его в текущую панель
        new_panel = QSplitter(Qt.Horizontal)
        new_panel.addWidget(QLabel("Новая панель"))
        self.panel2.addWidget(new_panel)

    def toggle_menu(self):
        self.menuBar().setEnabled(not self.menuBar().isEnabled())

    def toggle_status_message(self):
        if self.statusBar.currentMessage():
            self.statusBar.clearMessage()
        else:
            self.statusBar.showMessage("Сообщение в строке состояния")

    def restart_sdi(self):
        # Перезапускаем SDI-программу
        self.close()
        new_sdi = SDIWindow()
        new_sdi.show()

    def copy_text(self):
        print("Текст скопирован")

    def paste_text(self):
        print("Текст вставлен")

    def change_panel_orientation(self):
        # Изменяем ориентацию разделителя между горизонтальной и вертикальной
        if self.panel2.orientation() == Qt.Vertical:
            self.panel2.setOrientation(Qt.Horizontal)
        else:
            self.panel2.setOrientation(Qt.Vertical)


class MDIWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("MDI-программа")
        self.setGeometry(100, 100, 800, 600)

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # Меню "Файл"
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Файл")

        create_action = QAction("Создать окно", self)
        create_action.triggered.connect(self.create_subwindow)
        file_menu.addAction(create_action)

        # Меню "Окно"
        window_menu = menu_bar.addMenu("Окно")

        cascade_action = QAction("Расположить каскадом", self)
        cascade_action.triggered.connect(self.mdi_area.cascadeSubWindows)
        window_menu.addAction(cascade_action)

        tile_action = QAction("Расположить плиткой", self)
        tile_action.triggered.connect(self.mdi_area.tileSubWindows)
        window_menu.addAction(tile_action)

        close_active_action = QAction("Закрыть активное", self)
        close_active_action.triggered.connect(self.mdi_area.closeActiveSubWindow)
        window_menu.addAction(close_active_action)

        close_all_action = QAction("Закрыть все", self)
        close_all_action.triggered.connect(self.mdi_area.closeAllSubWindows)
        window_menu.addAction(close_all_action)

        self.counter = 1

    def create_subwindow(self):
        sub_window = QMdiSubWindow()
        text_edit = QPlainTextEdit()
        text_edit.setPlainText(f"Окно {self.counter}: Фамилия")
        sub_window.setWidget(text_edit)
        sub_window.setWindowTitle(f"Окно {self.counter}")
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()
        self.counter += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())