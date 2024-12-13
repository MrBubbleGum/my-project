from PyQt6 import QtGui, QtWidgets, QtCore
import sys
import time
# Функция для загрузки данных
def load_data(splash):
    for i in range(1, 11):  # Имитируем процесс загрузки
        time.sleep(1)
        splash.showMessage(f"{i * 10}%",
                           QtCore.Qt.AlignmentFlag.AlignHCenter |
                           QtCore.Qt.AlignmentFlag.AlignBottom,
                           QtCore.Qt.GlobalColor.black)
        # Принудительно обрабатываем события
        QtWidgets.QApplication.instance().processEvents()
# Функция для создания главного окна
def create_main_window():
    main_window = QtWidgets.QWidget()
    # Создаем надпись с текстом
    label = QtWidgets.QLabel(
        "Лабораторная работа №1\n"
        "Введение в PyQt 6\n"
        "Выполнил студент группы ИТИ-21\n"
        "Важная Яна Ивановна", main_window
    )
    label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # центрировать
    # фотка
    image_label = QtWidgets.QLabel(main_window)
    pixmap = QtGui.QPixmap("lim.png")
    image_label.setPixmap(pixmap)
    image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # центрировать
    # Создаем кнопку для закрытия окна
    button = QtWidgets.QPushButton("Закрыть окно", main_window)
    button.clicked.connect(QtWidgets.QApplication.instance().quit)
    # Размещаем виджеты в вертикальном компоновщике
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(image_label)
    layout.addWidget(button)
    main_window.setLayout(layout)
    main_window.setWindowTitle("Лабораторная работа №1")
    main_window.resize(400, 400)
    return main_window
# Основная функция
def main():
    app = QtWidgets.QApplication(sys.argv)
    # Создаем заставку
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("lim.png"))
    splash.showMessage("0%",
                       QtCore.Qt.AlignmentFlag.AlignHCenter |
                       QtCore.Qt.AlignmentFlag.AlignBottom,
                       QtGui.QColor("black"))
    splash.show()
    # Принудительно обрабатываем события
    QtWidgets.QApplication.instance().processEvents()
    # Загрузка данных
    load_data(splash)
    # Создаем и показываем основное окно
    main_window = create_main_window()
    main_window.show()
    # Закрываем заставку
    splash.finish(main_window)
    sys.exit(app.exec())
if __name__ == "__main__":
    main()