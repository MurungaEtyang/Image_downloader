from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import databaseApi.pos_generatebill.generate_bill as bill_generate
import time, time_day, main, dashboard
class show_Dataset(QWidget):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("POINT OF SALE")
        self.adjustSize()
        
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
        # username
        self.username_label = QLabel(self)
        self.username_label.setFont(font)
        self.username_label.move(1000, 10)
        self.username_label.setFixedHeight(40)
        self.username_label.setFixedWidth(220)
        self.username_label.setStyleSheet("background-color: #FFFFFF")
        # header
        self.label = QLabel(self)
        self.label.setText("POINT OF SALE")
        self.label.move(800,10)
        self.label.setFont(font)
        # time
        self.label = QLabel(self)
        self.label.setText(time.ctime())
        self.label.move(250,10)
        self.label.setFont(font)

        self.logout = QPushButton(self)
        self.logout.setText("logout")
        self.logout.move(1200,10) 
        self.logout.setFont(font)
        self.logout.setFixedHeight(40)
        self.logout.setFixedWidth(150)
        self.logout.clicked.connect(self.open_login) 

        # shut down
        self.clos = QPushButton(self)
        self.clos.setText("close")
        self.clos.move(1200,700) 
        self.clos.setFont(font)
        self.clos.setFixedHeight(40)
        self.clos.setFixedWidth(100)
        self.clos.setStyleSheet("background-color: red; border: 4px solid red; border-radius: 10px")
        self.clos.clicked.connect(self.close) 
        # dashboard
        self.dash = QPushButton(self)
        self.dash.setText("DASHBOARD")
        self.dash.move(1000,700) 
        self.dash.setFont(font)
        self.dash.setFixedHeight(40)
        self.dash.setFixedWidth(150)
        self.dash.setStyleSheet("background-color: green; border: 4px solid green;")
        self.dash.clicked.connect(self.open_dashboard)     
  
        self.label = QLabel(self)
        self.label.setText(time_day.a)
        self.label.move(10,10)
        self.label.setFont(font)

        # SEARCH
        self.search1 = QLineEdit(self)
        self.search1.setPlaceholderText("name of the product or product code")
        self.search1.setFont(font)
        self.search1.move(30,60)
        self.search1.setFixedHeight(50)
        self.search1.setFixedWidth(450)

        self.search1.textChanged.connect(self.search_product)

        # vbox = QVBoxLayout()
        self.spinbox = QSpinBox(self)
        self.spinbox.textChanged.connect(self.search_product)
        self.spinbox.move(450, 150)
        self.spinbox.setFixedHeight(50)
        self.spinbox.setFixedWidth(50)
        self.spinbox.setFont(font)
        # paid amount label
        self.search_paid = QLabel(self)
        self.search_paid.setText("paid amount")
        self.search_paid.setFont(font)
        self.search_paid.move(30,320)
        self.search_paid.setFixedHeight(50)
        self.search_paid.setFixedWidth(150)
        self.search_paid.setStyleSheet("background-color: white;")
        # paid amoubt input
        self.paid = QLineEdit(self)
        self.paid.setPlaceholderText("paid amount")
        self.paid.setFont(font)
        self.paid.move(30,400)
        self.paid.setFixedHeight(50)
        self.paid.setFixedWidth(150)
        self.paid.setStyleSheet("background-color: rgb(65,74,76)); color:green; border-color:pink; border-radius: 5px;")

        # change label
        self.search_change = QLabel(self)
        self.search_change.setText("change")
        self.search_change.setFont(font)
        self.search_change.move(200,320)
        self.search_change.setFixedHeight(50)
        self.search_change.setFixedWidth(150)
        self.search_change.setStyleSheet("background-color: white;")
        # change
        self.search_change1 = QLabel(self)
        self.search_change1.setFont(font)
        self.search_change1.move(200,400)
        self.search_change1.setFixedHeight(50)
        self.search_change1.setFixedWidth(150)
        # total label
        self.search_total = QLabel(self)
        self.search_total.setText("total amount")
        self.search_total.setFont(font)
        self.search_total.move(370,320)
        self.search_total.setFixedHeight(50)
        self.search_total.setFixedWidth(150)
        self.search_total.setStyleSheet("background-color: white;")

        self.search_total2 = QLabel(self) 
        self.search_total2.setFont(font)
        self.search_total2.move(370,400)
        self.search_total2.setFixedHeight(50)
        self.search_total2.setFixedWidth(150)
        self.search_total2.setStyleSheet("background-color: white; color: green;")

        self.search_label = QLabel(self)
        self.search_label.setFont(font)
        self.search_label.move(30,150)
        self.search_label.setFixedHeight(50)
        self.search_label.setFixedWidth(400)
        self.search_label.setStyleSheet("background-color: white;")

        self.generate_bill = QPushButton(self)
        self.generate_bill.setFont(font)
        self.generate_bill.move(30,550)
        self.generate_bill.setText("generate bill")
        self.generate_bill.setFixedHeight(50)
        self.generate_bill.setFixedWidth(500)
        self.generate_bill.setStyleSheet("background-color: green")
        self.generate_bill.clicked.connect(self.search_product)

    def set_username(self, username):
        self.username_label.setText("User: " + str(username))

    def open_login(self):
        self.login = main.window()
        self.login.create_buttons()
        self.login.day_time()
        self.login.showMaximized()
        self.login.show()
        self.close()

    def open_dashboard(self):
        self.dash = dashboard.show_Dataset()
        self.dash.showMaximized()
        self.dash.show()
        self.close()

    def search_product(self):
        search_text = self.search1
        total_product_price =self.spinbox
        paid_amount = self.paid
        bill_generate.Bill_generate.search_products(self, search_text, total_product_price, paid_amount)     