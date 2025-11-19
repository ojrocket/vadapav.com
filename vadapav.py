#pip install package_name --no-build-isolation

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QHBoxLayout, QLineEdit, QInputDialog, QMessageBox, QRadioButton, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import sys, random



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JASHWANTH.COM")
        self.setGeometry(400, 100, 900, 700)
        self.radio_withdraw = QRadioButton("WITHDRAW", self)
        self.radio_deposite = QRadioButton("DEPOSITE", self)
        self.radio_check = QRadioButton("CHECK BALANCE", self)
        self.radio_loan = QRadioButton("LOAN ROOM", self)
        self.radio_transfer = QRadioButton("MONEY TRANSFER", self)
        self.radio_stock = QRadioButton("STOCK MARKET", self)
        self.end1_button = QPushButton("EXIT", self)
        self.radio_years = QRadioButton("YEARS", self)
        self.radio_months = QRadioButton("MONTHS", self)
        self.line_edit = QLineEdit(self)
        self.pin_num = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.welcome_label = QLabel("",self)
        self.typewriter_label = QLabel("", self)
        self.users = {
            "kranthi rajesh": {"balance": 8900000, "pin": 19208, "account_num": 135792466},
            "jashwanth": {"balance": 756958, "pin": 78923, "account_num": 983421763},
            "hema": {"balance": 1000000, "pin": 11801, "account_num": 123456789},
            "tempusr": {"balance": 50000, "pin": 12345, "account_num": 111222333}
        }
        self.current_user = None
        self.is_thank_you = False
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(330, 200, 250, 50)
        self.pin_num.setGeometry(330, 260, 250, 50)
        self.button.setGeometry(345, 320, 200, 40)
        
        self.line_edit.setStyleSheet(
            "font-size: 20px;"
            "font-family: Arial;"
            "padding: 8px;"
        )
        self.pin_num.setStyleSheet(
            "font-size: 20px;"
            "font-family: Arial;"
            "padding: 8px;"
        )
        self.button.setObjectName("button")
        self.button.setStyleSheet("""
            QPushButton#button {
            font-size: 30px;
            font-family: Arial;
            padding: 10px 40px;
            margin: 25px;
            border: 2px solid black;
            border-radius: 15px;
            background-color: #cc918d;
            color: black;
            }
            QPushButton#button:hover {
            background-color: #c7736d;
            color: #fff;
            }
        """)
        self.button.adjustSize()
        self.button.clicked.connect(self.authenticate)
        self.end1_button.hide()
        self.radio_years.hide()
        self.radio_months.hide()
        self.radio_withdraw.hide()
        self.radio_deposite.hide()
        self.radio_check.hide()
        self.radio_loan.hide()
        self.radio_transfer.hide()
        self.radio_stock.hide()
        
    def nxt_lobby(self):

        self.line_edit.hide()
        self.pin_num.hide()
        self.button.hide()
        self.radio_years.hide()
        self.radio_months.hide()

        
        self.wel_text = f"🙏WELCOME {self.current_user.upper()} TO VADAPAV.COM BANKING SERVICES🙏"
        self.welcome_index = 0
        self.welcome_label.setGeometry(80, 100, 900, 50)
        self.welcome_label.setStyleSheet("font-size: 24px; font-family: Arial; color: blue;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.welcome_typewriter)
        self.timer.start(100)
        self.radio_deposite.setGeometry(330, 260, 250, 50)
        self.radio_deposite.show()
        self.radio_withdraw.setGeometry(330, 320, 250, 50)
        self.radio_withdraw.show()
        self.radio_check.setGeometry(330, 380, 250, 50)
        self.radio_check.show()
        self.radio_loan.setGeometry(330, 440, 250, 50)
        self.radio_loan.show()
        self.radio_transfer.setGeometry(330, 500, 250, 50)
        self.radio_transfer.show()
        self.radio_stock.setGeometry(330, 560, 250, 50)
        self.radio_stock.show()
        self.end1_button.setGeometry(700, 600, 150, 50)
        self.end1_button.show()


        self.radio_deposite.clicked.connect(self.deposit_room)
        self.radio_withdraw.clicked.connect(self.withdraw_room)
        self.radio_check.clicked.connect(self.check_balance)
        self.radio_loan.clicked.connect(self.loan_room)
        self.radio_transfer.clicked.connect(self.money_transfer)
        self.radio_stock.clicked.connect(self.stock_market)
        self.end1_button.clicked.connect(self.thank_you)
        
    def welcome_typewriter(self):
        if self.welcome_index < len(self.wel_text):
            self.welcome_index += 1
            self.welcome_label.setText(self.wel_text[:self.welcome_index])
        else:
            self.timer.stop()  
    
    def thank_you(self):
        self.radio_deposite.hide()
        self.radio_withdraw.hide()
        self.radio_check.hide()
        self.radio_loan.hide()
        self.radio_transfer.hide()
        self.radio_stock.hide()
        self.end1_button.hide()
        self.welcome_label.hide()
        self.typewriter_label.setGeometry(80, 300, 900, 50)
        self.typewriter_label.setStyleSheet("font-size: 24px; font-family: Arial; color: red;")
        self.full_text = f"🙏🙏THANK YOU {self.current_user.upper()} FOR DOING BUSINESS WITH US🙏🙏"
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.thankyou_typewriter)
        self.timer.start(20)

    def thankyou_typewriter(self):
        if self.current_index < len(self.full_text):
            self.current_index += 1
            self.typewriter_label.setText(self.full_text[:self.current_index])
        else:
            self.timer.stop()

    def withdraw_room(self):
        if self.radio_withdraw.isChecked():
            amount, ok = QInputDialog.getInt(self, "Withdraw Amount", "ENTER THE AMOUNT TO WITHDRAW:")
            if not ok:
                return
            if amount <= 0:
                QMessageBox.warning(self, "Invalid Amount", "PLEASE ENTER A VALID AMOUNT")
                return
            if amount > self.users[self.current_user]["balance"]:
                QMessageBox.warning(self, "Insufficient Balance", "YOU DO NOT HAVE ENOUGH BALANCE")
                return
            self.users[self.current_user]["balance"] -= amount
            QMessageBox.information(self, "Withdrawal Successful", f"YOU HAVE WITHDRAWN {amount}. NEW BALANCE IS {self.users[self.current_user]['balance']}")
            
    
    def deposit_room(self):
        if self.radio_deposite.isChecked():
            amount, ok = QInputDialog.getInt(self, "Deposit Amount", "ENTER THE AMOUNT TO DEPOSITING:")
            if not ok:
                return
            if amount <= 0:
                QMessageBox.warning(self, "Invalid Amount", "PLEASE ENTER A VALID AMOUNT")
                return
            self.users[self.current_user]["balance"] += amount
            QMessageBox.information(self, "Deposit Successful", f"YOU HAVE DEPOSITED {amount}. NEW BALANCE IS {self.users[self.current_user]['balance']}")
    
    def check_balance(self):
        if self.radio_check.isChecked():
            balance = self.users[self.current_user]["balance"]
            QMessageBox.information(self, "Account Balance ", f"YOUR CURRENT BALANCE IS {balance}")
    
    def loan_room(self):
        pass
    
    def money_transfer(self):
        if self.radio_transfer.isChecked():
           uracc_bal = self.users[self.current_user]["balance"]
           rsep_num = QInputDialog.getText(self,"RECIPIENT NAME", "ENTER NAME")
           if rsep_num not in self.users:
               QMessageBox.warning(self,"INVALID ACCOUNT NUMBER")
               return
           if rsep_num in self.users:    
               tran_amt = QInputDialog.getInt(self,"TRANSFER AMOUNT","ENTER AMOUNT (LIMIT UPTO 100K)")
               if tran_amt <= 0 or tran_amt >100000:
                  QMessageBox.warning(self,"CAN'T THIS AMOUNT")
                  return
               if tran_amt > 0 or tran_amt <= 100000:
                  uracc_bal -=tran_amt
                  rsep_num["balance"] += self.users["balance"] 
                   
                   
               
   
    def stock_market(self):
        pass
            

    def authct_name(self):
        text = self.line_edit.text().strip().lower()
        if text not in self.users:
            QMessageBox.warning(self, "Authentication Failed", "USER NOT FOUND")
            return False
        else:
            self.current_user = text
            QMessageBox.information(self, "Authentication Successful", f"WELCOME {self.current_user.upper()}")
            return True

    def authct_pin(self):
        if self.current_user is None:
            QMessageBox.warning(self, "Error", "Please authenticate username first")
            return False
        pin_text = self.pin_num.text().strip()
        if not pin_text.isdigit() or int(pin_text) != self.users[self.current_user]["pin"]:
            QMessageBox.warning(self, "Authentication Failed", "INVALID PIN")
            return False
        else:
            QMessageBox.information(self, "Authentication Successful", "PIN VERIFIED")
            return True

    def authenticate(self):
        if self.authct_name() and self.authct_pin():
            self.nxt_lobby()
            
            
    def generate_random_otp(self):
        gen_code = random.randint(0, 999999)
        return gen_code

    def timeperiod(self):
        typem, ok1 = QInputDialog.getText(self, "Time Period Type", "WHAT WILL BE THE TIME PERIOD FOR YOUR LOAN (YEARS/MONTHS/DAYS):").upper()
        if not ok1:
            return 0
        typem = typem.strip().upper()
        time_period, ok2 = QInputDialog.getInt(self, "Time Period", "ENTER THE TIME PERIOD:")
        if not ok2:
            return 0
        if typem == "YEARS":
            return time_period
        elif typem == "MONTHS":
            return time_period / 12
        elif typem == "DAYS":
            return time_period / 365
        else:
            QMessageBox.warning(self, "Invalid Input", "PLEASE ENTER A VALID TIME PERIOD TYPE")
            return 0

    def interest(self):
        personal = 0.08
        NEWcarloan = 0.05
        USEDcarloan = 0.07
        studentloan = 0.05
        smallbusiness = 0.09
        typeo, ok = QInputDialog.getText(self, "Loan Type", "WHAT IS THE TYPE OF LOAN YOU WANT:")
        if not ok:
            return None
        typeo = typeo.strip().lower()
        if typeo == "personal":
            return personal
        elif typeo == "newcarloan":
            return NEWcarloan
        elif typeo == "usedcarloan":
            return USEDcarloan
        elif typeo == "studentloan":
            return studentloan
        elif typeo == "smallbusiness":
            return smallbusiness
        else:
            QMessageBox.warning(self, "Invalid Input", "PLEASE ENTER A VALID LOAN TYPE")
            return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
