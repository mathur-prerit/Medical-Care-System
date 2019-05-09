import sys
from PyQt5 import QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import adminpage
import User


class login(adminpage.App,User.UserPage):
    'Login Page'

    def __init__(self):


        self.initUI()

    def initUI(self):
        #window banai h isse
        self.p=QWidget()
        self.p.setWindowTitle("Medical Care System- Login Page")
        self.p.setStyleSheet("background-image: url(sky.jpg)")
        self.p.setGeometry(100,100,600,600)

        # Login ka button
        self.qbtn1=QPushButton("Login",self.p)
        self.qbtn1.setToolTip("This is to login the account of user")
        self.qbtn1.clicked.connect(self.admin_user_login)
        self.qbtn1.move(100, 250)


        # Signup ka button
        self.qbtn2 = QPushButton("Signup", self.p)
        self.qbtn2.setToolTip("Add your Database to use services")
        self.qbtn2.clicked.connect(self.add_user)
        self.qbtn2.move(200, 250)

        # Emergency ka button
        self.qbtn3 = QPushButton("EMERGENCY", self.p)
        self.qbtn3.setToolTip("Click for Emergency Services")
        self.qbtn3.clicked.connect(self.emerg)
        self.qbtn3.move(500, 250)

        # About Us ka button
        self.qbtn4 = QPushButton("About Us", self.p)
        self.qbtn4.setToolTip("Our Developer Team")
        self.qbtn4.clicked.connect(self.about)
        self.qbtn4.move(200, 550)

        #Heading h program ki
        self.label=QLabel("Medical Care System",self.p)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial',18))
        self.label.move(50,20)

        #Username ka label
        self.usernamel= QLabel("Username:", self.p)
        self.usernamel.move(100, 100)

        #Password ka label
        self.passwordl = QLabel("Password:", self.p)
        self.passwordl.move(100, 150)

        #username ka input
        self.usernamei=QLineEdit(self.p)
        self.usernamei.move(200,100)
        self.usernamei.resize(130,20)

        # password ka input
        self.passwordi = QLineEdit(self.p)
        self.passwordi.setEchoMode(QLineEdit.Password)
        self.passwordi.move(200, 150)
        self.passwordi.resize(130, 20)
        self.p.show()

    #smiple printing
    def on_click(self):
        print("This is working")

    def admin_user_login(self):
        if self.usernamei.text()=='admin':
            if self.passwordi.text()=='12345678':
                self.initUI1()
            else:
                QMessageBox.warning(self.p,"Warning","Enter Correct Password", QMessageBox.Ok,QMessageBox.Ok)

        else:

            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('patient.db')

            if not db.open():
                QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)

                return False

            query = QtSql.QSqlQuery()

            sql = "select epassword from patient where eemail='%s' " % (self.usernamei.text())
            query.exec_(sql)
            row = []
            while query.next():
                row += [[query.value(index) for index in range(1)]]

            if row[0][0] == self.passwordi.text():
                self.initUI3()
            else:
                QMessageBox.warning(self.p, "Caution","Enter Correct Password", QMessageBox.Ok,
                                QMessageBox.Ok)

    #Emergency ka messageboxreply
    def emerg(self):

        QMessageBox.warning(self.p,"Emergency Services","EMERGENCY CONTACT NUMBER\nDial 108",QMessageBox.Ok,QMessageBox.Ok)

    #About us ka button bhaisahab
    def about(self):

        QMessageBox.warning(self.p,"About Us","Developer Name:\n Prerit Mathur\nVarun Singhal\nSachin Kumar",QMessageBox.Ok,QMessageBox.Ok)

if __name__=='__main__':
    app=QApplication (sys.argv)
    ex=login()
    sys.exit(app.exec_())
