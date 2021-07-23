from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QWidget, QHBoxLayout, QLabel, QPushButton, QSpacerItem, \
    QGroupBox, QTreeView, QTextEdit, QLineEdit, QApplication, QFileDialog, QSlider
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QSize, Qt, QTimer, QTime, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon, QFont
import os


class Ui_Form(QWidget):

    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Music Player CC")
        Form.resize(500, 272)
        Form.setWindowTitle("Music Player CC")
        Form.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff87ff, stop:1 #87ffeb);")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(30, 0, 30, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MusicLogo = QPushButton(Form)
        self.MusicLogo.setMinimumSize(QSize(60, 60))
        self.MusicLogo.setStyleSheet("background : transparent")
        self.MusicLogo.setText("")
        self.MusicLogo.setObjectName("MusicLogo")
        self.horizontalLayout.addWidget(self.MusicLogo)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.MusicTitle = QLabel()
        font = QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.MusicTitle.setFont(font)
        self.MusicTitle.setObjectName("MusicTitle")
        self.horizontalLayout.addWidget(self.MusicTitle)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.FileFinder = QPushButton(Form)
        self.FileFinder.setMinimumSize(QSize(20, 50))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FileFinder.setFont(font)
        self.FileFinder.setStyleSheet("background : transparent")
        self.FileFinder.setObjectName("FileFinder")
        self.horizontalLayout.addWidget(self.FileFinder)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(30, 20, 0, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #############################################
        self.ProgressSlider = QSlider()
        self.ProgressSlider.setOrientation(Qt.Horizontal)
        self.ProgressSlider.setObjectName("ProgressSlider")

        ###########################################

        self.horizontalLayout_2.addWidget(self.ProgressSlider)
        self.ProgressLabel = QLabel(Form)
        self.ProgressLabel.setObjectName("ProgressLabel")
        self.horizontalLayout_2.addWidget(self.ProgressLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(30, 20, 30, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PreviousButton = QPushButton(Form)
        self.PreviousButton.setMinimumSize(QSize(80, 50))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PreviousButton.setFont(font)
        self.PreviousButton.setObjectName("PreviousButton")
        self.horizontalLayout_3.addWidget(self.PreviousButton)
        self.PauseButton = QPushButton(Form)
        self.PauseButton.setMinimumSize(QSize(80, 50))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PauseButton.setFont(font)
        self.PauseButton.setObjectName("PauseButton")
        self.horizontalLayout_3.addWidget(self.PauseButton)
        self.PlayButton = QPushButton(Form)
        self.PlayButton.setMinimumSize(QSize(80, 50))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PlayButton.setFont(font)
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout_3.addWidget(self.PlayButton)
        self.ForwardButton = QPushButton(Form)
        self.ForwardButton.setMinimumSize(QSize(80, 50))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ForwardButton.setFont(font)
        self.ForwardButton.setObjectName("ForwardButton")
        self.horizontalLayout_3.addWidget(self.ForwardButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.VolumeSlider = QSlider()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy)
        self.VolumeSlider.setOrientation(Qt.Vertical)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayout_5.addWidget(self.VolumeSlider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.VolumeLogo = QPushButton(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeLogo.sizePolicy().hasHeightForWidth())
        self.VolumeLogo.setSizePolicy(sizePolicy)
        self.VolumeLogo.setMinimumSize(QSize(20, 20))
        self.VolumeLogo.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.VolumeLogo)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        ###################################################
        self.song_title = None
        self.song_location = None

        self.player = QMediaPlayer()
        self.position = 0
        self.timer = QTimer()
        self.playlist = []
        self.current_song_index = None
        if not os.path.exists("../music"):
            os.mkdir("../music")
        self.music_folder = "music"
        if os.path.exists("../music_file.txt"):
            save_file = open("../music_file.txt", "r")
            data = save_file.read().split("\t")
            self.music_folder = data[0]
            print(self.music_folder)
            self.button_openfile(self.music_folder, int(data[1]))

        ##############
        # Set Icons ##
        ##############
        self.PlayButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/play.png"))
        self.PlayButton.setIconSize(QSize(60, 60))
        self.PlayButton.setStyleSheet("QPushButton{background:transparent;}")
        self.PlayButton.pressed.connect(
            lambda: self.PlayButton.setIcon(QIcon("../Assets/music player assets/music player assets/pressed/play.png")))
        self.PlayButton.released.connect(
            lambda: self.PlayButton.setIcon(QIcon(
                "../Assets/music player assets/music player assets/unpressed/play.png")))
        self.PauseButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/pause.png"))
        self.PauseButton.setIconSize(QSize(60, 60))
        self.PauseButton.setStyleSheet("QPushButton{background:transparent;}")
        self.PauseButton.pressed.connect(
            lambda: self.PauseButton.setIcon(QIcon(
                "../Assets/music player assets/music player assets/pressed/pause.png")))
        self.PauseButton.released.connect(
            lambda: self.PauseButton.setIcon(
                QIcon("../Assets/music player assets/music player assets/unpressed/pause.png")))
        self.ForwardButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/right_skip.png"))
        self.ForwardButton.setIconSize(QSize(60, 60))
        self.ForwardButton.setStyleSheet("QPushButton{background:transparent;}")
        self.ForwardButton.pressed.connect(
            lambda: self.ForwardButton.setIcon(
                QIcon("../Assets/music player assets/music player assets/pressed/right_skip.png")))
        self.ForwardButton.released.connect(
            lambda: self.ForwardButton.setIcon(
                QIcon("../Assets/music player assets/music player assets/unpressed/right_skip.png")))
        self.PreviousButton.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/left_skip.png"))
        self.PreviousButton.setIconSize(QSize(60, 60))
        self.PreviousButton.setStyleSheet("QPushButton{background:transparent;}")
        self.PreviousButton.pressed.connect(
            lambda: self.PreviousButton.setIcon(
                QIcon("../Assets/music player assets/music player assets/pressed/left_skip.png")))
        self.PreviousButton.released.connect(
            lambda: self.PreviousButton.setIcon(
                QIcon("../Assets/music player assets/music player assets/unpressed/left_skip.png")))
        self.FileFinder.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/menu.png"))
        self.FileFinder.setIconSize(QSize(60, 60))
        self.FileFinder.setStyleSheet("QPushButton{background:transparent;}")
        self.MusicLogo.setIcon(QIcon("../Assets/music player assets/music player assets/unpressed/music_note.png"))
        self.MusicLogo.setIconSize(QSize(60, 60))
        self.MusicLogo.setStyleSheet("QPushButton{background:transparent;}")
        self.VolumeLogo.setIcon(QIcon("../Assets/music player assets/music player assets/others/volume_icon.png"))
        self.VolumeLogo.setIconSize(QSize(30, 30))
        self.VolumeLogo.setStyleSheet("QPushButton{background:transparent;}")
        self.MusicTitle.setStyleSheet("background:transparent;")
        self.ProgressLabel.setStyleSheet("background:transparent;")
        ########################################

        self.player.setVolume(30)
        self.VolumeSlider.setValue(self.player.volume())
        self.ProgressSlider.setMaximum(5000)
        # self.timer.start(50)
        self.timer.timeout.connect(
            lambda: [self.ProgressSlider.blockSignals(True),
                     self.ProgressSlider.setValue(
                        self.player.position() / self.player.duration() * self.ProgressSlider.maximum() if self.player.duration() != 0 else 0),
                     self.ProgressSlider.blockSignals(False),
                     self.update_progress_label()])

        self.PlayButton.clicked.connect(self.button_play)
        self.PauseButton.clicked.connect(self.button_stop)
        self.PreviousButton.clicked.connect(self.button_previous)
        self.ForwardButton.clicked.connect(self.button_next)
        self.VolumeSlider.valueChanged.connect(lambda: self.player.setVolume(self.VolumeSlider.value()))
        self.ProgressSlider.valueChanged.connect(
            lambda: [self.player.setPosition(int(self.ProgressSlider.value() / self.ProgressSlider.maximum() * self.player.duration())),
                     self.update_progress_label])
        self.FileFinder.clicked.connect(self.button_openfile)

        self.ProgressSlider.setStyleSheet("QSlider{background : transparent}"
                                          "QSlider::groove:horizontal "
                                          "{"
                                          # "border: 1px solid #999999;"
                                          "height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */"
                                          "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff00fb, stop:1 #00fff7);"
                                          "margin: 2px 0;"
                                          "border-radius: 3px;"
                                          "}"
                                          "QSlider::handle:horizontal "
                                          "{"
                                          "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);"
                                          # "border: 1px solid #5c5c5c;"
                                          "width: 18px;"
                                          "margin: -4px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */"
                                          "border-radius: 5px;"
                                          "}"
                                          "QSlider::add-page:horizontal "
                                          "{"
                                          "background: white;"
                                          "margin: 2px 0;"
                                          "border-radius: 3px;"
                                          "height: 8px;"
                                          "}"
                                          )


        self.VolumeSlider.setStyleSheet("QSlider{background : transparent}"
                                        "QSlider::groove:vertical "
                                        "{"
                                        "background: #00fff7;"
                                        # "position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */"
                                        "left: 7px; right: 7px;"
                                        "border-radius: 3px;"
                                        "}"
                                        "QSlider::handle:vertical "
                                        "{"
                                        "height: 10px;"
                                        "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);"
                                        "margin: 0 -4px; /* expand outside the groove */"
                                        "border-radius: 4px;"
                                        "}"
                                        "QSlider::add-page:vertical {"
                                        "background: 8f8f8f;"
                                        "left: 7px; right: 7px;"
                                        "border-radius: 3px;"
                                        "}"
                                        "QSlider::sub-page:vertical {"
                                        "background: white;"
                                        "left: 7px; right: 7px;"
                                        "border-radius: 3px;"
                                        "}"
                                        )

    def update_progress_label(self):
        # print(QTime(0, 0, msec=self.player.position()).toString("mm:ss"))
        time = self.player.position()
        currentTime = QTime(0, time / 1000 // 60 % 60, time // 1000 % 60).toString("mm:ss")
        duration = QTime(0, self.player.duration() / 1000 // 60 % 60, self.player.duration() // 1000 % 60).toString("mm:ss")
        self.ProgressLabel.setText(currentTime + "/" + duration)

        if currentTime == duration and duration != "00:00":
            self.button_next()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MusicTitle.setText(_translate("Form", "MusicTitle"))
        self.ProgressLabel.setText(_translate("Form", "00:00/00:00"))

    def button_play(self):
        if self.current_song_index is None:
            self.SetSongAtPath(None)
        if self.position == 0:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.playlist[self.current_song_index])))

        self.timer.start(50)
        self.SetSongAtPath(self.playlist[self.current_song_index])
        self.position = self.ProgressSlider.value() / self.ProgressSlider.maximum() * self.player.duration()
        self.player.setPosition(int(self.position))
        self.player.play()
        save_file = open("../music_file.txt", "w")
        save_file.write(self.music_folder + "\t" + str(self.current_song_index))

    def button_stop(self):
        if self.player is not None:
            self.position = self.player.position()
            self.player.stop()
            self.timer.stop()
        self.player.setPosition(self.position)

    def button_openfile(self, filePath=None, index=None):
        print(filePath)
        if not filePath:
            filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', self.music_folder, "Audio files (*.wav *.mp3)")
        if filePath:
            self.SetSongAtPath(filePath)
            self.playlist.clear()
            entries = os.listdir(self.music_folder)
            for file in entries:
                if file[-4:] in [".wav", ".mp3"]:
                    self.playlist.append(os.path.abspath(self.music_folder + "/" + file))
            if index:
                self.current_song_index = index
                self.SetSongAtPath(self.playlist[index])
            else:
                self.current_song_index = 0

        save_file = open("../music_file.txt", "w")
        save_file.write(self.music_folder + "\t" + str(self.current_song_index))

    def button_next(self):
        NewPath = ""
        if len(self.playlist) == 0:
            entries = os.listdir(self.music_folder)
            for file in entries:
                if file[-4:] in [".wav", ".mp3"]:
                    self.playlist.append(os.path.abspath(self.music_folder + "/" + file))

        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        NewPath = self.playlist[self.current_song_index]
        print(NewPath)

        self.SetSongAtPath(NewPath)
        self.position = 0
        self.ProgressSlider.setValue(0)
        self.button_play()

    def button_previous(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
        NewPath = self.playlist[self.current_song_index]
        print(NewPath)

        self.SetSongAtPath(NewPath)
        self.position = 0
        self.ProgressSlider.setValue(0)
        self.button_play()

    def SetSongAtPath(self, filePath):
        if filePath is None:
            self.song_location = None
            self.MusicTitle.setText("Select Music")
            self.timer.stop()
        else:
            self.song_location = os.path.abspath(filePath)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.song_location)))
            title = os.path.basename(self.song_location).split('.')[0]
            font = QFont()
            font.setFamily("Segoe Print")
            font.setBold(True)
            font.setWeight(75)
            if 24 > len(title) > 12:
                title = title[0:12] + "\n" + title[12:]
                font.setPointSize(22)
                font.setWeight(60)
            elif len(title) > 24:
                title = title[0:12] + "\n" + title[12:20] + "..."
                font.setPointSize(22)
                font.setWeight(60)
            else:
                font.setPointSize(28)
                font.setWeight(75)
            self.MusicTitle.setFont(font)
            self.MusicTitle.setText(title)
            self.update_progress_label()
            if os.path.isfile(filePath):
                self.music_folder = os.path.dirname(filePath)
            else:
                self.music_folder = os.path.abspath(filePath)

        # self.position = 0
        # self.ProgressSlider.setValue(0)
        print(self.music_folder)
        # self.player.play()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())
