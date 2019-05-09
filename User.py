import sys
from PyQt5 import QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import smtplib
from smtplib import *

class UserPage():
    'Login Page'



    def initUI3(self):
        self.v = QDialog()
        self.v.setStyleSheet('QWidget{background-image: url(marble.jpeg)}')
        self.grid = QGridLayout()

        # Book appointment ka button
        self.bookappointment = QPushButton("Book Appointment")
        self.bookappointment.setStyleSheet('QPushButton {background-color: Blue; color:Blue;}')
        self.bookappointment.setIcon(QIcon(QPixmap("doctor.jpg")))
        self.bookappointment.clicked.connect(self.book_appointment)

        # General Prescription ka button


        # MEdical Store near me ka button
        self.medical= QPushButton("Medical Store Near Me")
        self.medical.setIcon(QIcon(QPixmap("patient.jpg")))
        self.medical.setStyleSheet('QPushButton {background-color: Blue; color: Blue;}')
        self.medical.clicked.connect(self.chemist_store)

        # Track Appointment ka button
        self.tappoint = QPushButton("Track Appointment")
        self.tappoint.setIcon(QIcon(QPixmap("total.jpg")))
        self.tappoint.setStyleSheet('QPushButton {background-color: Blue; color:White;}')

        self.grid.addWidget(self.bookappointment, 1, 1)
        #self.grid.addWidget(self.general_prescription, 1, 2)
        self.grid.addWidget(self.medical, 4, 0)
        self.grid.addWidget(self.tappoint, 4, 2)

        self.v.setLayout(self.grid)

        self.v.setGeometry(100, 100, 400, 400)
        self.v.exec_()

    #Main function apppointment ka
    def book_appointment(self):
        self.z = QDialog()
        self.layout = QFormLayout()
        self.z.setStyleSheet("background-image: url(dots.jpg)")

        self.bookheader = QLabel("Welcome to Book Appointment")
        self.bookheader.setStyleSheet("QLabel {font: 30pt Comic Sans MS;font-style:italic;text-decoration:underline;font-weight:bold;color: #621D6B;border:2px dashed blue}")

        self.bookname = QLabel("Enter your name")
        self.bookname.setStyleSheet("QLabel{font-weight:bold}")

        self.bookemail = QLabel("Enter your email id")
        self.bookemail.setStyleSheet("QLabel{font-weight:bold}")
        self.bookcity = QLabel("Enter your city")
        self.bookcity.setStyleSheet("QLabel{font-weight:bold}")
        self.bookarea = QLabel("Enter your area")
        self.bookarea.setStyleSheet("QLabel{font-weight:bold}")
        self.bookmobile = QLabel("Enter your mobile number")
        self.bookmobile.setStyleSheet("QLabel{font-weight:bold}")




        self.booksubmit = QPushButton("click here to submit")
        self.booksubmit.clicked.connect(self.select_doctor)

        self.booktxtname = QLineEdit()

        self.booktxtemail = QLineEdit()
        self.booktxtcity = QComboBox()
        self.booktxtarea = QComboBox()

        self.booktxtarea.addItem("Enter area")
        self.booktxtcity.addItem("Enter city")
        self.booktxtcity.addItem("Jaipur")
        self.booktxtcity.addItem("Bhubaneswar")
        self.booktxtcity.currentIndexChanged.connect(self.selectionchange1)

        self.booktxtmobile = QLineEdit()

        self.layout.addRow(self.bookheader)
        self.layout.addRow(self.bookname, self.booktxtname)
        self.layout.addRow(self.bookemail, self.booktxtemail)
        self.layout.addRow(self.bookcity, self.booktxtcity)
        self.layout.addRow(self.bookarea, self.booktxtarea)
        self.layout.addRow(self.bookmobile, self.booktxtmobile)


        self.layout.addRow(self.booksubmit)

        self.z.setLayout(self.layout)
        self.z.setGeometry(100, 100, 400, 400)
        self.z.exec_()

    #chemist show krne ke liye
    def chemist_store(self):
        self.l = QDialog()
        self.layout = QFormLayout()
        self.l.setStyleSheet("background-image: url(dots.jpg)")

        self.cheader = QLabel("Near By Chemist Shops and Store")
        self.cheader.setStyleSheet("QLabel {font: 30pt Comic Sans MS;font-style:italic;text-decoration:underline;font-weight:bold;color: #621D6B;border:2px dashed blue}")

        self.ccity = QLabel("Enter your city")
        self.ccity.setStyleSheet("QLabel{font-weight:bold}")
        self.carea = QLabel("Enter your area")
        self.carea.setStyleSheet("QLabel{font-weight:bold}")

        self.csubmit = QPushButton("click here to submit")
        self.csubmit.clicked.connect(self.selectionshop)
        self.ctxtcity = QComboBox()
        self.ctxtarea = QComboBox()

        self.ctxtarea.addItem("Enter area")
        self.ctxtcity.addItem("Enter city")
        self.ctxtcity.addItem("Jaipur")
        self.ctxtcity.addItem("Bhubaneswar")
        self.ctxtcity.currentIndexChanged.connect(self.selectionchange2)


        self.layout.addRow(self.cheader)
        self.layout.addRow(self.ccity, self.ctxtcity)
        self.layout.addRow(self.carea, self.ctxtarea)
        self.layout.addRow(self.csubmit)

        self.l.setLayout(self.layout)
        self.l.setGeometry(100, 100, 400, 400)
        self.l.exec_()

    def selectionchange2(self):
        city = self.ctxtcity.currentText()
        self.ccity = city
        if self.ccity == "Jaipur":
            self.ctxtarea.clear()
            self.ctxtarea.addItem("Select Area")
            self.ctxtarea.addItem("Mahaveer Nagar")
            self.ctxtarea.addItem("Sitapura")
            self.ctxtarea.addItem("Mansarovar")
            self.ctxtarea.addItem("Lal Kothi")
            self.ctxtarea.addItem("Jagatpura")
            self.ctxtarea.currentIndexChanged.connect(self.selectionareauser2)

        if self.ccity == "Bhubaneswar":
            self.ctxtarea.clear()
            self.ctxtarea.addItem("Enter Area")
            self.ctxtarea.addItem("Khandagiri")
            self.ctxtarea.addItem("Sahaeed Nagar")
            self.ctxtarea.addItem("Tilak Nagar")
            self.ctxtarea.currentIndexChanged.connect(self.selectionareauser2)

    def selectionareauser2(self):
        self.finalarea = self.ctxtarea.currentText()
        print(self.finalarea)



    def selectionchange1(self,i):
        city=self.booktxtcity.currentText()
        self.bookcity=city
        if self.bookcity=="Jaipur":
            self.booktxtarea.clear()
            self.booktxtarea.addItem("Select Area")
            self.booktxtarea.addItem("Mahaveer Nagar")
            self.booktxtarea.addItem("Sitapura")
            self.booktxtarea.addItem("Mansarovar")
            self.booktxtarea.addItem("Lal Kothi")
            self.booktxtarea.addItem("Jagatpura")
            self.booktxtarea.currentIndexChanged.connect(self.selectionareauser)

        if self.bookcity=="Bhubaneswar":
            self.booktxtarea.clear()
            self.booktxtarea.addItem("Enter Area")
            self.booktxtarea.addItem("Khandagiri")
            self.booktxtarea.addItem("Sahaeed Nagar")
            self.booktxtarea.addItem("Tilak Nagar")
            self.booktxtarea.currentIndexChanged.connect(self.selectionareauser)

    #general Prescription
    def general_prescription(self):
        self.n = QDialog()
        self.layout = QFormLayout()
        self.n.setStyleSheet("background-image: url(dots.jpg)")

        self.gheader = QLabel("FInd Your General Prescription")
        self.gheader.setStyleSheet("QLabel {font: 30pt Comic Sans MS;font-style:italic;text-decoration:underline;font-weight:bold;color: #621D6B;border:2px dashed blue}")

        self.iname = QLabel("Select your illines:")
        self.iname.setStyleSheet("QLabel{font-weight:bold}")



        self.imed = QComboBox()

        self.imed.addItem("Select Illiness")
        self.imed.addItem("Fever")
        self.imed.addItem("Cough")
        self.imed.addItem("Pain")
        #self.imed.currentIndexChanged.connect(self.selectionmed)

        self.layout.addRow(self.gheader)
        self.layout.addRow(self.iname, self.imed)


        self.n.setLayout(self.layout)
        self.n.setGeometry(100, 100, 400, 400)
        self.n.exec_()

    def selectionareauser(self,j):

        self.areafinal=self.booktxtarea.currentText()
        print(self.areafinal)
        print(type(self.areafinal))

    def selectionshop(self,event):

        if self.finalarea=="Mahaveer Nagar":
            QMessageBox.warning(self.l, "Chemist Details", "Apollo pharmcy 08003899474\n Dev medical 9024544650", QMessageBox.Ok,QMessageBox.Ok)
        elif self.finalarea=="Sitapura":
            QMessageBox.warning(self.l, "Chemist Details", "Om Medical 095494 22221 \n Jain Medicare 094130 42954",QMessageBox.Ok, QMessageBox.Ok)
        elif self.finalarea=="Jagatpura":
            QMessageBox.warning(self.l, "Chemist Details", "Maxwell Pharmacy 099289 70239 \n Chaudhary medical 095297 44822",QMessageBox.Ok, QMessageBox.Ok)
        elif self.finalarea=="Mansarovar":
            QMessageBox.warning(self.l, "Chemist Details", "Apollo pharmacy 080038 99477 \n B Lal Pharmacy 073577 26777",QMessageBox.Ok, QMessageBox.Ok)
        elif self.finalarea=="Lal Kothi":
            QMessageBox.warning(self.l, "Chemist Details", "Mukesh Medical 098297 88966 \n Rajasthan Medical 0141 321 7657",QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self.l,"Chemist Details","Sorry No Medical Store in this area",QMessageBox.Ok,QMessageBox.Ok)


    #Doctor Show ur date show krake appointment book krne ke liye
    def select_doctor(self):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('doctors.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("connect open database"), qApp.tr("Unable to establish a DB"),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()

        sql = "select dname from doctors where area='%s'"%(self.areafinal)
        query.exec_(sql)
        row = []
        while query.next():
            row += [query.value(index) for index in range(1)]

        self.doclist=row
        print(self.doclist)

        self.y = QDialog()
        self.layout = QFormLayout()
        # self.y.setStyleSheet("background-image: url(dots.jpg)")

        # email se doctor show karne ke liye
        self.bdoc = QLabel("Select Doctor in your area:")
        self.bdoc.setStyleSheet("QLabel{font-weight:bold}")
        self.bdate = QPushButton("book a date")
        self.bdate.clicked.connect(self.book_date)
        self.finalsubmit = QPushButton("Final Submit")
        self.finalsubmit.clicked.connect(self.createdbfinal)
        self.doctorlistc = QComboBox()
        self.doctorlistc.addItem("Select doctor")
        for i in self.doclist:
            self.doctorlistc.addItem(i)
        self.doctorlistc.currentIndexChanged.connect(self.variab)
        self.layout.addRow(self.bdoc, self.doctorlistc)
        self.layout.addRow(self.bdate)
        self.layout.addRow(self.finalsubmit)
        self.y.setLayout(self.layout)
        self.y.setGeometry(100, 100, 400, 400)

        self.y.exec_()

    def variab(self):
        self.doct=self.doctorlistc.currentText()
    def book_date(self):
        self.c=QDialog()
        cal = QCalendarWidget(self.c)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.c.setGeometry(100, 100, 300, 300)
        self.c.setWindowTitle('Calendar')
        self.c.exec_()

    def showDate(self, date):
        self.datestr=date.toString()




    def createdbfinal(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('appointment.db')

        if not db.open():
            QMessageBox.critical(None, qApp.tr("Cannot open database"),
                                 qApp.tr("Unable to establish a database connection.\n"
                                         "This example needs SQLite support. Please read "
                                         "the Qt SQL driver documentation for information "
                                         "how to build it.\n\n" "Click Cancel to exit."),
                                 QMessageBox.Cancel)

            return False

        print(self.booktxtname.text())
        print(self.booktxtemail.text())
        print(self.bookcity)
        print(self.areafinal)
        print(self.booktxtmobile.text())
        print(self.datestr)
        print(self.doct)

        query = QtSql.QSqlQuery()
        sql = "create table appointment(pname varchar(50),pmail varchar(50),pcity varchar(50),parea varchar(50),pmobile varchar(50),pdate varchar(50),pdoc varchar(50))"
        query.exec_(sql)

        query.exec_("insert into appointment(pname,pmail,pcity,parea,pmobile,pdate,pdoc)values('%s','%s','%s','%s','%s','%s','%s')" % (self.booktxtname.text(), self.booktxtemail.text(),self.bookcity, self.areafinal, self.booktxtmobile.text(),self.datestr,self.doct))

        x=self.booktxtemail.text()
        to =x
        gmail_user ='abc@gmail.com' # hospital ka email address
        gmail_pwd ='passwordxyz'  # apna password

        header123 = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject: Response for your Doctor Appointment\n'

        print(header123)

        msg = header123 + '\nThis is an automatic response regarding the booking of an Appointment with Doctor: ' + self.doct + 'For the date\t' + self.datestr + ' is confirmed.\n Please visit the doctor on time. Thanks.\n Medical Care System'

        try:
            smtpObj = smtplib.SMTP("smtp.gmail.com", 587)

            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(gmail_user, gmail_pwd)
            smtpObj.sendmail(gmail_user, to, msg)
            print("Sent Sucessfully sent mail")
        except SMTPException as e:
            print("Enable to send email", e)
        smtpObj.close()
