import sys
from PyPDF2 import PdfFileMerger

from PyQt5 import uic, QtWidgets
import design

arr = list()
merger = PdfFileMerger(strict=False)


class DlgMain(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.evt_opn_btn_click)
        self.pushButton_2.clicked.connect(self.evt_sv_btn_click)

    def evt_opn_btn_click(self):
        try:
            global arr
            res = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File', '/', 'PDF File (*.pdf)')
            arr = res[0]

            for file_name in res:
                self.listWidget.addItems(file_name)
            print(res[0])
        except Exception as exc:
            print(exc)

    def evt_sv_btn_click(self):
        global merger
        try:
            for pdf in arr:
                merger.append(pdf)

            res = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '/', 'PDF File (*.pdf)')
            merger.write(res[0])
            merger.close()

            QtWidgets.QMessageBox.information(self, 'Save File', f'File saved in {res[0]}')

        except Exception as exc:
            QtWidgets.QMessageBox.critical(self, 'Something wrong', 'Error')
            print(exc)


def main():
    # Recompile ui
    with open("design.ui") as ui_file:
        with open("design.py", "w") as py_ui_file:
            uic.compileUi(ui_file, py_ui_file)
    app = QtWidgets.QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute application


if __name__ == '__main__':
    main()
