import sys
from PyPDF2 import PdfFileMerger
from PyQt5.QtWidgets import *

arr = list()
merger = PdfFileMerger(strict=False)


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MergePDF')
        self.resize(200, 200)

        self.btn = QPushButton('Open File', self)
        self.btn.move(60, 50)
        self.btn.clicked.connect(self.evt_opn_btn_click)

        self.btn = QPushButton('Save File', self)
        self.btn.move(60, 80)
        self.btn.clicked.connect(self.evt_sv_btn_click)

    def evt_opn_btn_click(self):
        global arr
        res = QFileDialog.getOpenFileNames(self, 'Open File', '/', 'PDF File (*.pdf)')
        arr = res[0]

    def evt_sv_btn_click(self):
        global merger
        try:
            for pdf in arr:
                merger.append(pdf)

            res = QFileDialog.getSaveFileName(self, 'Save File', '/', 'PDF File (*.pdf)')
            merger.write(res[0])
            merger.close()

            QMessageBox.information(self, 'Save File', f'File saved in {res[0]}')

        except Exception as exc:
            QMessageBox.critical(self, 'Something wrong', 'Error')
            print(exc)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute application
