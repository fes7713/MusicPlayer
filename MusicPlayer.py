# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(800, 400)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 0, 511, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(30, 20, 30, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MusicLogo = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.MusicLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MusicLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MusicLogo.setObjectName("MusicLogo")
        self.horizontalLayout.addWidget(self.MusicLogo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.MusicTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MusicTitle.setFont(font)
        self.MusicTitle.setObjectName("MusicTitle")
        self.horizontalLayout.addWidget(self.MusicTitle)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.FileFinder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.FileFinder.setMinimumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FileFinder.setFont(font)
        self.FileFinder.setObjectName("FileFinder")
        self.horizontalLayout.addWidget(self.FileFinder)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(30, 5, 0, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ProgressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.ProgressBar.setProperty("value", 24)
        self.ProgressBar.setObjectName("ProgressBar")
        self.horizontalLayout_2.addWidget(self.ProgressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(30, 20, 30, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PreviousButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PreviousButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PreviousButton.setFont(font)
        self.PreviousButton.setObjectName("PreviousButton")
        self.horizontalLayout_3.addWidget(self.PreviousButton)
        self.PauseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PauseButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PauseButton.setFont(font)
        self.PauseButton.setObjectName("PauseButton")
        self.horizontalLayout_3.addWidget(self.PauseButton)
        self.PlayButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PlayButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PlayButton.setFont(font)
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout_3.addWidget(self.PlayButton)
        self.ForwardButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ForwardButton.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ForwardButton.setFont(font)
        self.ForwardButton.setObjectName("ForwardButton")
        self.horizontalLayout_3.addWidget(self.ForwardButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MusicTitle.setText(_translate("Form", "MusicTitle"))
        self.FileFinder.setText(_translate("Form", "Files"))
        self.PreviousButton.setText(_translate("Form", "Prev"))
        self.PauseButton.setText(_translate("Form", "Pause"))
        self.PlayButton.setText(_translate("Form", "Play"))
        self.ForwardButton.setText(_translate("Form", "Forw"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())