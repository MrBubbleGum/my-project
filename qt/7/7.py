import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog,
                             QSlider, QMessageBox, QTextEdit, QHBoxLayout)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
import os
from PyQt6.QtPrintSupport import QPrintDialog, QPrinter, QPageSetupDialog, QPrintPreviewDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вероника Ковалёва - ИТИ-21")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        label = QLabel(
            "Лабораторная работа №7\nМультимедиа. Печать документов.\nВыполнил студент группы ИТИ-21\nВероника Ковалёва")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        button_audio = QPushButton("Аудиоплеер")
        button_audio.setToolTip("Открыть окно аудиоплеера")
        button_audio.clicked.connect(self.open_audio_player)

        button_video = QPushButton("Видеоплеер")
        button_video.setToolTip("Открыть окно видеоплеера")
        button_video.clicked.connect(self.open_video_player)

        button_print = QPushButton("Печать документов")
        button_print.setToolTip("Открыть окно печати документов")
        button_print.clicked.connect(self.open_print_window)

        layout.addWidget(button_audio)
        layout.addWidget(button_video)
        layout.addWidget(button_print)

    def open_audio_player(self):
        self.audio_window = AudioPlayerWindow()
        self.audio_window.show()

    def open_video_player(self):
        self.video_window = MediaPlayerWindow()
        self.video_window.show()

    def open_print_window(self):
        self.print_window = PrintWindow()
        self.print_window.show()

class AudioPlayerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Аудиоплеер")
        layout = QVBoxLayout(self)

        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        self.info_label = QLabel("Информация о файле: Нет файла")
        open_file_btn = QPushButton("Открыть файл")
        open_file_btn.clicked.connect(self.open_file)

        self.position_slider = QSlider(Qt.Orientation.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)

        control_layout = QHBoxLayout()

        rewind_btn = QPushButton("<<")
        rewind_btn.setStyleSheet("border-radius: 25px; background-color: lightgray; padding: 10px;")
        rewind_btn.clicked.connect(self.rewind_audio)

        pause_btn = QPushButton("||")
        pause_btn.setStyleSheet("border-radius: 25px; background-color: lightgray; padding: 10px;")
        pause_btn.clicked.connect(self.pause_audio)

        forward_btn = QPushButton(">>")
        forward_btn.setStyleSheet("border-radius: 25px; background-color: lightgray; padding: 10px;")
        forward_btn.clicked.connect(self.forward_audio)

        control_layout.addWidget(rewind_btn)
        control_layout.addWidget(pause_btn)
        control_layout.addWidget(forward_btn)

        volume_slider = QSlider(Qt.Orientation.Horizontal)
        volume_slider.setToolTip("Громкость")
        volume_slider.setRange(0, 100)
        volume_slider.setValue(50)
        volume_slider.valueChanged.connect(self.change_volume)

        layout.addWidget(self.info_label)
        layout.addWidget(open_file_btn)
        layout.addLayout(control_layout)
        layout.addWidget(QLabel("Громкость:"))
        layout.addWidget(volume_slider)

        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть аудиофайл", "", "Audio Files (*.mp3 *.wav)")
        if file_name:
            self.media_player.setSource(QUrl.fromLocalFile(file_name))
            self.media_player.play()
            file_info = os.path.basename(file_name)
            self.info_label.setText(f"Информация о файле: {file_info}")

    def rewind_audio(self):
        current_time = self.media_player.position()
        self.media_player.setPosition(max(0, current_time - 5000))

    def forward_audio(self):
        current_time = self.media_player.position()
        self.media_player.setPosition(current_time + 5000)

    def pause_audio(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        elif self.media_player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
            self.media_player.play()

    def change_volume(self, value):
        self.audio_output.setVolume(value / 100)

    def update_position(self, position):
        self.position_slider.setValue(position)

    def update_duration(self, duration):
        self.position_slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def closeEvent(self, event):
        self.media_player.stop()
        event.accept()

class MediaPlayerWindow(QWidget):
    def __init__(self, parent=None):
        super(MediaPlayerWindow, self).__init__(parent)
        self.setWindowTitle("Мультимедиа Проигрыватель")
        self.resize(800, 600)

        layout = QVBoxLayout(self)
        self.open_button = QPushButton("Открыть файл")
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        self.position_slider = QSlider(Qt.Orientation.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)

        control_layout = QHBoxLayout()
        self.play_button = QPushButton("Пуск")
        self.play_button.clicked.connect(self.play)
        control_layout.addWidget(self.play_button)

        rewind_btn = QPushButton("<<")
        rewind_btn.setStyleSheet("border-radius: 25px; background-color: lightgray; padding: 10px;")
        rewind_btn.clicked.connect(self.rewind_video)
        control_layout.addWidget(rewind_btn)

        self.pause_button = QPushButton("||")
        self.pause_button.setStyleSheet("border-radius: 25px; background-color: lightgray; padding: 10px;")
        self.pause_button.clicked.connect(self.pause)
        control_layout.addWidget(self.pause_button)

        forward_btn = QPushButton(">>")
        forward_btn.setStyleSheet("border-radius: 25px; background-color: lightgray; padding: 10px;")
        forward_btn.clicked.connect(self.forward_video)
        control_layout.addWidget(forward_btn)

        layout.addLayout(control_layout)

        volume_layout = QHBoxLayout()
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)
        volume_layout.addWidget(QLabel("Громкость:"))
        volume_layout.addWidget(self.volume_slider)
        layout.addLayout(volume_layout)

        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)

    def set_volume(self, volume):
        self.audio_output.setVolume(volume / 100)

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Открыть видеофайл", "", "Видео файлы (*.mp4 *.avi *.mkv)")
        if file_path:
            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.media_player.play()

    def play(self):
        self.media_player.play()

    def pause(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        elif self.media_player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
            self.media_player.play()

    def rewind_video(self):
        current_time = self.media_player.position()
        self.media_player.setPosition(max(0, current_time - 5000))

    def forward_video(self):
        current_time = self.media_player.position()
        self.media_player.setPosition(current_time + 5000)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_position(self, position):
        self.position_slider.setValue(position)

    def update_duration(self, duration):
        self.position_slider.setRange(0, duration)

    def closeEvent(self, event):
        self.media_player.stop()
        event.accept()

class PrintWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Печать документов")
        layout = QVBoxLayout(self)

        self.text_viewer = QTextEdit()
        self.text_viewer.setReadOnly(True)

        open_file_btn = QPushButton("Открыть файл")
        open_file_btn.clicked.connect(self.open_file)

        page_setup_btn = QPushButton("Настройка страницы")
        page_setup_btn.clicked.connect(self.page_setup)

        preview_btn = QPushButton("Просмотр")
        preview_btn.clicked.connect(self.preview)

        print_btn = QPushButton("Печать")
        print_btn.clicked.connect(self.print_document)

        export_pdf_btn = QPushButton("Экспорт в PDF")
        export_pdf_btn.clicked.connect(self.export_to_pdf)

        layout.addWidget(self.text_viewer)
        layout.addWidget(open_file_btn)
        layout.addWidget(page_setup_btn)
        layout.addWidget(preview_btn)
        layout.addWidget(print_btn)
        layout.addWidget(export_pdf_btn)

        self.printer = QPrinter()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть документ", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_viewer.setText(content)
            QMessageBox.information(self, "Файл открыт", f"Файл: {os.path.basename(file_name)}")

    def page_setup(self):
        dialog = QPageSetupDialog(self.printer, self)
        dialog.exec()

    def preview(self):
        preview_dialog = QPrintPreviewDialog(self.printer, self)
        preview_dialog.paintRequested.connect(self.text_viewer.print)
        preview_dialog.exec()

    def print_document(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec():
            self.text_viewer.print(self.printer)

    def export_to_pdf(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Экспорт в PDF", "", "PDF Files (*.pdf)")
        if file_name:
            self.printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            self.printer.setOutputFileName(file_name)
            self.text_viewer.print(self.printer)
            QMessageBox.information(self, "Экспорт", "Документ успешно экспортирован в PDF")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(400, 300)
    main_window.show()
    sys.exit(app.exec())