
vid_path = "D:/test_seq/test_explosion_v012.mp4"

import sys
import cv2
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSlider
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt, QTimer

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.video_capture = cv2.VideoCapture(vid_path)  # Replace with your video file path
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.toggle_playback)

        self.seek_slider = QSlider(Qt.Horizontal)
        self.seek_slider.setMinimum(0)
        self.seek_slider.setMaximum(int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT)))
        self.seek_slider.valueChanged.connect(self.seek_frame)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.seek_slider)

        main_widget = QWidget(self)
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.playing = False

        self.update_frame()

    def toggle_playback(self):
        if self.playing:
            self.timer.stop()
            self.play_button.setText("Play")
        else:
            self.timer.start(33)  # 30 FPS (approx. 33 ms per frame)
            self.play_button.setText("Pause")
        self.playing = not self.playing

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(q_image)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.view.setSceneRect(0, 0, width, height)
            self.seek_slider.setValue(int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES)))
        else:
            self.timer.stop()
            self.playing = False
            self.play_button.setEnabled(False)
            self.video_capture.release()

    def seek_frame(self, frame_index):
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        self.update_frame()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())


