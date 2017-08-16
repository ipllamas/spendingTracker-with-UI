import sys
import tracker
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtWidgets import QAction, QMessageBox, QLabel, QComboBox, QTextEdit

class window(QMainWindow):
    def __init__(self):
        #Sets up the window, complete with save, load, and exit actions
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Spending Tracker')
        self.setWindowIcon(QIcon('python_icon.jpg'))

        loadAction = QAction("&Load", self)
        loadAction.setShortcut("Ctrl+L")
        loadAction.setStatusTip("Load your data")
        loadAction.triggered.connect(self.loadData)

        saveAction = QAction("&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save your data")
        saveAction.triggered.connect(self.saveData)

        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Leave The App")
        exitAction.triggered.connect(self.close_application)

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(exitAction)

        #This creates an object of the Profile class, which holds most
        #major functions that is executed by the buttons in this UI.
        self.profile = tracker.Profile()
        self.profile.resetValues()

        self.home()

    def home(self):
        self.inputCategory = QTextEdit(self)
        self.inputCategory.move(150, 50)

        #Adds various interactable buttons to the window
        btn_add = QPushButton("Add Category", self)
        btn_add.clicked.connect(self.addCategory)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(250, 50)

        btn_del = QPushButton("Delete Category", self)
        btn_del.clicked.connect(self.delCategory)
        btn_del.resize(btn_del.sizeHint())
        btn_del.move(325, 50)
        
        self.dropDown = QComboBox(self)
        self.dropDown.addItem("Balance")
        self.dropDown.addItem("Food")
        self.dropDown.addItem("Gas")
        self.dropDown.addItem("Shopping")
        self.dropDown.move(150, 100)

        self.inputVal = QTextEdit(self)
        self.inputVal.move(40, 100)
        
        btn_exec = QPushButton("Add/Subtract", self)
        btn_exec.clicked.connect(self.execute_program)
        btn_exec.resize(btn_exec.sizeHint())
        btn_exec.move(250, 100)

        btn_exit = QPushButton("Quit", self)
        btn_exit.clicked.connect(self.close_application)
        btn_exit.resize(btn_exit.sizeHint())
        btn_exit.move(150, 200)

        self.dataOutput = QLabel(self.profile.displayData(), self)
        self.dataOutput.resize(self.dataOutput.sizeHint())
        self.dataOutput.move(250, 200)

        self.show()

    #Modifies the values of various categories in the program
    def execute_program(self):
        if(self.isNum(self.inputVal.toPlainText())==True):
            inp = float(self.inputVal.toPlainText())
            category = self.dropDown.currentText()
            self.profile.updateItem(category, inp)
            self.dataOutput.setText(self.profile.displayData())
            self.dataOutput.resize(self.dataOutput.sizeHint())
        else:
            pass

    def addCategory(self):
        newCategory = self.inputCategory.toPlainText()
        self.dropDown.addItem(newCategory)
        self.profile.newItem(newCategory, 0)
        self.dataOutput.setText(self.profile.displayData())
        self.dataOutput.resize(self.dataOutput.sizeHint())

    def delCategory(self):
        delCategory = self.inputCategory.toPlainText()
        self.profile.delItem(delCategory)
        self.dataOutput.setText(self.profile.displayData())
        self.dataOutput.resize(self.dataOutput.sizeHint())        


    def close_application(self):
        self.choice = QMessageBox.question(self, "Confirmation", "Exit Program?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if self.choice == QMessageBox.Yes:
            self.profile.displayData()
            sys.exit()
        else:
            pass

    #Creates text file to save data
    def saveData(self):
        self.profile.saveFile()
        self.profile.displayData()
        self.dataOutput.setText(self.profile.displayData())
        self.dataOutput.resize(self.dataOutput.sizeHint())  

    #Pulls data from text file to use
    def loadData(self):
        self.profile.loadFile()
        self.profile.displayData()
        self.dataOutput.setText(self.profile.displayData())
        self.dataOutput.resize(self.dataOutput.sizeHint())  

    def isNum(self, toCheck):
        try:
            val = float(str(toCheck))
            return True
        except ValueError:
            print("Invalid entry")
            return False

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
