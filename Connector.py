from PyQt5 import QtCore, QtWidgets, QtQml

class Connector(QtCore.QObject):
    thumbnailSignal = QtCore.pyqtSignal(name='thumbnailReload')
    updateProgressSignal = QtCore.pyqtSignal(QtCore.QPointF, name='updateProgess')

    def __init__(self, program, parent=None):
        super(Connector, self).__init__(parent)
        self.program = program

    def Init(self):
        self.root = self.program.engine.rootObjects()[0]

    # def thumbnailReload(self):
    #     self.thumbnailSignal.emit()