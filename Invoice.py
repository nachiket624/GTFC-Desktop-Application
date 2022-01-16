import sys
from PySide2 import QtWidgets
from PrintInvoice import Ui_Dialog1
from PySide2 import QtPrintSupport
from PySide2.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
class MYInvoics(QtWidgets.QDialog,Ui_Dialog1):
    def __init__(self):
        super(MYInvoics, self).__init__()
        self.setupUi(self)
        # self.dashboard_btn.clicked.connect(self.windashboard)
        self.Invoice_print_btn.clicked.connect(self.print_file)
        self.Perview_btn.clicked.connect(self.print_preview_dialog)
    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        diglog = QPrintDialog(printer,self)

        if diglog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.printperview)
        previewDialog.exec_()


    def printperview(self,printer):
        self.textEdit.print_(printer)
app = QtWidgets.QApplication(sys.argv)
window = MYInvoics()
window.show()
app.exec_()