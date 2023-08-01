from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import addproducts, addusers, roles, display_products, display_roles, display_users, main, pos_sale

class show_Dataset(QWidget):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("administrative dashboard")
        self.isFullScreen()
        self.adjustSize()
        
        
        
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)

        self.username_label = QLabel(self)
        self.username_label.setFont(font)
        self.username_label.move(1000, 10)
        self.username_label.setFixedHeight(40)
        self.username_label.setFixedWidth(150)
        self.username_label.setStyleSheet("background-color: #FFFFFF")

        # shut down
        self.clos = QPushButton(self)
        self.clos.setText("close")
        self.clos.move(1200,600)
        self.clos.setFont(font)
        self.clos.setFixedHeight(40)
        self.clos.setFixedWidth(100)
        self.clos.setStyleSheet("background-color: red; border: 4px solid red; border-radius: 10px")
        self.clos.clicked.connect(self.close) 

        self.logout = QPushButton(self)
        self.logout.setText("logout")
        self.logout.move(1200,10) 
        self.logout.setFont(font)
        self.logout.setFixedHeight(40)
        self.logout.setFixedWidth(150)
        self.logout.clicked.connect(self.open_login)  

        self.pos1 = QPushButton(self)
        self.pos1.setText("pos")
        self.pos1.move(30,10) 
        self.pos1.setFont(font)
        self.pos1.setFixedHeight(40)
        self.pos1.setFixedWidth(100)
        self.pos1.clicked.connect(self.pos)   
        # header
        self.label = QLabel(self)
        self.label.setText("Welcome to administrative dashboard")
        self.label.move(500,20)
        self.label.setFont(font)
        self.label.setFixedHeight(70)
        # Roles
        self.button0 = QPushButton(self)
        self.button0.setFont(font)
        self.button0.setFixedWidth(200)
        self.button0.setFixedHeight(50)
        self.button0.setText("ADD ROLES")
        self.button0.move(10, 100)
        self.button0.setStyleSheet("background-color: rgb(100,149,237)")
        self.button0.clicked.connect(self.launch_addrole_file)


        # USERS
        self.button1 = QPushButton(self)
        self.button1.setFont(font)
        self.button1.setFixedWidth(200)
        self.button1.setFixedHeight(50)
        self.button1.setText("ADD USERS")
        self.button1.move(220, 100)
        self.button1.setStyleSheet("background-color: rgb(100,149,237)")
        self.button1.clicked.connect(self.launch_adduser_file)


        # button2
        self.button2 = QPushButton(self)
        self.button2.setFont(font)
        self.button2.setFixedWidth(200)
        self.button2.setFixedHeight(50)
        self.button2.setText("Add Products")
        self.button2.move(430, 100)
        self.button2.setStyleSheet("background-color: rgb(100,149,237)")
        self.button2.clicked.connect(self.launch_addproducts_file)


        # button3
        self.button3 = QPushButton(self)
        self.button3.setFont(font)
        self.button3.setFixedWidth(200)
        self.button3.setFixedHeight(50)
        self.button3.setText("products")
        self.button3.move(640, 100)
        self.button3.setStyleSheet("background-color: rgb(100,149,237)")
        self.button3.clicked.connect(self.launch_products_file)

        # button4
        self.button4 = QPushButton(self)
        self.button4.setFont(font)
        self.button4.setFixedWidth(200)
        self.button4.setFixedHeight(50)
        self.button4.setText("users")
        self.button4.move(850, 100)
        self.button4.setStyleSheet("background-color: rgb(100,149,237)")
        self.button4.clicked.connect(self.launch_users_file)

        # button5
        self.button5 = QPushButton(self)
        self.button5.setFont(font)
        self.button5.setFixedWidth(200)
        self.button5.setFixedHeight(50)
        self.button5.setText("roles")
        self.button5.move(1060, 100)
        self.button5.setStyleSheet("background-color: rgb(100,149,237)")
        self.button5.clicked.connect(self.launch_role_file)

    def open_login(self):
        self.login = main.window()
        self.login.create_buttons()
        self.login.day_time()
        self.login.showMaximized()
        self.login.show()
        self.close()

    def set_username(self, username):
        self.username_label.setText("Administrator: " + username)

    def pos(self, user):
        self.pos1 = pos_sale.show_Dataset()
        self.pos1.showFullScreen()
        # self.pos1.set_username(self.set_username(user))
        self.pos1.show()
        self.close()

    def launch_addrole_file(self):
        self.roles = roles.show_Dataset()
        self.roles.show()

    def launch_adduser_file(self):
        self.addusers = addusers.show_Dataset()
        self.addusers.show()

    def launch_addproducts_file(self):
        self.addproducts = addproducts.show_Dataset()
        self.addproducts.show()

    def launch_products_file(self):
        self.deleteproducts = display_products.ShowDataset()
        self.deleteproducts.show()

    def launch_users_file(self):
        self.deleteusers = display_users.show_Dataset()
        self.deleteusers.show()

    def launch_role_file(self):
        self.deleterole = display_roles.show_Dataset()
        self.deleterole.show()



    
 
        