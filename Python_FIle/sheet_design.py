import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QFileDialog,QStackedWidget
from PySide2.QtCore import QFile, QIODevice,QCoreApplication

class Setup_urls:
    def __init__(self):
        self.ui_file_name = "../UI/sheet_design.ui"
        self.ui_file = QFile(self.ui_file_name)

        if not self.ui_file.open(QIODevice.ReadOnly):                                                         # Error Occure if file not open
            print("Cannot open {}: {}".format(self.ui_file_name, ui_file.errorString()))
            sys.exit(-1)

        self.window=QUiLoader().load(self.ui_file)
        self.ui_file.close()

# customisation if any changes in Design level like lable text then use self.window

    def Button_clicks(self):                                                                         # all Button click define here And call Further function
        self.window.Browse_JSON.clicked.connect(self.browseJson)
        self.window.Browse_Student_List.clicked.connect(self.browseStudent_list)
        self.window.OK_btn.clicked.connect(self.save_data)
        self.window.Cancel_btn.clicked.connect(QCoreApplication.instance().quit)  # cancel button define 

    def browseJson(self):
        __fname__=QFileDialog.getOpenFileName(QFileDialog(),"Google Json File","../","JSONFile(*.json)")
        self.window.Json_file_path.setText(__fname__[0])
    def browseStudent_list(self):
        __fname__=QFileDialog.getOpenFileName(QFileDialog(),"Student List","../","EXCEL(*.xlsx *.xlsm *.xls *.xlt *.xml *.xlam *.xla *.xlw *.xlr)")
        self.window.Student_List_Url.setText(__fname__[0])
    def save_data(self):
        # check git repo and Google Sheet(use Json)
        # create two file/class for Google Sheet and git and call it from here
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Object1 = Setup_urls()
    #Object1.Button_clicks()   # all Click event define here
    Object1.window.show()
    sys.exit(app.exec_())

