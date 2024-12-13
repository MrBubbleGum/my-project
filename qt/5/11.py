import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, \
    QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsTextItem, QGraphicsPixmapItem, QGraphicsItemGroup, \
    QComboBox, QHBoxLayout, QGraphicsDropShadowEffect, QGraphicsBlurEffect, QGraphicsItem
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QBrush, QPen, QColor, QFont, QImage, QPolygonF, QPixmap, QCursor
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Лабораторная работа №5")
        self.setGeometry(100, 100, 500, 400)

        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Лабораторная работа №5\nРабота с графикой. Графическая сцена.\n"
                       "Выполнил студент группы ИТИ-21\nВажная Яна", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        button1 = QPushButton("Открыть окно с картиной")
        button1.setToolTip("Нажмите для открытия окна с перерисовкой картины")
        button1.clicked.connect(self.open_paint_window)

        button2 = QPushButton("Открыть газетный лист")
        button2.setToolTip("Нажмите для открытия окна с газетой")
        button2.clicked.connect(self.open_newspaper_window)

        button3 = QPushButton("Открыть графическую сцену")
        button3.setToolTip("Нажмите для открытия графической сцены")
        button3.clicked.connect(self.open_graphicsscene_window)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_paint_window(self):
        """Метод для открытия окна с картиной."""
        self.paint_window = PaintWindow()
        self.paint_window.show()

    def open_newspaper_window(self):
        """Метод для открытия окна с газетным листом."""
        self.newspaper_window = NewspaperWindow()
        self.newspaper_window.show()

    def open_graphicsscene_window(self):
        """Метод для открытия окна с графической сценой."""
        self.graphicsscene_window = GraphicsSceneWindow()
        self.graphicsscene_window.show()


class PaintWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Чёрный квадрат Малевича")
        self.setGeometry(100, 100, 600, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_painting(painter)

    def draw_painting(self, painter):
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(QPen(QColor(255, 255, 255), 2))

        size = 300
        frame_size = 20
        start_x = (self.width() - (size + frame_size * 2)) // 2
        start_y = (self.height() - (size + frame_size * 2)) // 2

        painter.drawRect(start_x, start_y, size + frame_size * 2, size + frame_size * 2)

        painter.setBrush(QBrush(QColor(0, 0, 0)))
        painter.setPen(QPen(QColor(0, 0, 0), 2))

        painter.drawRect(start_x + frame_size, start_y + frame_size, size, size)

        painter.setPen(QPen(QColor(255, 255, 255), 2))
        font = QFont('Arial', 14)
        painter.setFont(font)
        painter.drawText(start_x, start_y + size + frame_size * 2 + 30, "Чёрный квадрат Малевича")


class NewspaperWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Газетный лист")
        self.setGeometry(100, 100, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_newspaper(painter)

    def draw_newspaper(self, painter):
        pen = QPen(QColor(0, 0, 0), 3)
        painter.setPen(pen)

        painter.setFont(QFont('Times', 32))
        painter.drawText(325, 60, "Газеты")

        painter.drawRect(50, 100, 700, 450)
        painter.drawLine(300, 100, 300, 550)
        painter.drawLine(500, 100, 500, 550)

        image_path1 = os.path.abspath("1.jpg")
        image_path2 = os.path.abspath("2.jpg")
        image_path3 = os.path.abspath("3.jpg")

        if os.path.exists(image_path1) and os.path.exists(image_path2) and os.path.exists(image_path3):
            image1 = QImage(image_path1)
            image2 = QImage(image_path2)
            image3 = QImage(image_path3)
            if not image1.isNull() and not image2.isNull() and not image3.isNull():
                painter.drawImage(75, 250, image1.scaled(200, 150))
                painter.drawImage(312, 120, image2.scaled(180, 150))
                painter.drawImage(525, 350, image3.scaled(180, 150))
            else:
                print("Ошибка: Изображение не удалось загрузить.")
        else:
            print(f"Файл изображения не найден.")

        painter.setFont(QFont('Arial', 12))
        painter.drawText(60, 130, 230, 200, Qt.TextFlag.TextWordWrap,
                         "Что из напечатанного на бумаге стареет быстрее всего? Разумеется, газета. Причем к еженедельникам судьба относится благосклоннее. ")
        painter.drawText(60, 425, 230, 200, Qt.TextFlag.TextWordWrap,
                         "Особенно если они печатают интервью со знаменитостями или, в крайнем случае, программу телевидения на неделю. ")
        painter.drawText(310, 300, 180, 200, Qt.TextFlag.TextWordWrap,
                         "Судьба вчерашних газет незавидна. В первой половине ХХ века люди попроще делали из них самокрутки, именовавшиеся из-за своей формы «козьими ножками».")
        painter.drawText(510, 130, 180, 200, Qt.TextFlag.TextWordWrap,
                         "Газетами растапливали кафельные печи и буржуйки в домах, на них клеили обои, ими разжигались пионерские и прочие костры.")


class GraphicsSceneWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графическая сцена")
        self.setGeometry(100, 100, 1200, 600)

        layout = QVBoxLayout()

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 1000, 500)
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(10, 10, 1170, 570)

        self.selected_items = []
        self.group = None

        self.add_graphics_items()

        self.element_selector = QComboBox()
        self.element_selector.addItem("Выберите элемент")
        self.element_selector.addItem("Прямоугольник")
        self.element_selector.addItem("Круг")
        self.element_selector.addItem("Треугольник")
        self.element_selector.addItem("Текст")
        self.element_selector.addItem("Изображение")
        self.element_selector.addItem("Группа")

        layout.addWidget(self.element_selector)

        controls_layout = QHBoxLayout()
        self.add_control_buttons(controls_layout)

        layout.addWidget(self.view)
        layout.addLayout(controls_layout)
        self.setLayout(layout)

        self.view.setScene(self.scene)
        self.view.mousePressEvent = self.on_mouse_click

    def add_graphics_items(self):
        self.rect = QGraphicsRectItem(100, 100, 200, 100)
        self.rect.setBrush(QBrush(QColor("blue")))
        self.rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        self.rect.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.scene.addItem(self.rect)

        self.ellipse = QGraphicsEllipseItem(400, 100, 100, 100)
        self.ellipse.setBrush(QBrush(QColor("green")))
        self.ellipse.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.ellipse.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.scene.addItem(self.ellipse)

        self.triangle = QGraphicsPolygonItem(QPolygonF([QPointF(200, 400), QPointF(250, 350), QPointF(300, 400)]))
        self.triangle.setBrush(QBrush(QColor("red")))
        self.triangle.setFlag(QGraphicsPolygonItem.GraphicsItemFlag.ItemIsMovable)
        self.triangle.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.scene.addItem(self.triangle)

        self.text_item = QGraphicsTextItem("Текст")
        self.text_item.setPos(350, 250)
        self.text_item.setFont(QFont("Arial", 18))
        self.text_item.setFlag(QGraphicsTextItem.GraphicsItemFlag.ItemIsMovable)
        self.scene.addItem(self.text_item)

        image_path = os.path.abspath("sample_image.jpg")
        self.image_item = QGraphicsPixmapItem(QPixmap(image_path))
        self.image_item.setPos(600, 200)
        self.image_item.setFlag(QGraphicsPixmapItem.GraphicsItemFlag.ItemIsMovable)
        self.scene.addItem(self.image_item)

    def on_mouse_click(self, event):
        item = self.scene.itemAt(self.view.mapToScene(event.pos()), self.view.transform())
        if item:
            self.selected_items.append(item)
            item.setSelected(True)

    def add_control_buttons(self, layout):
        button1 = QPushButton("Центрировать элемент")
        button1.clicked.connect(self.center_element)
        layout.addWidget(button1)

        button2 = QPushButton("Повернуть элемент")
        button2.clicked.connect(self.rotate_element)
        layout.addWidget(button2)

        button3 = QPushButton("Изменить размер элемента")
        button3.clicked.connect(self.resize_element)
        layout.addWidget(button3)

        button4 = QPushButton("Группировать элементы")
        button4.clicked.connect(self.group_items)
        layout.addWidget(button4)

        button5 = QPushButton("Применить эффект 1")
        button5.clicked.connect(self.toggle_effect1)
        layout.addWidget(button5)

        button6 = QPushButton("Применить эффект 2")
        button6.clicked.connect(self.toggle_effect2)
        layout.addWidget(button6)

    def center_element(self):
        selected_item = self.element_selector.currentText()
        if selected_item == "Прямоугольник":
            self.view.centerOn(self.rect)
        elif selected_item == "Круг":
            self.view.centerOn(self.ellipse)
        elif selected_item == "Треугольник":
            self.view.centerOn(self.triangle)
        elif selected_item == "Текст":
            self.view.centerOn(self.text_item)
        elif selected_item == "Изображение":
            self.view.centerOn(self.image_item)
        elif selected_item == "Группа" and self.group:
            self.view.centerOn(self.group)

    def rotate_element(self):
        selected_item = self.element_selector.currentText()
        if selected_item == "Прямоугольник":
            self.rect.setRotation(self.rect.rotation() + 15)
        elif selected_item == "Круг":
            self.ellipse.setRotation(self.ellipse.rotation() + 15)
        elif selected_item == "Треугольник":
            self.triangle.setRotation(self.triangle.rotation() + 15)
        elif selected_item == "Текст":
            self.text_item.setRotation(self.text_item.rotation() + 15)
        elif selected_item == "Изображение":
            self.image_item.setRotation(self.image_item.rotation() + 15)

    def resize_element(self):
        selected_item = self.element_selector.currentText()
        if selected_item == "Прямоугольник":
            self.rect.setRect(self.rect.rect().x(), self.rect.rect().y(), 150, 150)
        elif selected_item == "Круг":
            self.ellipse.setPolygon(QPolygonF([QPointF(400, 100), QPointF(500, 50), QPointF(600, 100)]))
        elif selected_item == "Треугольник":
            self.triangle.setPolygon(QPolygonF([QPointF(200, 400), QPointF(350, 300), QPointF(400, 400)]))
        elif selected_item == "Текст":
            self.text_item.setFont(QFont("Arial", 24))
        elif selected_item == "Изображение":
            self.image_item.setPixmap(QPixmap(os.path.abspath("sample_image_resized.jpg")))

    def group_items(self):
        if self.selected_items:
            self.group = QGraphicsItemGroup()
            for item in self.selected_items:
                self.group.addToGroup(item)
                item.setSelected(False)

            self.group.setFlag(QGraphicsItemGroup.GraphicsItemFlag.ItemIsMovable)
            self.scene.addItem(self.group)
            self.selected_items.clear()

    def toggle_effect1(self):
        if self.group:
            if not self.group.graphicsEffect():
                effect = QGraphicsDropShadowEffect()
                effect.setBlurRadius(10)
                self.group.setGraphicsEffect(effect)
            else:
                self.group.setGraphicsEffect(None)

    def toggle_effect2(self):
        if self.group:
            if not self.group.graphicsEffect():
                effect = QGraphicsBlurEffect()
                effect.setBlurRadius(15)
                self.group.setGraphicsEffect(effect)
            else:
                self.group.setGraphicsEffect(None)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
