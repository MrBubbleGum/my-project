import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView,
                            QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsTextItem, QGraphicsLineItem,
                            QGraphicsPixmapItem, QGraphicsSimpleTextItem, QGraphicsItemGroup, QGraphicsItem, QPushButton,
                            QVBoxLayout, QWidget, QHBoxLayout, QColorDialog, QSlider, QLabel, QComboBox, QGraphicsDropShadowEffect, QGraphicsBlurEffect)
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QFont, QImage, QPolygonF, QCursor, QPixmap  # Переносим QPolygonF в QtGui
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.setWindowTitle("Лабораторная работа №5")
        self.setGeometry(100, 100, 500, 400)

        # Создание центрального виджета и layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Создание метки с текстом
        label = QLabel("Лабораторная работа №5\nРабота с графикой. Графическая сцена.\n"
                       "Выполнил студент группы ИТИ-21\nВажная Яна", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Создание кнопок с подсказками
        button1 = QPushButton("Открыть окно с картиной")
        button1.setToolTip("Нажмите для открытия окна с перерисовкой картины")
        button1.clicked.connect(self.open_paint_window)

        button2 = QPushButton("Открыть газетный лист")
        button2.setToolTip("Нажмите для открытия окна с газетой")
        button2.clicked.connect(self.open_newspaper_window)

        button3 = QPushButton("Открыть графическую сцену")
        button3.setToolTip("Нажмите для открытия графической сцены")
        button3.clicked.connect(self.open_graphicsscene_window)
        # Добавление кнопок в layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_paint_window(self):
        # Открыть новое окно с перерисовкой картины
        self.paint_window = PaintWindow()
        self.paint_window.show()

    def open_newspaper_window(self):
        # Открыть новое окно с газетным листом
        self.newspaper_window = NewspaperWindow()
        self.newspaper_window.show()

    def open_graphicsscene_window(self):
        self.graphicsscene_window = GraphicsSceneWindow()
        self.graphicsscene_window.show()

class PaintWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Чёрный квадрат Малевича")
        self.setGeometry(100, 100, 600, 600)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_painting(painter)

    def draw_painting(self, painter):

        painter.setBrush(QBrush(QColor(255, 255, 255)))  # Белая кисть для рамки
        painter.setPen(QPen(QColor(255, 255, 255), 2))  # Белое перо для рамки


        size = 300  # Размер квадрата
        frame_size = 20  # Ширина рамки
        start_x = (self.width() - (size + frame_size * 2)) // 2  # Координаты для рамки
        start_y = (self.height() - (size + frame_size * 2)) // 2


        painter.drawRect(start_x, start_y, size + frame_size * 2, size + frame_size * 2)

        painter.setBrush(QBrush(QColor(128, 0, 128)))  # Чёрная кисть для квадрата
        painter.setPen(QPen(QColor(128, 0, 128), 2))  # Чёрное перо, чтобы границы квадрата были не видны


        painter.drawRect(start_x + frame_size, start_y + frame_size, size, size)



        painter.setPen(QPen(QColor(128, 0, 128), 2))
        font = QFont('Arial', 14)
        painter.setFont(font)
        painter.drawText(start_x, start_y + size + frame_size * 2 + 30, "НеЧёрный квадрат НеМалевича")


class NewspaperWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Газетный лист")
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_newspaper(painter)

    def draw_newspaper(self, painter):
        pen = QPen(QColor(0, 0, 0), 3)  # Черный цвет
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
                painter.drawImage(525, 350, image3.scaled(180, 150))  #
            else:
                print("Ошибка: Изображение не удалось загрузить.")
        else:
            print(f"Файл изображения не найден по пути: {image_path1}")

        painter.setFont(QFont('Arial', 12))

        # Перенос текста с помощью TextWordWrap
        painter.drawText(60, 130, 230, 200, Qt.TextFlag.TextWordWrap,
                         "На старой заброшенной станции часы остановились, как если бы время решило замерзнуть навсегда. ")
        painter.drawText(60, 425, 230, 200, Qt.TextFlag.TextWordWrap,
                        "Особенно если они печатают интервью со знаменитостями или, в крайнем случае, программу телевидения на неделю. ")

        painter.drawText(310, 300, 180, 200, Qt.TextFlag.TextWordWrap,
                         "Судьба вчерашних газет незавидна. В первой половине ХХ века люди попроще делали из них самокрутки, именовавшиеся из-за своей формы «козьими ножками»."
                         "Помните, как бравый Швейк авторитетно признавал")
        painter.drawText(510, 130, 180, 200, Qt.TextFlag.TextWordWrap,
                         "полезность для солдат ящиков, куда складывают прочитанные газеты? "
                         "Песчаные дюны простирались до горизонта, создавая иллюзию бескрайности, где небо встречается с землей..")
class GraphicsSceneWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графическая сцена")
        self.setGeometry(100, 100, 1200, 600)  # Установите ширину 1200 и высоту 600

        layout = QVBoxLayout()

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 1000, 500)  # Установите размеры сцены
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(10, 10, 1170, 570)  # Размеры представления

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
        # Прямоугольник
        rect = QGraphicsRectItem(50, 50, 100, 100)
        rect.setBrush(QBrush(QColor("yellow")))
        rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        rect.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.scene.addItem(rect)

        # Круг (исправляем ошибку)
        ellipse = QGraphicsEllipseItem(400, 100, 100, 100)
        ellipse.setBrush(QBrush(QColor("blue")))
        ellipse.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        ellipse.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.scene.addItem(ellipse)

        # Треугольник
        triangle = QGraphicsPolygonItem(QPolygonF([QPointF(200, 50), QPointF(250, 150), QPointF(150, 150)]))
        triangle.setBrush(QBrush(QColor("red")))
        self.scene.addItem(triangle)

        # Текст
        text_item = QGraphicsTextItem("жижужа")
        text_item.setPos(100, 200)
        text_item.setDefaultTextColor(QColor("black"))
        self.scene.addItem(text_item)

        # Изображение
        image_path = "4.png"  # Убедитесь, что путь к изображению корректный
        image_item = QGraphicsPixmapItem(QPixmap.fromImage(QImage(image_path)))
        image_item.setPos(50, 400)
        image_item.setFlag(QGraphicsPixmapItem.GraphicsItemFlag.ItemIsMovable)
        image_item.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.scene.addItem(image_item)

        # Группа объектов
        rect_group = QGraphicsRectItem(300, 400, 50, 50)
        rect_group.setBrush(QBrush(QColor("orange")))
        ellipse_group = QGraphicsEllipseItem(400, 400, 50, 50)
        ellipse_group.setBrush(QBrush(QColor("white")))

        self.group = QGraphicsItemGroup()
        self.group.addToGroup(rect_group)
        self.group.addToGroup(ellipse_group)
        self.group.setFlag(QGraphicsItemGroup.GraphicsItemFlag.ItemIsMovable)
        self.scene.addItem(self.group)

    def add_control_buttons(self, layout):
        resize_scene_button = QPushButton("Изменить размеры сцены")
        resize_scene_button.clicked.connect(self.resize_scene)
        layout.addWidget(resize_scene_button)

        reset_view_button = QPushButton("Сброс масштаба")
        reset_view_button.clicked.connect(self.reset_view)
        layout.addWidget(reset_view_button)

        center_element_button = QPushButton("Центрировать элемент")
        center_element_button.clicked.connect(self.center_element)
        layout.addWidget(center_element_button)

        show_element_button = QPushButton("Показать элемент")
        show_element_button.clicked.connect(self.show_element)
        layout.addWidget(show_element_button)

        rotate_element_button = QPushButton("Повернуть элемент")
        rotate_element_button.clicked.connect(self.rotate_element)
        layout.addWidget(rotate_element_button)

        resize_element_button = QPushButton("Изменить размер элемента")
        resize_element_button.clicked.connect(self.resize_element)
        layout.addWidget(resize_element_button)

        toggle_visibility_button = QPushButton("Сделать элемент видимым/невидимым")
        toggle_visibility_button.clicked.connect(self.toggle_visibility)
        layout.addWidget(toggle_visibility_button)

        move_element_button = QPushButton("Переместить элемент")
        move_element_button.clicked.connect(self.move_element)
        layout.addWidget(move_element_button)

        toggle_movable_button = QPushButton("Запретить/разрешить перемещение")
        toggle_movable_button.clicked.connect(self.toggle_movable)
        layout.addWidget(toggle_movable_button)

        effect1_button = QPushButton("Добавить/убрать эффект 1")
        effect1_button.clicked.connect(self.toggle_effect1)
        layout.addWidget(effect1_button)

        effect2_button = QPushButton("Добавить/убрать эффект 2")
        effect2_button.clicked.connect(self.toggle_effect2)
        layout.addWidget(effect2_button)

        group_button = QPushButton("Группировать")
        group_button.clicked.connect(self.group_items)
        layout.addWidget(group_button)

        ungroup_button = QPushButton("Разгруппировать")
        ungroup_button.clicked.connect(self.ungroup_items)
        layout.addWidget(ungroup_button)

    def on_mouse_click(self, event):
        scene_pos = self.view.mapToScene(event.pos())
        item = self.scene.itemAt(scene_pos, self.view.transform())

        if item:
            if item in self.selected_items:
                self.selected_items.remove(item)
                item.setSelected(False)
                item.setOpacity(1)
            else:
                self.selected_items.append(item)
                item.setSelected(True)
                item.setOpacity(0.5)

            if isinstance(item, QGraphicsPolygonItem):
                pen = item.pen()
                new_color = QColor("blue") if pen.color() != QColor("blue") else QColor("black")
                pen.setColor(new_color)
                item.setPen(pen)
            elif isinstance(item, QGraphicsTextItem):
                current_color = item.defaultTextColor()
                new_color = QColor("blue") if current_color != QColor("blue") else QColor("black")
                item.setDefaultTextColor(new_color)

    def resize_scene(self):
        current_rect = self.scene.sceneRect()
        new_rect = current_rect.adjusted(-50, -50, 50, 50)
        self.scene.setSceneRect(new_rect)
        self.view.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def reset_view(self):
        self.view.resetTransform()
        self.view.centerOn(self.scene.sceneRect().center())

    def center_element(self):
        selected_item = self.element_selector.currentText()
        if selected_item == "Прямоугольник":
            self.view.centerOn(self.scene.items()[0])  # Прямоугольник
        elif selected_item == "Круг":
            self.view.centerOn(self.scene.items()[1])  # Круг
        elif selected_item == "Треугольник":
            self.view.centerOn(self.scene.items()[2])  # Треугольник
        elif selected_item == "Текст":
            self.view.centerOn(self.scene.items()[3])  # Текст
        elif selected_item == "Изображение":
            self.view.centerOn(self.scene.items()[4])  # Изображение
        elif selected_item == "Группа":
            self.view.centerOn(self.group)  # Группа

    def show_element(self):
        self.view.centerOn(self.group)  # Центрируемся на группе объектов

    def rotate_element(self):
        selected_item = self.selected_items[0] if self.selected_items else None
        if selected_item:
            selected_item.setRotation(selected_item.rotation() + 45)  # Поворот на 45 градусов

    def resize_element(self):
        selected_item = self.selected_items[0] if self.selected_items else None
        if selected_item:
            scale_factor = 1.2  # Изменение размера на 20%
            selected_item.setScale(selected_item.scale() * scale_factor)

    def toggle_visibility(self):
        if self.group.isVisible():
            self.group.setVisible(False)
        else:
            self.group.setVisible(True)

    def move_element(self):
        selected_item = self.selected_items[0] if self.selected_items else None
        if selected_item:
            selected_item.setPos(selected_item.x() + 20, selected_item.y() + 20)  # Перемещаем элемент

    def toggle_movable(self):
        if self.group.flags() & QGraphicsItem.GraphicsItemFlag.ItemIsMovable:
            self.group.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        else:
            self.group.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)

    def toggle_effect1(self):
        if not self.group.graphicsEffect():
            effect = QGraphicsDropShadowEffect()
            effect.setBlurRadius(10)
            self.group.setGraphicsEffect(effect)
        else:
            self.group.setGraphicsEffect(None)

    def toggle_effect2(self):
        if not self.group.graphicsEffect():
            effect = QGraphicsBlurEffect()
            effect.setBlurRadius(5)
            self.group.setGraphicsEffect(effect)
        else:
            self.group.setGraphicsEffect(None)

    def group_items(self):
        if self.selected_items:
            group = QGraphicsItemGroup()
            for item in self.selected_items:
                group.addToGroup(item)
                item.setSelected(False)

            group.setFlag(QGraphicsItemGroup.GraphicsItemFlag.ItemIsMovable)

            # Применяем эффекты к группе
            blur_effect = QGraphicsBlurEffect()
            blur_effect.setBlurRadius(10)
            group.setGraphicsEffect(blur_effect)

            self.scene.addItem(group)
            self.selected_items.clear()
            self.selected_items.append(group)

    def ungroup_items(self):
        if self.selected_items and isinstance(self.selected_items[0], QGraphicsItemGroup):
            group = self.selected_items[0]
            items = group.childItems()

            for item in items:
                group.removeFromGroup(item)
                self.scene.addItem(item)
                item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
                item.setSelected(True)

            self.scene.removeItem(group)
            self.selected_items.clear()
            self.selected_items.extend(items)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
