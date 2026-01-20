import streamlit as st
import random
# function to open account
if "all_accounts" not in st.session_state:
    st.session_state.all_accounts=[]
def open_account(cnic, title, initial_deposit):
    account = {'cnic'            :cnic,
               'title'           :title,
               'balance'         :initial_deposit,
               'account_number'  :random.randint(1001,9999),
               'pin'             :random.randint(1001,9999)
              }
    st.session_state.all_accounts.append(account)
    return account
# Function to show current balance
def check_balance(account, pin):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                return acc['balance']
            else:
                return "Invalid Pin"
                
    else:
        return "Invalid Account Number" 
# function to withdraw amount
def withdraw(account, pin, amt):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                if acc['balance']>=amt:
                    acc['balance']-=amt
                    return acc['balance']
                else:
                    return "Insufficient Amount"
            else:
                return "Invalid Pin"                
    else:        
        return "Invalid Account Number" 
# Function to deposit amount
def deposit(account,amt):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            acc['balance']+=amt
            return  acc['balance']    
    else:        
        return "Invalid Account Number" 
# Function to transfer amount
def transfer(account, pin ,amt, bacc):
    for ba in st.session_state.all_accounts:
        if ba['account_number']==bacc:        
            for acc in st.session_state.all_accounts:
                if acc['account_number']==account:
                    if acc['pin']==pin:
                        if acc['balance']>=amt:
                            ba['balance']+=amt
                            acc['balance']-=amt
                            return acc["balance"]
                        else:
                            return "Insufficient Amount"
                    else:
                        return "Invalid Pin"                
            else:        
                return "Invalid Account Number" 
    else:
        return "Invalid Beneficiary Account Number"
closed_accounts=[]
# function to close account
def close_account(account, pin):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                closed_accounts.append(st.session_state.all_accounts.pop(st.session_state.all_account.index(acc)))
                return acc
            else:
                return "Invalid Pin"
    else:
        return "Invalid Account Number"
# Function to change PIN
def change_pin(account, pin, new_pin):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                acc['pin']=new_pin
                return acc
            else:
                return "Invalid Pin"
    else:
        return "Invalid Account Number"
#function to show all accounts
def show_all_account():
    return st.session_state.all_accounts

# Interface to user using streamlit
st.title("🏛 Simple Banking System")
st.write("This is a simple banking system .")

menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Check Balance", "Deposit", "Withdraw", "Transfer", "Show All Account","Close Account","Change pin"]
)
if menu=='Open Account':
   st.header("➕ open a new account")
   cnic= st.text_input("enter the cnic")
   title =st.text_input("enter the title")
   initial_deposit=st.number_input("enter the initial deposit" ,min_value=0)
   if st.button("create account"):
      
      acc=open_account(cnic,title,initial_deposit)
      st.success("account created sucessfully")
      st.write(f"**account num ** {acc['account_number']}")
      st.write(f"your pin is {acc["pin"]} save it ")
if menu=="Check Balance":
            st.header("check your balance")
            account=st.number_input("enter your account number")
            pin=st.number_input("enter your pin")
            if st.button("check balance"):
                acc=check_balance(account,pin)
                st.success(acc)
if menu=="Close Account":
    st.header("Close Account")
    account=st.number_input("enter your account number")
    pin=st.number_input("enter your amount to  pin")
    if  st.button("delete account"):
                    acc=close_account(account,pin)
                    st.success(acc)
if menu=="Change pin":
    st.header("change pin")
    account=st.number_input("enter your account num")
    pin = st.number_input("enter your pin")
    new_pin = st.number_input("enter your pin")
    if st.button("Change Pin"):
        acc=change_pin(account,pin,new_pin)
        st.success(acc)
if menu=="Deposit":
    st.header("Deposit section")
    account=st.number_input("enter acciunt num")
    amt=st.number_input("enter deposit amount")
    if st.button("DEPOSIT"):
        acc=deposit(account,amt)
        st.success(acc)
if menu=="Withdraw":
    st.header("💸🤑 Withdrawl section")
    account=st.number_input("enter your account num")
    pin=st.number_input("enter your account pin")
    amt=st.number_input("enter your account amount")
    if st.button("WITHDRAW"):
        acc=withdraw(account,pin,amt)
        st.success(acc)
if menu=="Transfer":
    st.header("💸🤑 Transfer section")
    account=st.number_input("enter your account num")
    pin=st.number_input("enter your account pin")
    amt=st.number_input("enter your account amount")
    bacc=st.number_input("enter your account of beneficiary")
    if st.button("transfer"):
        acc=transfer(account,pin,amt,bacc)
        st.success(acc)
if  menu=="Show All Account":
    st.header("here are your all accounts")
    if st.button("show me"):
        acc=show_all_account()
        st.success(acc)