import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import QtSql






class App():





    def initUI1(self):

        self.w=QDialog()

        self.w.setStyleSheet('QWidget{background-image: url(blue.png)}')

        self.grid = QGridLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setStyleSheet('border: 1px solid #999999;height: 8px;')

        self.b1=QPushButton("ADD DOCTOR")
        self.b1.setStyleSheet('QPushButton {background-image:url(white.png);font:14pt; color:grey;}')

        self.b1.setIcon(QIcon(QPixmap("doctor.jpg")))
        self.b1.setIconSize(QSize(100,100))
        self.b1.setToolTip("This is to login the account of user")

        self.b1.clicked.connect(self.add_doctor)
        self.b2=QPushButton("DELETE Doctor")
        self.b2.setIcon(QIcon(QPixmap("doctor.jpg")))
        self.b2.setIconSize(QSize(100, 100))
        self.b2.setStyleSheet('QPushButton {background-image:url(white.png);font:14pt; color: grey;}')
        self.b2.clicked.connect(self.delete_doctor)
        self.b3=QPushButton("ADD Patient")
        self.b3.setIcon(QIcon(QPixmap("patient.jpg")))
        self.b3.setIconSize(QSize(100, 100))

        self.b3.setStyleSheet('QPushButton {background-image:url(white.png);font:14pt Comic Sans MS; color: grey;}')
        self.b3.clicked.connect(self.add_user)

        self.b4 = QPushButton("DELETE Patient")
        self.b4.setIcon(QIcon(QPixmap("patient.jpg")))
        self.b4.setIconSize(QSize(100, 100))
        self.b4.setStyleSheet('QPushButton {background-image:url(white.png);font:14pt; color: grey;}')
        self.b4.clicked.connect(self.delete_user)

        self.b5 = QPushButton("Total appointments")
        self.b5.setIcon(QIcon(QPixmap("total.jpg")))
        self.b5.setIconSize(QSize(100, 100))
        self.b5.setStyleSheet('QPushButton {background-color: Blue;background-color:red;font:10pt; color: grey;}')

        self.grid.addWidget(self.b1,0,2)
        self.grid.addWidget(self.b2, 4, 2)
        self.grid.addWidget(self.b2, 4, 2)
        self.grid.addWidget(self.b3, 0, 4)
        self.grid.addWidget(self.b4, 4, 4)
        self.grid.addWidget(self.b5, 5, 3)

        self.w.setLayout(self.grid)

        self.w.setGeometry(100, 100, 400, 400)
        self.w.setWindowTitle("PyQt")
        self.w.show()

    def add_doctor(self):
        self.d = QDialog()
        self.layout = QFormLayout()
        self.d.setStyleSheet("background-image: url(green.jpeg)")

        self.header = QLabel("Welcome to our health care program")
        self.header.setStyleSheet("QLabel {font: 30pt Comic Sans MS;font-style:italic;text-decoration:underline;font-weight:bold;color:skyblue}")

        self.lname = QLabel("Enter your name")
        self.lname.setStyleSheet("QLabel{font-weight:bold}")


        self.lcity = QLabel("Enter your city")
        self.lcity.setStyleSheet("QLabel{font-weight:bold}")
        self.larea = QLabel("Enter your area")
        self.larea.setStyleSheet("QLabel{font-weight:bold}")
        self.lmobile = QLabel("Enter your mobile number")
        self.lmobile.setStyleSheet("QLabel{font-weight:bold}")

        self.lsubmit = QPushButton("click here to submit")
        self.lsubmit.clicked.connect(self.createdb)

        self.txtname = QLineEdit()


        self.txtcity = QComboBox()
        self.txtarea = QComboBox()
        self.txtarea.addItem("Enter area")
        self.txtcity.addItem("Enter city")
        self.txtcity.addItem("Jaipur")
        self.txtcity.addItem("Bhubaneswar")
        self.txtcity.currentIndexChanged.connect(self.selectionchange)



        self.txtmobile = QLineEdit()

        self.layout.addRow(self.header)
        self.layout.addRow(self.lname, self.txtname)

        self.layout.addRow(self.lcity, self.txtcity)
        self.layout.addRow(self.larea, self.txtarea)
        self.layout.addRow(self.lmobile, self.txtmobile)
        self.layout.addRow(self.lsubmit)
        self.d.setLayout(self.layout)
        self.d.setGeometry(100, 100, 400, 400)

        self.d.exec_()
    def selectionchange(self,i):
        city=self.txtcity.currentText()
        self.city=city
        if self.city=="Jaipur":
            self.txtarea.clear()
            self.txtarea.addItem("Enter area")
            self.txtarea.addItem("mahaveer nagar")
            self.txtarea.addItem("sitapura")
            self.txtarea.addItem("narayan singh circle")
            self.txtarea.addItem("lal koti")
            self.txtarea.addItem("Gaurav Tower")
            self.txtarea.currentIndexChanged.connect(self.selectionarea)

        if self.city=="Bhubaneswar":
            self.txtarea.clear()
            self.txtarea.addItem("Enter area")
            self.txtarea.addItem("bapuji nagar")
            self.txtarea.addItem("sahaeed nagar")
            self.txtarea.addItem("tilak nagar")
            self.txtarea.addItem("khandagiri")
            self.txtarea.currentIndexChanged.connect(self.selectionarea)





    def selectionarea(self,j):

        self.area=self.txtarea.currentText()





    def delete_doctor(self):
        self.a = QDialog()
        self.layout = QFormLayout()
        self.a.setStyleSheet("background-image: url(sky.jpg)")


        self.delheader = QLabel("Welcome to our health care program")
        self.delheader.setStyleSheet("QLabel {font: 30pt Comic Sans MS;text-decoration:underline;font-weight:bold;color: #621D6B;border:3px dotted red }")


        self.deluserid = QLabel("Enter user id of doctor")
        self.deluserid.setStyleSheet("QLabel{font-weight:bold}")
        self.deltxtuserid = QLineEdit()
        self.btn2=QPushButton("CLICK HERE TO DELETE")
        self.btn2.clicked.connect(self.deletedb)

        self.layout.addRow(self.delheader)
        self.layout.addRow(self.deluserid, self.deltxtuserid)
        self.layout.addRow(self.btn2)
        self.a.setLayout(self.layout)
        self.a.setGeometry(100,100,500,50)


        self.a.exec_()

    def add_user(self):
        self.j = QDialog()
        self.layout = QFormLayout()
        self.j.setStyleSheet("background-image: url(coins.jpeg)")
        self.header1 = QLabel("Thanks for logging in with us")
        self.header1.setStyleSheet("QLabel {font: 40pt Comic Sans MS;text-decoration:underline;font-style:italic;font-weight:bold;color: #621D6B;border:2px dashed blue}")

        self.header2 = QLabel("Kindly Fill The Registration Form")
        self.header2.setStyleSheet("QLabel {font: 20pt Brush Script MT;text-decoration:underline;font-style:italic;;color: Brown;}")

        self.uname = QLabel("Enter your name")
        self.uname.setStyleSheet("QLabel{font-weight:bold}")
        self.uemail = QLabel("Enter your email id")
        self.uemail.setStyleSheet("QLabel{font-weight:bold}")

        self.upassword = QLabel("Enter your password")
        self.upassword.setStyleSheet("QLabel{font-weight:bold}")
        self.ucity = QLabel("Enter your city")
        self.ucity.setStyleSheet("QLabel{font-weight:bold}")
        self.uarea = QLabel("Enter your area")
        self.uarea.setStyleSheet("QLabel{font-weight:bold}")
        self.umobile = QLabel("Enter your mobile number")
        self.umobile.setStyleSheet("QLabel{font-weight:bold}")

        self.usubmit = QPushButton("click here to submit")
        self.usubmit.clicked.connect(self.usercreatedb)

        self.utxtname = QLineEdit()

        self.utxtemail = QLineEdit()

        self.utxtpassword = QLineEdit()
        self.utxtpassword.setEchoMode(QLineEdit.Password)
        self.utxtcity = QComboBox()
        self.utxtarea = QComboBox()
        self.utxtarea.addItem("Enter area")
        self.utxtcity.addItem("Enter city")
        self.utxtcity.addItem("Jaipur")
        self.utxtcity.addItem("Bhubaneswar")
        self.utxtcity.currentIndexChanged.connect(self.userselectionchange)

        self.utxtmobile = QLineEdit()

        self.layout.addRow(self.header1)
        self.layout.addRow(self.header2)

        self.layout.addRow(self.uname, self.utxtname)
        self.layout.addRow(self.uemail, self.utxtemail)

        self.layout.addRow(self.upassword, self.utxtpassword)
        self.layout.addRow(self.ucity, self.utxtcity)
        self.layout.addRow(self.uarea, self.utxtarea)
        self.layout.addRow(self.umobile, self.utxtmobile)
        self.layout.addRow(self.usubmit)

        self.j.setLayout(self.layout)
        self.j.setGeometry(100, 100, 500, 50)




        self.j.exec_()

    def userselectionchange(self, i):
        ucity = self.utxtcity.currentText()
        self.ucity = ucity
        if self.ucity == "Jaipur":
            self.utxtarea.clear()
            self.utxtarea.addItem("Enter area")
            self.utxtarea.addItem("mahaveer nagar")
            self.utxtarea.addItem("sitapura")
            self.utxtarea.addItem("narayan singh circle")
            self.utxtarea.addItem("lal koti")
            self.utxtarea.addItem("Gaurav Tower")
            self.utxtarea.currentIndexChanged.connect(self.userselectionarea)

        if self.ucity == "Bhubaneswar":
            self.utxtarea.clear()
            self.utxtarea.addItem("Enter area")
            self.utxtarea.addItem("bapuji nagar")
            self.utxtarea.addItem("sahaeed nagar")
            self.utxtarea.addItem("tilak nagar")
            self.utxtarea.addItem("khandagiri")
            self.utxtarea.currentIndexChanged.connect(self.userselectionarea)

    def userselectionarea(self, j):


        self.uarea = self.utxtarea.currentText()

    def delete_user(self):

        self.k = QDialog()
        self.layout = QFormLayout()
        self.k.setStyleSheet("background-image: url(sky.jpg)")

        self.udelheader = QLabel("Welcome to our health care program")
        self.udelheader.setStyleSheet("QLabel {font: 30pt Comic Sans MS;text-decoration:underline;font-weight:bold;color: #621D6B;border:3px dotted red }")

        self.udeluserid = QLabel("Enter user id of Patient")
        self.udeluserid.setStyleSheet("QLabel{font-weight:bold}")
        self.udeltxtuserid = QLineEdit()
        self.btn2 = QPushButton("CLICK HERE TO DELETE")
        self.btn2.clicked.connect(self.userdeletedb)

        self.layout.addRow(self.udelheader)
        self.layout.addRow(self.udeluserid, self.udeltxtuserid)
        self.layout.addRow(self.btn2)
        self.k.setLayout(self.layout)
        self.k.setGeometry(100, 100, 500, 50)

        self.k.exec_()







    def usercreatedb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('patient.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("Cannot open database"),
                                 qApp.tr("Unable to establish a database connection.\n"
                                         "This example needs SQLite support. Please read "
                                         "the Qt SQL driver documentation for information "
                                         "how to build it.\n\n" "Click Cancel to exit."),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        sql = "create table patient(ename varchar(50),eemail varchar(50),epassword varchar(50),ecity varchar(50),earea varchar(50),emobile varchar(50))"
        query.exec_(sql)

        query.exec_("insert into patient(ename,eemail,epassword,ecity,earea,emobile)values('%s','%s','%s','%s','%s','%s')" % (self.utxtname.text(), self.utxtemail.text(), self.utxtpassword.text(), self.ucity,self.uarea, self.utxtmobile.text()))

        return True


    def userdeletedb(self):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('patient.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("Cannot open database"),
                                 qApp.tr("Unable to establish a database connection.\n"
                                         "This example needs SQLite support. Please read "
                                         "the Qt SQL driver documentation for information "
                                         "how to build it.\n\n" "Click Cancel to exit."),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        query.exec_("delete from patient where euserid = '%s'" % (self.udeltxtuserid.text()))
        return True

    def deletedb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('doctors.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("Cannot open database"),
                                 qApp.tr("Unable to establish a database connection.\n"
                                         "This example needs SQLite support. Please read "
                                         "the Qt SQL driver documentation for information "
                                         "how to build it.\n\n" "Click Cancel to exit."),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        query.exec_("delete from doctors where euserid = '%s'"%(self.deltxtuserid.text()))
        return True








    def createdb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('doctors.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("Cannot open database"),
                                 qApp.tr("Unable to establish a database connection.\n"
                                         "This example needs SQLite support. Please read "
                                         "the Qt SQL driver documentation for information "
                                         "how to build it.\n\n" "Click Cancel to exit."),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        sql = "create table doctors(dname varchar(50),city varchar(50),area varchar(50),dmobile varchar(50))"
        query.exec_(sql)

        query.exec_("insert into doctors(dname,city,area,dmobile)values('%s','%s','%s','%s')" % (self.txtname.text(),self.city, self.area, self.txtmobile.text()))

        return True















