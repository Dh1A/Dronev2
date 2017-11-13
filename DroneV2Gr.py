import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import CopterGUIv2
from time import sleep

import serial

ser = serial.Serial('/dev/ttyACM0', 115200)



throttle = 0
Yaw = 128
Pitch = 125
Roll = 132

index = 0
SendF = 0

Vals = []

Delays =[]

class MainG (QtGui.QMainWindow ,CopterGUIv2.Ui_MainWindow):



    def __init__(self, parent = None ):
        super(MainG, self).__init__(parent)
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.threadclass.start()
        self.Init()





        ##ControlledFlight##
        self.ThrottleHIGH.pressed.connect(self.ThrottleUP)
        self.ThrottleLOW.pressed.connect(self.ThrottleDOWN)
        self.YawHigh.pressed.connect(self.YawUP)
        self.YawLOW.pressed.connect(self.YawDOWN)
        self.YawReset.pressed.connect(self.Yawreset)

        self.PitchHIGH.pressed.connect(self.PitchUP)
        self.PitchLOW.pressed.connect(self.PitchDOWN)
        self.RollHIGH.pressed.connect(self.RollUP)
        self.RollLOW.pressed.connect(self.RollDOWN)
        self.PitchRollReset.pressed.connect(self.PitchRollreset)

        self.connect(self.threadclass, QtCore.SIGNAL('Bound'), self.Bounded)
        self.connect(self.threadclass, QtCore.SIGNAL('Alt'), self.Alt)
        self.connect(self.threadclass, QtCore.SIGNAL('Bat'), self.Batt)
        self.connect(self.threadclass, QtCore.SIGNAL('Angle'), self.Ang)
        self.connect(self.threadclass, QtCore.SIGNAL('Debug'), self.Debug)




        ##Binding##
        self.BindBUtton.pressed.connect(self.BindingS)

        ##AutomatedFlight##
        self.ThrottleUpA.pressed.connect(self.DialValLim)
        self.ThrottleDownA.pressed.connect(self.DialValLim)
        self.YawUpA.pressed.connect(self.DialValLim)
        self.YawDownA.pressed.connect(self.DialValLim)
        self.RollUpA.pressed.connect(self.DialValLim)
        self.RollDownA.pressed.connect(self.DialValLim)
        self.PitchUpA.pressed.connect(self.DialValLim)
        self.PitchDownA.pressed.connect(self.DialValLim)

        self.RecButton.pressed.connect(self.RecAction)
        self.RunButton.pressed.connect(self.Execution)



    def Init(self):
        self.Debug1.setText("Initialising...")
        sleep(0.5)
        self.Debug1.setText("Controller initialised")
        sleep(0.5)
        self.Debug1.setText("Waiting For Copters")


    def hexcut(self,s,n):
        return s[n:]

    def RadioWrite(self,com,Value):

        if self.Copter1.isChecked():
            ser.write('01'+com+str(Value)+'\r\n')
        if self.Copter2.isChecked():
            ser.write('02' + com + str(Value) + '\r\n')
        if self.Copter3.isChecked():
            ser.write('03' + com + str(Value) + '\r\n')
        if self.Copter4.isChecked():
            ser.write('04' + com + str(Value) + '\r\n')
        if self.Copter5.isChecked():
            ser.write('05' + com + str(Value) + '\r\n')
        if self.Copter6.isChecked():
            ser.write('06' + com + str(Value) + '\r\n')


                ##AutomatedFlight##

    def RadioWriteAuto (self,Value):

        if self.Copter1A.isChecked():
            ser.write('01' + Value)
        if self.Copter2A.isChecked():
            ser.write('02' + Value)
        if self.Copter3A.isChecked():
            ser.write('03' + Value)
        if self.Copter4A.isChecked():
            ser.write('04' + Value)
        if self.Copter5A.isChecked():
            ser.write('05' + Value)
        if self.Copter6A.isChecked():
            ser.write('06' + Value)


    def DialValLim(self):

        if (self.ThrottleUpA.isChecked() or self.ThrottleDownA.isChecked()):
            self.ValueD.setMaximum(255)
            self.ValueD.setMinimum(0)

        if (self.YawUpA.isChecked() or self.YawDownA.isChecked()):
            self.ValueD.setMaximum(204)
            self.ValueD.setMinimum(52)


        if (self.PitchUpA.isChecked() or self.PitchDownA.isChecked()):
            self.ValueD.setMaximum(188)
            self.ValueD.setMinimum(62)

        if (self.RollUpA.isChecked() or self.RollDownA.isChecked()):
            self.ValueD.setMaximum(195)
            self.ValueD.setMinimum(69)




    def RecVal(self,val):
        global Vals,index

        if (self.ThrottleUpA.isChecked() or self.ThrottleDownA.isChecked()):

            if val == 0:
                Vals.append('0200'+'\r\n')
            else:

                ThrottleHex = hex(val)
                throttleTs = self.hexcut(str(ThrottleHex), 2)
                Vals.append ('02'+ str(throttleTs)+ '\r\n')




        if (self.YawUpA.isChecked() or self.YawDownA.isChecked()):

            YawHex = hex(val)
            YawTs = self.hexcut(str(YawHex), 2)
            Vals.append( '03' + str(YawTs) + '\r\n')



        if (self.PitchUpA.isChecked() or self.PitchDownA.isChecked()):

            PitchHex = hex(val)
            PitchTs = self.hexcut(str(PitchHex), 2)
            Vals.append ('05' + str(PitchTs) + '\r\n')


        if (self.RollUpA.isChecked() or self.RollDownA.isChecked()):

            RollHex = hex(val)
            RollTs = self.hexcut(str(RollHex), 2)
            Vals.append ('04' + str(RollTs) + '\r\n')



    def RecTime(self,Val):
        global Delays,index

        Delays.append (Val)

    def RecAction(self):
        global index,Vals,Delays
        self.RecVal(self.ValueDisp.intValue())
        self.RecTime(self.TimeDisplay.intValue())

        self.RECval1.setText("Action Recorded")
        self.RECval1_2.setText(str(index))
        self.RECval1_3.setText(Vals[index])
        self.RECval1_4.setText(str(Delays[index]))
        index = index + 1

    def Execution(self):
        global Delays,index,Vals,SendF

        for i in range(len(Vals)):
            while True:



                self.RadioWriteAuto(Vals[i])
                self.RECval1.setText("Sending...")
                self.RECval1_2.setText(str(index))
                self.RECval1_3.setText(Vals[i])
                self.RECval1_4.setText(str(Delays[i]))


                if SendF :
                    self.RECval1.setText("CommandSent")
                    break
            sleep (Delays[i])









            ##ControlledFlight##

    def Alt(self,x):

        self.Altitude.display(x)

    def Batt(self, x):

        self.Battery.display(x)


    def Ang(self, x):

        self.Angle.display(x)



    def Debug(self,x):
        global SendF
        if x == 1:
            self.Debug1.setText('Command sent')
            SendF = 1
        if x == 0:
            self.Debug1.setText('Command not sent')
            SendF = 0






    def ThrottleUP(self):
        global throttle
        throttle = throttle + 1
        if throttle > 255:
            throttle = 255
        self.Thrust.display(throttle)
        self.Debug1.setText('Throttle_up'+str(throttle))
        ThrottleHex = hex(throttle)
        throttleTs = self.hexcut(str(ThrottleHex),2)
        self.RadioWrite("02", throttleTs)





    def ThrottleDOWN(self):
        global throttle
        throttle = throttle -1
        if throttle < 0:
            throttle = 0
            self.RadioWrite("02", "00")
            self.Thrust.display(throttle)
            self.Debug1.setText('Throttle_Down' + str(throttle))
        else:
            self.Thrust.display(throttle)
            self.Debug1.setText('Throttle_Down' + str(throttle))
            ThrottleHex = hex(throttle)
            throttleTs = self.hexcut(str(ThrottleHex), 2)
            self.RadioWrite("02", throttleTs)





    def YawUP(self):
        global Yaw
        Yaw = Yaw +1
        if Yaw > 204:
            Yaw = 204
        self.Yaw.display(Yaw)
        self.Debug1.setText('Yaw_UP' + str(Yaw))
        YawHex = hex(Yaw)
        YawHexTs = self.hexcut(str(YawHex), 2)
        self.RadioWrite("03", YawHexTs)




    def YawDOWN(self):
        global Yaw
        Yaw = Yaw - 1
        if Yaw < 52:
            Yaw = 52
        self.Yaw.display(Yaw)
        self.Debug1.setText('Yaw_Down' + str(Yaw))
        YawHex = hex(Yaw)
        YawHexTs = self.hexcut(str(YawHex), 2)
        self.RadioWrite("03", YawHexTs)




    def Yawreset(self):
        global Yaw
        Yaw = 128
        self.Yaw.display(Yaw)
        self.Debug1.setText('Yaw_Reset' + str(Yaw))
        YawHex = hex(Yaw)
        YawHexTs = self.hexcut(str(YawHex), 2)
        self.RadioWrite("03", YawHexTs)



    def PitchUP(self):
        global Pitch
        Pitch = Pitch+1
        if Pitch > 188:
            Pitch =188
        self.Pitch.display(Pitch)
        self.Debug1.setText('Pitch_Up' + str(Pitch))
        PitchHex = hex(Pitch)
        PitchHexTs = self.hexcut(str(PitchHex), 2)
        self.RadioWrite("05", PitchHexTs)



    def PitchDOWN(self):
        global Pitch
        Pitch = Pitch-1
        if Pitch < 62:
            Pitch = 62
        self.Pitch.display(Pitch)
        self.Debug1.setText('Pitch_Down' + str(Pitch))
        PitchHex = hex(Pitch)
        PitchHexTs = self.hexcut(str(PitchHex), 2)
        self.RadioWrite("05", PitchHexTs)




    def RollUP(self):
        global Roll
        Roll = Roll + 1
        if Roll > 195:
            Roll = 195
        self.Roll.display(Roll)
        self.Debug1.setText('Roll_Up' + str(Roll))

        RollHex = hex(Roll)
        RollHexTs = self.hexcut(str(RollHex), 2)
        self.RadioWrite("04", RollHexTs)



    def RollDOWN(self):
        global Roll
        Roll = Roll - 1
        if Roll < 69:
            Roll = 69
        self.Roll.display(Roll)
        self.Debug1.setText('Roll_Down' + str(Roll))

        RollHex = hex(Roll)
        RollHexTs = self.hexcut(str(RollHex), 2)
        self.RadioWrite("04", RollHexTs)



    def PitchRollreset(self):

        global Pitch,Roll

        Roll = 132
        Pitch = 125
        self.Roll.display(Roll)
        self.Pitch.display(Pitch)
        self.Debug1.setText('Pitch_Roll_Reset' + str(Roll))


        RollHex = hex(Roll)
        RollHexTs = self.hexcut(str(RollHex), 2)
        self.RadioWrite("04", RollHexTs)


        PitchHex = hex(Pitch)
        PitchHexTs = self.hexcut(str(PitchHex), 2)
        self.RadioWrite("05", PitchHexTs)




