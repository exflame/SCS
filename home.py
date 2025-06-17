import streamlit as stt
stt.set_page_config(page_title="Bank App", layout="centered")

# savings = SavingsAccount(42500)
# current = CurrentAccount(67000)

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


