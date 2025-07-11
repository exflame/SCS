import streamlit as stt
stt.set_page_config(page_title="Bank App", layout="centered")

 class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        
class CurrentAccount(Account):
    def _init_(self, balance):
        super()._init_(balance)


current = CurrentAccount(67000)

class SavingsAccount(Account):
    def __init__(self,balance):
        super().__init__(balance)
    
    def Withdraw(self, amount):
        if(amount < 1000):
            super().withdraw(amount)
        else:
            print(" Withdrawal limit exceeded")

savings = SavingsAccount(42500)


PIN = "2098" 

user_pin = stt.text_input("Enter your PIN", type="password")

if user_pin == PIN:
    stt.success("PIN verified successfully!")

    with stt.form("account_form"):
        account_type = stt.selectbox("Select Account Type", ("Savings", "Current"))
        stt.write=("You selected:",account_type)
        amount = stt.number_input("Enter Amount", min_value=1000)
        amount = stt.number_input("Enter Amount", max_value=50000)
        operations = stt.selectbox("Select Type", ("Deposit", "Withdraw"))
        submit = stt.form_submit_button("Submit")

        if submit:
            if operations == "Withdraw":
                if account_type == "Savings":
                    if savings.withdraw(amount):
                        stt.success(f"Successfully withdrew {amount} from Savings Account.")
                    else:
                        stt.error("Insufficient balance in Savings Account.")
                elif account_type == "Current":
                    if current.withdraw(amount):
                        stt.success(f"Successfully withdrew {amount} from Current Account.")
                    else:
                        stt.error("Insufficient balance in Current Account.")
            elif operations == "Deposit":
                if account_type == "Savings":
                    savings.deposit(amount)
                    stt.success(f"Successfully deposited {amount} into Savings Account.")
                elif account_type == "Current":
                    current.deposit(amount)
                    stt.success(f"Successfully deposited {amount} into Current Account.")
else:
    stt.error("Wrong PIN. Please try again.")


