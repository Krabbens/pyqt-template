from Models.HintResultList import HintResultList
from Models.AlbumsResultList import AlbumsResultList
from Connector import Connector
from PyQt5.QtCore import QCoreApplication, QUrl, pyqtSignal, QObject
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQml import qmlRegisterType, QQmlComponent
from Thread import Thread
from concurrent.futures import ThreadPoolExecutor as cf
from Models.PersonResultList import PersonResultList
from Models.Image import Image
import os
import ctypes
import json

class Callback(QObject):
    def __init__(self, program):
        QObject.__init__(self)
        self.program = program
        self.engine = None
        self.personList = PersonResultList()
        self.background = Image(self.program.fullPath)
        self.connector = Connector(self.program)
        self.threads = []
        self.threadId = 0

    def ManageThread(self, id):
        for pair in self.threads:
            if pair[0] == id:
                pair[1].terminate()
                self.threads.remove(pair)
                break

    @pyqtSlot()
    def Exit(self):
        os._exit(0)

    @pyqtSlot()
    def Minimize(self):
        poly_window = ctypes.windll.user32.FindWindowW(None, "polyflow")
        ctypes.windll.user32.ShowWindow(poly_window, 6)