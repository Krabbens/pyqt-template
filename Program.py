import os
from PyQt5.QtCore import QMetaObject, QUrl, pyqtSignal, pyqtSlot, QObject, Qt
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent
from Callback import Callback
import sys
import json

class Program(QObject):
    def __init__(self, app):
        QObject.__init__(self)
        self.engine = None
        self.app = app
        self.fullPath = os.path.dirname(os.path.realpath(__file__))
        self.callback = Callback(self)
        self.Initialize()
        if self.engine != None: self.Run()
        

    def Initialize(self):
        self.engine = QQmlApplicationEngine()
        ctx = self.engine.rootContext()
        ctx.setContextProperty('callback', self.callback)
        ctx.setContextProperty('connector', self.callback.connector)
        self.engine.load("main.qml")
        self.callback.connector.Init()

    def Run(self):
        pass