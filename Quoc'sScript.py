# import sys
# from PyQt5 import QtGui, QtCore
# from PyQt5.QtGui import QSound
# import random
# ​
#
# class PyAudioPylerGUI(QWidget):
#     filepath = ""
#
#     def __init__(self):
#         super().__init__()
#         self.qsound = None
#         self.init_ui()
#         self.show()
#
# ​
#
# def init_ui(self):
#     self.setGeometry(100, 100, 250, 250)
#     grid = QGridLayout()
#     self.setWindowTitle('PyQt AudioPlayer with QSound')
#
# ​
# # grid.setSpacing(10)
# button_play = QPushButton("Play")
# button_stop = QPushButton("Stop")
# button_exit = QPushButton("Exit")
# button_dialog = QPushButton("Open audio-file")
# button_next = QPushButton("Next")
# button_next = QPushButton("Next")
# ​
# self.label = QLabel(self)
# ​
# grid.addWidget(button_dialog, 0, 0, 1, 2)
# grid.addWidget(button_play, 1, 0)
# grid.addWidget(button_stop, 1, 1)
# grid.addWidget(button_exit, 2, 0, 1, 2)
# grid.addWidget(self.label, 3, 0, 1, 2)
# ​
# button_dialog.clicked.connect(self.button_openfile)
# button_play.clicked.connect(self.button_play)
# button_stop.clicked.connect(self.button_stop)
# button_exit.clicked.connect(self.button_exit)
# button_next.clicked.connect(self.)
#
#
# self.setLayout(grid)
# ​
#
# def button_exit(self):
#     QApplication.quit()
#
# ​
#
# def button_play(self):
#     if self.qsound is not None:
#         self.qsound.play()
#     # if self.player is not None:
#     #     self.player.play()
#
#
# def button_stop(self):
#     if self.qsound is not None:
#         self.qsound.stop()
#     # print(self.player.volume())
#     # self.player.setVolume(self.player.volume()-10)
#     # print(self.player.position())
#
#
# def button_openfile(self):
#     filepath, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Audio files (*.wav)")
#     filepath = os.path.abspath(filepath)
#
#     self.qsound = QSound(filepath)
#     self.player = QMediaPlayer()
#     self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filepath)))
#
# ​
# ​
# self.filename = os.path.basename(filepath)
# self.label.setText(self.filename)
# self.label.adjustSize()
# ​
#
# def button_next(self):
#     entries = os.listdir()
#     while (true):
#         if (len(entries) == 0):
#             break
#
#         newfile = entries.pop(entries.[random.randrange(0, len(entries))])
#         check = newfile[len(entries) - 3, len(entries)]
#         if (check == "wav" or check == "mp3"):
#             filepath = os.path.dirname(filepath)
#             filepath += newfile
#             break;
#
#     self.qsound = QSound(filepath)
#     self.player = QMediaPlayer()
#     self.player.setMedia(QmediaContent(QUrl.fromLocalFile(filepath)))
#
#     self.filename = os.path.basename(filepath)
#     self.label.setText(self.filename)
#     self.label.adjustSize()
#
# ​
# ​
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = PyAudioPylerGUI()
#     app.exit(app.exec_())