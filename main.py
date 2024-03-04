from PyQt5.QtWidgets import *
from multiprocessing import Process
import os


CWD = os.getcwd()


class RadioButton(QRadioButton):
    def __init__(self):
        super(RadioButton, self).__init__()
        self.value = None

    def setValue(self, val):
        self.value = val

    def getValue(self):
        return self.value


class PushButton(QPushButton):
    def __init__(self):
        super(PushButton, self).__init__()
        self.value = None

    def setValue(self, val):
        self.value = val

    def getValue(self):
        return self.value


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.setGeometry(200,200,400,100) 
        self.setWindowTitle('App')
        
        radioPdf = RadioButton()
        radioPdf.setText('Esporta  .pdf')
        radioPdf.setValue(0)
        radioPdf.clicked.connect(lambda: self.swapFileTypeSelection(radioPdf.getValue()))

        radioDocx = RadioButton()
        radioDocx.setText('Esporta  .docx')
        radioDocx.setValue(1)
        radioDocx.clicked.connect(lambda: self.swapFileTypeSelection(radioDocx.getValue()))

        btnGroup = QButtonGroup()
        btnGroup.setExclusive(True)
        btnGroup.addButton(radioPdf)
        btnGroup.addButton(radioDocx)

        descrPdf = QLabel('Impiega più tempo,\n estrae anche immagini')
        descrDocx = QLabel('Impiega meno tempo,\n non estrae immagini')
        
        self.btnSelectPdf = PushButton()
        self.btnSelectPdf.setText('Select PDF')
        self.btnSelectPdf.setValue(0)
        self.btnSelectPdf.clicked.connect(lambda: self.browseFiles(self.btnSelectPdf.getValue()))
        self.pathToPdf = QLabel()
        
        VLPdf = QVBoxLayout()
        VLPdf.addWidget(self.btnSelectPdf)
        VLPdf.addWidget(self.pathToPdf)

        self.btnSelectDocx = PushButton()
        self.btnSelectDocx.setText('Select DOCX')
        self.btnSelectDocx.setValue(1)
        self.btnSelectDocx.clicked.connect(lambda: self.browseFiles(self.btnSelectDocx.getValue()))
        self.pathToDocx = QLabel()

        VLDocx = QVBoxLayout()
        VLDocx.addWidget(self.btnSelectDocx)
        VLDocx.addWidget(self.pathToDocx)

        self.btnEnter = PushButton()
        self.btnEnter.setText('GO!')

        GLayout = QGridLayout()
        GLayout.addWidget(radioPdf, 0,0)
        GLayout.addWidget(radioDocx, 0,1)
        GLayout.addWidget(descrPdf, 1,0)
        GLayout.addWidget(descrDocx, 1,1)
        GLayout.addLayout(VLPdf, 2,0)
        GLayout.addLayout(VLDocx, 2,1)
        GLayout.addWidget(self.btnEnter, 3,0,1,0)

        radioPdf.setChecked(True)
        self.btnSelectDocx.setEnabled(False)
        self.btnEnter.setValue(0)
        self.btnEnter.setEnabled(False)

        widget = QWidget()
        widget.setLayout(GLayout)
        self.setCentralWidget(widget)


    def swapFileTypeSelection(self, val):
        # chiudere il problema degli eventi multipli
        # penso che questo problema sia risolto
        match val:
            case 0:
                self.btnSelectDocx.setEnabled(False)
                self.btnSelectPdf.setEnabled(False)
                self.btnSelectPdf.setEnabled(True)
                self.pathToPdf.clear()
                self.pathToDocx.clear()
                try:
                    self.btnEnter.clicked.disconnect()
                except:
                    print('[EXCEPT TRIGGERED] event dupe prevented')
                self.btnEnter.setEnabled(False)
                self.btnEnter.setValue(0)

            case 1:
                self.btnSelectDocx.setEnabled(False)
                self.btnSelectDocx.setEnabled(True)
                self.btnSelectPdf.setEnabled(False)
                self.pathToPdf.clear()
                self.pathToDocx.clear()
                try:
                    self.btnEnter.clicked.disconnect()
                except:
                    print('[EXCEPT TRIGGERED] event dupes prevented')
                self.btnEnter.setEnabled(False)
                self.btnEnter.setValue(1)
    

    def browseFiles(self, val):
        if self.btnEnter.isEnabled():
            self.btnEnter.clicked.disconnect()
        match val:
            case 0:
                fname = QFileDialog.getOpenFileName(self, 'Open File', CWD, 'PDF Files (*.pdf)')
                if fname[0] != '':
                    self.pathToPdf.setText('File selected!')
                    self.btnEnter.setEnabled(True)
                    self.btnEnter.clicked.connect(lambda: self.on_click(fname[0]))
            case 1:
                fname = QFileDialog.getOpenFileName(self, 'Open File', CWD, 'DOCX Files (*.docx)')
                if fname[0] != '':
                    self.pathToDocx.setText('File selected!')
                    self.btnEnter.setEnabled(True)
                    self.btnEnter.clicked.connect(lambda: self.on_click(fname[0]))


    def on_click(self, text):
        match self.btnEnter.getValue():
            case 0:
                process = Process(target=self.task(text))
                process.start()
                process.join()
                os.system(f'docker exec unstruct python3 pyqt_project/scriptPdf.py')

            case 1:
                process = Process(target=self.task(text))
                process.start()
                process.join()
                os.system(f'docker exec unstruct python3 pyqt_project/scriptDocx.py')


    def task(self, path):
        os.system(f'cp "{path}" {CWD}/utils')

####################################################################################################################à

def main():
    gui = QApplication([])
    window = AppWindow()
    window.show()
    gui.exec()

if __name__=='__main__':
    main()