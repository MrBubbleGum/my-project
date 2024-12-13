import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox, QComboBox, 
    QVBoxLayout, QWidget, QTableView, QTreeView, QHeaderView, QLabel
)
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.setWindowTitle("Важаня Я И, ИТИ-21")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('1.png'))  # Путь к вашему значку

        # Создание кнопки
        self.button = QPushButton("Уголовная статья", self)
        self.button.setToolTip("жмак")
        self.button.clicked.connect(self.open_article_window)
        self.button.setGeometry(100, 150, 200, 40)

    def open_article_window(self):
        self.article_window = ArticleWindow()
        self.article_window.show()

class ArticleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторная работа №4 - Списки и таблицы")
        self.setGeometry(150, 150, 600, 600)

        # Создание основного виджета и макета
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Выпадающий список (QComboBox)
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["статья 1", "статья 2", "статья 3"])
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        self.layout.addWidget(self.combo_box)

        # Текстовое содержание статьи
        self.article_text = QLabel(self)
        self.article_text.setWordWrap(True)
        self.article_text.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.intro_text = """
<h3>1</h3>
Статья 286. Бандитизм
"""

        self.application_text = """
<h3>2</h3>
Статья 290. Угроза совершением акта терроризма
"""

        self.ethics_text = """
<h3>3</h3>
Статья 339. Хулиганство
"""

        self.article_text.setText(self.intro_text)
        self.layout.addWidget(self.article_text)

        # Обычный список (QListView через QStandardItemModel)
        self.list_model = QStandardItemModel()
        self.list_model.appendRow(QStandardItem("2"))
        self.list_model.appendRow(QStandardItem("3"))
        self.list_model.appendRow(QStandardItem("4"))

        self.list_view = QTreeView(self)
        self.list_view.setModel(self.list_model)
        self.layout.addWidget(self.list_view)

        # Иерархический список (QTreeView)
        self.tree_model = QStandardItemModel()
        parent_item = self.tree_model.invisibleRootItem()

        for i in range(1):
            parent = QStandardItem(f"1")
            for j in range(1):
                child = QStandardItem(f"2")
                parent.appendRow(child)
            parent_item.appendRow(parent)

        self.tree_view = QTreeView(self)
        self.tree_view.setModel(self.tree_model)
        self.tree_view.expandAll()  # Развернем все элементы
        self.layout.addWidget(self.tree_view)

        # Таблица 1 (QTableView)
        self.table1_model = QStandardItemModel(3, 3)
        self.table1_model.setHorizontalHeaderLabels(['1', '2', '3'])

        for row in range(3):
            for column in range(3):
                item = QStandardItem(f'+')
                self.table1_model.setItem(row, column, item)

        self.table1_view = QTableView(self)
        self.table1_view.setModel(self.table1_model)
        self.table1_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(self.table1_view)

        # Таблица 2 (QTableView)
        self.table2_model = QStandardItemModel(2, 2)
        self.table2_model.setHorizontalHeaderLabels(['A', 'B'])

        for row in range(2):
            for column in range(2):
                item = QStandardItem(f'777')
                self.table2_model.setItem(row, column, item)

        self.table2_view = QTableView(self)
        self.table2_view.setModel(self.table2_model)
        self.table2_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(self.table2_view)

    def on_combo_box_changed(self, index):
        if index == 0:
            self.article_text.setText(self.intro_text)
        elif index == 1:
            self.article_text.setText(self.application_text)
        elif index == 2:
            self.article_text.setText(self.ethics_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())