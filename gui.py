import sys
from PyPDF2 import PdfFileMerger

from PyQt5.QtWidgets import *

arr = list()


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MergePDF')
        self.resize(300, 200)

        self.ledText = QLineEdit('Files', self)
        self.ledText.move(35, 30)

        self.btn = QPushButton('Open File', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_opn_btn_click)

        self.btn = QPushButton('Save File', self)
        self.btn.move(35, 70)
        self.btn.clicked.connect(self.evt_sv_btn_click)

    def evt_opn_btn_click(self):
        global arr
        res = QFileDialog.getOpenFileNames(self, 'Open File', '/', 'PDF File (*.pdf)')
        self.ledText.clear()
        print(type(res[0]))
        arr = res[0]
        # self.ledText.setText(res[0])

    @staticmethod
    def evt_sv_btn_click():
        print(arr)
        try:
            merger = PdfFileMerger
            for pdf in arr:
                merger.append(pdf)

            # res = QFileDialog.getSaveFileName(self, 'Save File', '/', 'PDF File (*.pdf)')
            merger.write('result.pdf')
            merger.close()
        except:
            print("Что то не так")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute application