##Binding##

    def BindingS(self):
        ser.write("000101 ")


    def Bounded(self,a):
        if a == 1:
            self.Debug2.setText("Copter Bound")
            self.Debug1.setText("Copter Bound")
            x = self.Coptersbounded.intValue()
            x = x + 1
            self.Coptersbounded.display(x)

        if a == 2:
            self.Debug2.setText("Copter Bound")

            x = self.Coptersbounded.intValue()
            x = x + 1
            self.Coptersbounded.display(x)



class ThreadClass(QtCore.QThread) :
    def __init__(self, parent= None):
        super(ThreadClass, self).__init__(parent)



    def run(self):
        global SendF


        while 1:
            if ser.isOpen():

                DEBUG = ser.readline()
                

                if int(DEBUG) == 1 :
                    self.emit(QtCore.SIGNAL('Bound'), 1)
                if int(DEBUG) == 2:
                    self.emit(QtCore.SIGNAL('Bound'), 2)
                if int(DEBUG) == 0:
                    SendF = 1
                    self.emit(QtCore.SIGNAL('Debug'), 1)
                if int(DEBUG) == 11:
                    SendF = 0
                    self.emit(QtCore.SIGNAL('Debug'), 0)

                else :
                    Telem = int(float(DEBUG))


                    if  Telem >= 1000  and Telem < 2000:
                        Telem = Telem-1000
                        self.emit(QtCore.SIGNAL('Alt'), Telem)
                    if Telem >= 2000  and Telem < 3000:
                        Telem = Telem - 2000
                        self.emit(QtCore.SIGNAL('Bat'), Telem)
                    if Telem >= 3000  and Telem < 4000:
                        Telem = Telem - 3000
                        self.emit(QtCore.SIGNAL('Angle'), Telem)












a =QtGui.QApplication(sys.argv)

app = MainG()
app.show()

a.exec_()
