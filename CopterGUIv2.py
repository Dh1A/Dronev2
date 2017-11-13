# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dhia\Desktop\copterv2\copterv2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 480))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(52, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)

        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.ControledFlight = QtGui.QWidget()
        self.ControledFlight.setObjectName(_fromUtf8("ControledFlight"))
        self.label = QtGui.QLabel(self.ControledFlight)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 433))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("controlscreen.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.YawReset = QtGui.QPushButton(self.ControledFlight)
        self.YawReset.setGeometry(QtCore.QRect(68, 160, 81, 71))
        self.YawReset.setText(_fromUtf8(""))
        self.YawReset.setIconSize(QtCore.QSize(25, 23))
        self.YawReset.setFlat(True)
        self.YawReset.setObjectName(_fromUtf8("YawReset"))
        self.PitchRollReset = QtGui.QPushButton(self.ControledFlight)
        self.PitchRollReset.setGeometry(QtCore.QRect(647, 160, 91, 81))
        self.PitchRollReset.setText(_fromUtf8(""))
        self.PitchRollReset.setIconSize(QtCore.QSize(25, 23))
        self.PitchRollReset.setFlat(True)
        self.PitchRollReset.setObjectName(_fromUtf8("PitchRollReset"))
        self.Copter1 = QtGui.QCheckBox(self.ControledFlight)
        self.Copter1.setGeometry(QtCore.QRect(250, 166, 16, 17))
        self.Copter1.setText(_fromUtf8(""))
        self.Copter1.setIconSize(QtCore.QSize(25, 23))
        self.Copter1.setTristate(False)
        self.Copter1.setObjectName(_fromUtf8("Copter1"))
        self.Copter2 = QtGui.QCheckBox(self.ControledFlight)
        self.Copter2.setGeometry(QtCore.QRect(430, 166, 16, 17))
        self.Copter2.setText(_fromUtf8(""))
        self.Copter2.setIconSize(QtCore.QSize(25, 23))
        self.Copter2.setTristate(False)
        self.Copter2.setObjectName(_fromUtf8("Copter2"))
        self.Copter3 = QtGui.QCheckBox(self.ControledFlight)
        self.Copter3.setGeometry(QtCore.QRect(250, 229, 16, 17))
        self.Copter3.setText(_fromUtf8(""))
        self.Copter3.setIconSize(QtCore.QSize(25, 23))
        self.Copter3.setTristate(False)
        self.Copter3.setObjectName(_fromUtf8("Copter3"))
        self.Copter4 = QtGui.QCheckBox(self.ControledFlight)
        self.Copter4.setGeometry(QtCore.QRect(430, 228, 16, 17))
        self.Copter4.setText(_fromUtf8(""))
        self.Copter4.setIconSize(QtCore.QSize(25, 23))
        self.Copter4.setTristate(False)
        self.Copter4.setObjectName(_fromUtf8("Copter4"))
        self.Copter5 = QtGui.QCheckBox(self.ControledFlight)
        self.Copter5.setGeometry(QtCore.QRect(250, 292, 16, 17))
        self.Copter5.setText(_fromUtf8(""))
        self.Copter5.setIconSize(QtCore.QSize(25, 23))
        self.Copter5.setTristate(False)
        self.Copter5.setObjectName(_fromUtf8("Copter5"))
        self.Copter6 = QtGui.QCheckBox(self.ControledFlight)
        self.Copter6.setGeometry(QtCore.QRect(430, 292, 16, 17))
        self.Copter6.setText(_fromUtf8(""))
        self.Copter6.setIconSize(QtCore.QSize(25, 23))
        self.Copter6.setTristate(False)
        self.Copter6.setObjectName(_fromUtf8("Copter6"))
        self.Altitude = QtGui.QLCDNumber(self.ControledFlight)
        self.Altitude.setGeometry(QtCore.QRect(26, 49, 151, 31))
        self.Altitude.setFrameShape(QtGui.QFrame.NoFrame)
        self.Altitude.setFrameShadow(QtGui.QFrame.Sunken)
        self.Altitude.setLineWidth(3)
        self.Altitude.setDigitCount(5)
        self.Altitude.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Altitude.setProperty("intValue", 0)
        self.Altitude.setObjectName(_fromUtf8("Altitude"))
        self.Battery = QtGui.QLCDNumber(self.ControledFlight)
        self.Battery.setGeometry(QtCore.QRect(310, 50, 151, 31))
        self.Battery.setFrameShape(QtGui.QFrame.NoFrame)
        self.Battery.setFrameShadow(QtGui.QFrame.Sunken)
        self.Battery.setLineWidth(3)
        self.Battery.setDigitCount(5)
        self.Battery.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Battery.setProperty("intValue", 0)
        self.Battery.setObjectName(_fromUtf8("Battery"))
        self.Angle = QtGui.QLCDNumber(self.ControledFlight)
        self.Angle.setGeometry(QtCore.QRect(613, 50, 151, 31))
        self.Angle.setFrameShape(QtGui.QFrame.NoFrame)
        self.Angle.setFrameShadow(QtGui.QFrame.Sunken)
        self.Angle.setLineWidth(3)
        self.Angle.setDigitCount(5)
        self.Angle.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Angle.setProperty("intValue", 0)
        self.Angle.setObjectName(_fromUtf8("Angle"))
        self.Thrust = QtGui.QLCDNumber(self.ControledFlight)
        self.Thrust.setGeometry(QtCore.QRect(19, 326, 151, 31))
        self.Thrust.setFrameShape(QtGui.QFrame.NoFrame)
        self.Thrust.setFrameShadow(QtGui.QFrame.Sunken)
        self.Thrust.setLineWidth(3)
        self.Thrust.setDigitCount(5)
        self.Thrust.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Thrust.setProperty("intValue", 0)
        self.Thrust.setObjectName(_fromUtf8("Thrust"))
        self.Yaw = QtGui.QLCDNumber(self.ControledFlight)
        self.Yaw.setGeometry(QtCore.QRect(19, 387, 151, 31))
        self.Yaw.setFrameShape(QtGui.QFrame.NoFrame)
        self.Yaw.setFrameShadow(QtGui.QFrame.Sunken)
        self.Yaw.setLineWidth(3)
        self.Yaw.setDigitCount(5)
        self.Yaw.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Yaw.setProperty("intValue", 0)
        self.Yaw.setObjectName(_fromUtf8("Yaw"))
        self.Pitch = QtGui.QLCDNumber(self.ControledFlight)
        self.Pitch.setGeometry(QtCore.QRect(622, 329, 151, 31))
        self.Pitch.setFrameShape(QtGui.QFrame.NoFrame)
        self.Pitch.setFrameShadow(QtGui.QFrame.Sunken)
        self.Pitch.setLineWidth(3)
        self.Pitch.setDigitCount(5)
        self.Pitch.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Pitch.setProperty("intValue", 0)
        self.Pitch.setObjectName(_fromUtf8("Pitch"))
        self.Roll = QtGui.QLCDNumber(self.ControledFlight)
        self.Roll.setGeometry(QtCore.QRect(620, 389, 151, 31))
        self.Roll.setFrameShape(QtGui.QFrame.NoFrame)
        self.Roll.setFrameShadow(QtGui.QFrame.Sunken)
        self.Roll.setLineWidth(3)
        self.Roll.setDigitCount(5)
        self.Roll.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Roll.setProperty("intValue", 0)
        self.Roll.setObjectName(_fromUtf8("Roll"))
        self.PitchHIGH = QtGui.QPushButton(self.ControledFlight)
        self.PitchHIGH.setGeometry(QtCore.QRect(640, 90, 101, 51))
        self.PitchHIGH.setText(_fromUtf8(""))
        self.PitchHIGH.setAutoRepeat(True)
        self.PitchHIGH.setAutoRepeatDelay(300)
        self.PitchHIGH.setFlat(True)
        self.PitchHIGH.setObjectName(_fromUtf8("PitchHIGH"))
        self.PitchLOW = QtGui.QPushButton(self.ControledFlight)
        self.PitchLOW.setGeometry(QtCore.QRect(640, 250, 101, 51))
        self.PitchLOW.setText(_fromUtf8(""))
        self.PitchLOW.setAutoRepeat(True)
        self.PitchLOW.setAutoRepeatDelay(300)
        self.PitchLOW.setFlat(True)
        self.PitchLOW.setObjectName(_fromUtf8("PitchLOW"))
        self.ThrottleHIGH = QtGui.QPushButton(self.ControledFlight)
        self.ThrottleHIGH.setGeometry(QtCore.QRect(50, 100, 101, 51))
        self.ThrottleHIGH.setText(_fromUtf8(""))
        self.ThrottleHIGH.setAutoRepeat(True)
        self.ThrottleHIGH.setAutoRepeatDelay(300)
        self.ThrottleHIGH.setFlat(True)
        self.ThrottleHIGH.setObjectName(_fromUtf8("ThrottleHIGH"))
        self.ThrottleLOW = QtGui.QPushButton(self.ControledFlight)
        self.ThrottleLOW.setGeometry(QtCore.QRect(50, 250, 101, 51))
        self.ThrottleLOW.setText(_fromUtf8(""))
        self.ThrottleLOW.setAutoRepeat(True)
        self.ThrottleLOW.setAutoRepeatDelay(300)
        self.ThrottleLOW.setFlat(True)
        self.ThrottleLOW.setObjectName(_fromUtf8("ThrottleLOW"))
        self.YawHigh = QtGui.QPushButton(self.ControledFlight)
        self.YawHigh.setGeometry(QtCore.QRect(150, 160, 71, 81))
        self.YawHigh.setText(_fromUtf8(""))
        self.YawHigh.setAutoRepeat(True)
        self.YawHigh.setAutoRepeatDelay(300)
        self.YawHigh.setFlat(True)
        self.YawHigh.setObjectName(_fromUtf8("YawHigh"))
        self.YawLOW = QtGui.QPushButton(self.ControledFlight)
        self.YawLOW.setGeometry(QtCore.QRect(10, 150, 41, 91))
        self.YawLOW.setText(_fromUtf8(""))
        self.YawLOW.setAutoRepeat(True)
        self.YawLOW.setAutoRepeatDelay(300)
        self.YawLOW.setFlat(True)
        self.YawLOW.setObjectName(_fromUtf8("YawLOW"))
        self.RollLOW = QtGui.QPushButton(self.ControledFlight)
        self.RollLOW.setGeometry(QtCore.QRect(570, 160, 71, 81))
        self.RollLOW.setText(_fromUtf8(""))
        self.RollLOW.setAutoRepeat(True)
        self.RollLOW.setAutoRepeatDelay(300)
        self.RollLOW.setFlat(True)
        self.RollLOW.setObjectName(_fromUtf8("RollLOW"))
        self.RollHIGH = QtGui.QPushButton(self.ControledFlight)
        self.RollHIGH.setGeometry(QtCore.QRect(740, 150, 71, 81))
        self.RollHIGH.setText(_fromUtf8(""))
        self.RollHIGH.setAutoRepeat(True)
        self.RollHIGH.setAutoRepeatDelay(300)
        self.RollHIGH.setFlat(True)
        self.RollHIGH.setObjectName(_fromUtf8("RollHIGH"))
        self.Debug1 = QtGui.QLabel(self.ControledFlight)
        self.Debug1.setGeometry(QtCore.QRect(260, 370, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Debug1.setFont(font)
        self.Debug1.setText(_fromUtf8(""))
        self.Debug1.setTextFormat(QtCore.Qt.AutoText)
        self.Debug1.setObjectName(_fromUtf8("Debug1"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("controlicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.ControledFlight, icon, _fromUtf8(""))
        self.Binding = QtGui.QWidget()
        self.Binding.setObjectName(_fromUtf8("Binding"))
        self.label_2 = QtGui.QLabel(self.Binding)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 433))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("boundscreen.jpg")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BindBUtton = QtGui.QPushButton(self.Binding)
        self.BindBUtton.setGeometry(QtCore.QRect(330, 120, 171, 161))
        self.BindBUtton.setText(_fromUtf8(""))
        self.BindBUtton.setFlat(True)
        self.BindBUtton.setObjectName(_fromUtf8("BindBUtton"))
        self.Coptersbounded = QtGui.QLCDNumber(self.Binding)
        self.Coptersbounded.setGeometry(QtCore.QRect(20, 370, 151, 31))
        self.Coptersbounded.setFrameShape(QtGui.QFrame.NoFrame)
        self.Coptersbounded.setFrameShadow(QtGui.QFrame.Sunken)
        self.Coptersbounded.setLineWidth(3)
        self.Coptersbounded.setDigitCount(5)
        self.Coptersbounded.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Coptersbounded.setProperty("intValue", 0)
        self.Coptersbounded.setObjectName(_fromUtf8("Coptersbounded"))
        self.Debug2 = QtGui.QLabel(self.Binding)
        self.Debug2.setGeometry(QtCore.QRect(470, 370, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Debug2.setFont(font)
        self.Debug2.setText(_fromUtf8(""))
        self.Debug2.setTextFormat(QtCore.Qt.AutoText)
        self.Debug2.setObjectName(_fromUtf8("Debug2"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("bindico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Binding, icon1, _fromUtf8(""))
        self.AutomatedFlight = QtGui.QWidget()
        self.AutomatedFlight.setObjectName(_fromUtf8("AutomatedFlight"))
        self.label_3 = QtGui.QLabel(self.AutomatedFlight)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 800, 433))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("automate.jpg")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Copter3A = QtGui.QCheckBox(self.AutomatedFlight)
        self.Copter3A.setGeometry(QtCore.QRect(42, 118, 16, 17))
        self.Copter3A.setText(_fromUtf8(""))
        self.Copter3A.setIconSize(QtCore.QSize(25, 23))
        self.Copter3A.setTristate(False)
        self.Copter3A.setObjectName(_fromUtf8("Copter3A"))
        self.Copter1A = QtGui.QCheckBox(self.AutomatedFlight)
        self.Copter1A.setGeometry(QtCore.QRect(42, 65, 16, 16))
        self.Copter1A.setText(_fromUtf8(""))
        self.Copter1A.setIconSize(QtCore.QSize(25, 23))
        self.Copter1A.setTristate(False)
        self.Copter1A.setObjectName(_fromUtf8("Copter1A"))
        self.Copter5A = QtGui.QCheckBox(self.AutomatedFlight)
        self.Copter5A.setGeometry(QtCore.QRect(42, 171, 16, 17))
        self.Copter5A.setText(_fromUtf8(""))
        self.Copter5A.setIconSize(QtCore.QSize(25, 23))
        self.Copter5A.setTristate(False)
        self.Copter5A.setObjectName(_fromUtf8("Copter5A"))
        self.Copter4A = QtGui.QCheckBox(self.AutomatedFlight)
        self.Copter4A.setGeometry(QtCore.QRect(210, 65, 16, 17))
        self.Copter4A.setText(_fromUtf8(""))
        self.Copter4A.setIconSize(QtCore.QSize(25, 23))
        self.Copter4A.setTristate(False)
        self.Copter4A.setObjectName(_fromUtf8("Copter4A"))
        self.Copter2A = QtGui.QCheckBox(self.AutomatedFlight)
        self.Copter2A.setGeometry(QtCore.QRect(210, 118, 16, 17))
        self.Copter2A.setText(_fromUtf8(""))
        self.Copter2A.setIconSize(QtCore.QSize(25, 23))
        self.Copter2A.setTristate(False)
        self.Copter2A.setObjectName(_fromUtf8("Copter2A"))
        self.Copter6A = QtGui.QCheckBox(self.AutomatedFlight)
        self.Copter6A.setGeometry(QtCore.QRect(210, 171, 16, 17))
        self.Copter6A.setText(_fromUtf8(""))
        self.Copter6A.setIconSize(QtCore.QSize(25, 23))
        self.Copter6A.setTristate(False)
        self.Copter6A.setObjectName(_fromUtf8("Copter6A"))
        self.ValueD = QtGui.QDial(self.AutomatedFlight)
        self.ValueD.setGeometry(QtCore.QRect(353, 40, 231, 111))
        self.ValueD.setObjectName(_fromUtf8("ValueD"))
        self.TimeD = QtGui.QDial(self.AutomatedFlight)
        self.TimeD.setGeometry(QtCore.QRect(355, 253, 231, 111))
        self.TimeD.setObjectName(_fromUtf8("TimeD"))
        self.ValueDisp = QtGui.QLCDNumber(self.AutomatedFlight)
        self.ValueDisp.setGeometry(QtCore.QRect(390, 170, 151, 31))
        self.ValueDisp.setFrameShape(QtGui.QFrame.NoFrame)
        self.ValueDisp.setFrameShadow(QtGui.QFrame.Sunken)
        self.ValueDisp.setLineWidth(3)
        self.ValueDisp.setDigitCount(5)
        self.ValueDisp.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.ValueDisp.setProperty("intValue", 0)
        self.ValueDisp.setObjectName(_fromUtf8("ValueDisp"))
        self.TimeDisplay = QtGui.QLCDNumber(self.AutomatedFlight)
        self.TimeDisplay.setGeometry(QtCore.QRect(390, 382, 151, 31))
        self.TimeDisplay.setFrameShape(QtGui.QFrame.NoFrame)
        self.TimeDisplay.setFrameShadow(QtGui.QFrame.Sunken)
        self.TimeDisplay.setLineWidth(3)
        self.TimeDisplay.setDigitCount(5)
        self.TimeDisplay.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.TimeDisplay.setProperty("intValue", 0)
        self.TimeDisplay.setObjectName(_fromUtf8("TimeDisplay"))
        self.ThrottleUpA = QtGui.QCheckBox(self.AutomatedFlight)
        self.ThrottleUpA.setGeometry(QtCore.QRect(679, 93, 16, 17))
        self.ThrottleUpA.setText(_fromUtf8(""))
        self.ThrottleUpA.setObjectName(_fromUtf8("ThrottleUpA"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.ThrottleUpA)
        self.ThrottleDownA = QtGui.QCheckBox(self.AutomatedFlight)
        self.ThrottleDownA.setGeometry(QtCore.QRect(680, 150, 16, 17))
        self.ThrottleDownA.setText(_fromUtf8(""))
        self.ThrottleDownA.setObjectName(_fromUtf8("ThrottleDownA"))
        self.buttonGroup.addButton(self.ThrottleDownA)
        self.YawUpA = QtGui.QCheckBox(self.AutomatedFlight)
        self.YawUpA.setGeometry(QtCore.QRect(710, 121, 16, 17))
        self.YawUpA.setText(_fromUtf8(""))
        self.YawUpA.setObjectName(_fromUtf8("YawUpA"))
        self.buttonGroup.addButton(self.YawUpA)
        self.YawDownA = QtGui.QCheckBox(self.AutomatedFlight)
        self.YawDownA.setGeometry(QtCore.QRect(648, 122, 16, 17))
        self.YawDownA.setText(_fromUtf8(""))
        self.YawDownA.setObjectName(_fromUtf8("YawDownA"))
        self.buttonGroup.addButton(self.YawDownA)
        self.RollUpA = QtGui.QCheckBox(self.AutomatedFlight)
        self.RollUpA.setGeometry(QtCore.QRect(710, 321, 16, 17))
        self.RollUpA.setText(_fromUtf8(""))
        self.RollUpA.setObjectName(_fromUtf8("RollUpA"))
        self.buttonGroup.addButton(self.RollUpA)
        self.PitchUpA = QtGui.QCheckBox(self.AutomatedFlight)
        self.PitchUpA.setGeometry(QtCore.QRect(679, 293, 16, 17))
        self.PitchUpA.setText(_fromUtf8(""))
        self.PitchUpA.setObjectName(_fromUtf8("PitchUpA"))
        self.buttonGroup.addButton(self.PitchUpA)
        self.RollDownA = QtGui.QCheckBox(self.AutomatedFlight)
        self.RollDownA.setGeometry(QtCore.QRect(648, 322, 16, 17))
        self.RollDownA.setText(_fromUtf8(""))
        self.RollDownA.setObjectName(_fromUtf8("RollDownA"))
        self.buttonGroup.addButton(self.RollDownA)
        self.PitchDownA = QtGui.QCheckBox(self.AutomatedFlight)
        self.PitchDownA.setGeometry(QtCore.QRect(680, 350, 16, 17))
        self.PitchDownA.setText(_fromUtf8(""))
        self.PitchDownA.setObjectName(_fromUtf8("PitchDownA"))
        self.buttonGroup.addButton(self.PitchDownA)
        self.RecButton = QtGui.QPushButton(self.AutomatedFlight)
        self.RecButton.setGeometry(QtCore.QRect(41, 257, 51, 51))
        self.RecButton.setText(_fromUtf8(""))
        self.RecButton.setFlat(True)
        self.RecButton.setObjectName(_fromUtf8("RecButton"))
        self.RunButton = QtGui.QPushButton(self.AutomatedFlight)
        self.RunButton.setGeometry(QtCore.QRect(40, 350, 51, 51))
        self.RunButton.setText(_fromUtf8(""))
        self.RunButton.setFlat(True)
        self.RunButton.setObjectName(_fromUtf8("RunButton"))
        self.RECval1 = QtGui.QLabel(self.AutomatedFlight)
        self.RECval1.setGeometry(QtCore.QRect(126, 240, 181, 31))
        self.RECval1.setFrameShape(QtGui.QFrame.Box)
        self.RECval1.setText(_fromUtf8(""))
        self.RECval1.setObjectName(_fromUtf8("RECval1"))
        self.RECval1_2 = QtGui.QLabel(self.AutomatedFlight)
        self.RECval1_2.setGeometry(QtCore.QRect(126, 272, 181, 31))
        self.RECval1_2.setFrameShape(QtGui.QFrame.Box)
        self.RECval1_2.setText(_fromUtf8(""))
        self.RECval1_2.setObjectName(_fromUtf8("RECval1_2"))
        self.RECval1_3 = QtGui.QLabel(self.AutomatedFlight)
        self.RECval1_3.setGeometry(QtCore.QRect(126, 304, 181, 31))
        self.RECval1_3.setFrameShape(QtGui.QFrame.Box)
        self.RECval1_3.setText(_fromUtf8(""))
        self.RECval1_3.setObjectName(_fromUtf8("RECval1_3"))
        self.RECval1_4 = QtGui.QLabel(self.AutomatedFlight)
        self.RECval1_4.setGeometry(QtCore.QRect(126, 336, 181, 31))
        self.RECval1_4.setFrameShape(QtGui.QFrame.Box)
        self.RECval1_4.setText(_fromUtf8(""))
        self.RECval1_4.setObjectName(_fromUtf8("RECval1_4"))
        self.RECval1_5 = QtGui.QLabel(self.AutomatedFlight)
        self.RECval1_5.setGeometry(QtCore.QRect(126, 368, 181, 31))
        self.RECval1_5.setFrameShape(QtGui.QFrame.Box)
        self.RECval1_5.setText(_fromUtf8(""))
        self.RECval1_5.setObjectName(_fromUtf8("RECval1_5"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("autoicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.AutomatedFlight, icon2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.ValueD, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.ValueDisp.display)
        QtCore.QObject.connect(self.TimeD, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.TimeDisplay.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ControledFlight), _translate("MainWindow", "Controlled Flight", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Binding), _translate("MainWindow", "Binding", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AutomatedFlight), _translate("MainWindow", "Automated Flight", None))

