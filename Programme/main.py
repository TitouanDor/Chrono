### Importation ###
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
import os
import ctypes
import pygame

localPath = os.path.dirname(os.path.abspath(__file__))

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        self.setWindowTitle("Chrono")
        self.windowContent = QWidget()
        self.setCentralWidget(self.windowContent)
        loadUi(localPath + "/page.ui", self.windowContent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.windowContent.startButton.clicked.connect(self.start)
        self.windowContent.stackedWidget.setCurrentIndex(0)
        self.windowContent.stopButton.clicked.connect(self.stop)
        
    
    def stop(self):
        global fin
        fin = False
        self.windowContent.stackedWidget.setCurrentIndex(0)



    def start(self):
        global liste
        global fin
        fin = False
        self.windowContent.stackedWidget.setCurrentIndex(1)
        time = self.windowContent.timeEdit.time()
        liste = [time.hour(), time.minute(), time.second()]
        self.windowContent.textHeure.setText(misEnForme(liste))
        self.timer = QTimer(window)
        self.timer.timeout.connect(running)
        self.timer.start(1000)
        self.timer2 = QTimer(window)
        self.timer2.timeout.connect(son)
        self.timer2.start(10)
        

def misEnForme(temps):
    Text = f"{temps[0]}H {temps[1]} min {temps[2]} sec"
    return Text

def son():
    global fin
    global muse
    play = muse.get_busy()
    if fin and not play:
        muse.play

def running():
    global fin
    if not fin:
        if liste[2] == 0:
            if liste[1] == 0:
                if liste[0] == 0:
                    fin = True
                    print("Fin")
                else: 
                    liste[0] -= 1
                if not fin: liste[1] = 59
            else: liste[1] -= 1
            if not fin: liste[2] = 59
        else:
            liste[2] -= 1

        window.windowContent.textHeure.setText(misEnForme(liste))


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    liste = []
    fin = False
    muse = pygame.mixer.music
    muse.load(localPath + "/sonnerie.mp3")
    os.system("cls")
    app = QApplication([])
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QIcon(localPath + "/../logo.jpg"))
    window = MainPage()
    window.show() 
    app.exec_()