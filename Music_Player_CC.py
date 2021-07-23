from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QFileDialog
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtMultimedia import QSound, QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
import os
import random

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(500, 272)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(30, 0, 30, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MusicLogo = QtWidgets.QPushButton(Form)
        self.MusicLogo.setMinimumSize(QtCore.QSize(60, 60))
        self.MusicLogo.setStyleSheet("background : transparent")
        self.MusicLogo.setText("")
        self.MusicLogo.setObjectName("MusicLogo")
        self.horizontalLayout.addWidget(self.MusicLogo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.MusicTitle = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.MusicTitle.setFont(font)
        self.MusicTitle.setObjectName("MusicTitle")
        self.horizontalLayout.addWidget(self.MusicTitle)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.FileFinder = QtWidgets.QPushButton(Form)
        self.FileFinder.setMinimumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FileFinder.setFont(font)
        self.FileFinder.setStyleSheet("background : transparent")
        self.FileFinder.setObjectName("FileFinder")
        self.horizontalLayout.addWidget(self.FileFinder)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(30, 20, 0, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(30, 20, 30, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PreviousButton = QtWidgets.QPushButton(Form)
        self.PreviousButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PreviousButton.setFont(font)
        self.PreviousButton.setObjectName("PreviousButton")
        self.horizontalLayout_3.addWidget(self.PreviousButton)
        self.PauseButton = QtWidgets.QPushButton(Form)
        self.PauseButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PauseButton.setFont(font)
        self.PauseButton.setObjectName("PauseButton")
        self.horizontalLayout_3.addWidget(self.PauseButton)
        self.PlayButton = QtWidgets.QPushButton(Form)
        self.PlayButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PlayButton.setFont(font)
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout_3.addWidget(self.PlayButton)
        self.ForwardButton = QtWidgets.QPushButton(Form)
        self.ForwardButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ForwardButton.setFont(font)
        self.ForwardButton.setObjectName("ForwardButton")
        self.horizontalLayout_3.addWidget(self.ForwardButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.VolumeSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy)
        self.VolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayout_5.addWidget(self.VolumeSlider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.VolumeLogo = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeLogo.sizePolicy().hasHeightForWidth())
        self.VolumeLogo.setSizePolicy(sizePolicy)
        self.VolumeLogo.setMinimumSize(QtCore.QSize(20, 20))
        self.VolumeLogo.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.VolumeLogo)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.song_title = None
        self.player = None

        ##############
        # Set Icons ##
        ##############
        self.PlayButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/play.png"))
        self.PlayButton.setIconSize(QSize(60, 60))
        self.PlayButton.setStyleSheet("QPushButton{background:transparent;}")
        self.PauseButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/pause.png"))
        self.PauseButton.setIconSize(QSize(60, 60))
        self.PauseButton.setStyleSheet("QPushButton{background:transparent;}")
        self.ForwardButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/right_skip.png"))
        self.ForwardButton.setIconSize(QSize(60, 60))
        self.ForwardButton.setStyleSheet("QPushButton{background:transparent;}")
        self.PreviousButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/left_skip.png"))
        self.PreviousButton.setIconSize(QSize(60, 60))
        self.PreviousButton.setStyleSheet("QPushButton{background:transparent;}")
        self.FileFinder.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/menu.png"))
        self.FileFinder.setIconSize(QSize(60, 60))
        self.FileFinder.setStyleSheet("QPushButton{background:transparent;}")
        self.MusicLogo.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/music_note.png"))
        self.MusicLogo.setIconSize(QSize(60, 60))
        self.MusicLogo.setStyleSheet("QPushButton{background:transparent;}")
        self.VolumeLogo.setIcon(QIcon("../Assets/music player assets/music player assets/others/volume_icon.png"))
        self.VolumeLogo.setIconSize(QSize(30, 30))
        self.VolumeLogo.setStyleSheet("QPushButton{background:transparent;}")
        ####


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MusicTitle.setText(_translate("Form", "MusicTitle"))
        # self.FileFinder.setText(_translate("Form", "Files"))
        self.label.setText(_translate("Form", "00:00/03:00"))
        # self.PreviousButton.setText(_translate("Form", "Prev"))
        # self.PauseButton.setText(_translate("Form", "Pause"))
        # self.PlayButton.setText(_translate("Form", "Play"))
        # self.ForwardButton.setText(_translate("Form", "Next"))

    def button_play(self):
        # if self.qsound is not None:
        #     self.qsound.play()
        if self.player is not None:
            self.player.play()

    def button_stop(self):
        if self.player is not None:
            self.player.stop()
        # print(self.player.volume())
        # self.player.setVolume(self.player.volume()-10)
        # print(self.player.position())

    def button_openfile(self, filePath=None):
        if filePath is None:
            filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Audio files (*.wav)")
            filePath = os.path.abspath(filePath)

        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filePath)))

        self.song_title = os.path.basename(filePath)




    # def button_next(self):
    #     entries = os.listdir()
    #     while (True):
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
    #     self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filepath)))
    #
    #     self.song = os.path.basename(filepath)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.setStyleSheet("background : gray")
    Form.show()
    sys.exit(app.exec_())
