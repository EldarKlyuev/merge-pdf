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
        self.downButton.clicked.connect(self.evt_down_btn_click)
        self.upButton.clicked.connect(self.evt_up_btn_click)
        self.clearButton.clicked.connect(self.evt_clear_btn_click)

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
        arr = []
        lst = self.listWidget
        for x in range(lst.count()):
            arr.append(lst.item(x).text())

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

    def evt_up_btn_click(self):
        currentRow = self.listWidget.currentRow()
        currentItem = self.listWidget.takeItem(currentRow)
        self.listWidget.insertItem(currentRow - 1, currentItem)

    def evt_down_btn_click(self):
        currentRow = self.listWidget.currentRow()
        currentItem = self.listWidget.takeItem(currentRow)
        self.listWidget.insertItem(currentRow + 1, currentItem)

    def evt_clear_btn_click(self):
        arr = []
        self.listWidget.clear()


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
