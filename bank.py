
from datetime import datetime
class Account:
    def __init__(self,phoneNumber ,name,transactions):
         self.phoneNumber=phoneNumber
         self.name=name
         self.balance=0
         self.loanLimit=400
         self.transactions=[]


    def name(self):
         return f"hello this  is {self.phoneNumber}, {self.id} {self.name}"



    def send(self):
        withdraw=234568
        Send=4567890
        return f"hello this  is {self.withdraw}and{self.send}"


    def show_balance(self):
        return self.balance



    def deposit(self,amount):
        if amount<=0:
            return f"The {amount} must be greater than zero"
        else:
            self.balance +=amount
            transaction={"amount":"amount","balance":"self.balance","time":datetime.now(),"narration":"Deposit"}
            self.transactions.append(transaction)
            return f" dear {self.amount} you have deposited KES {amount} your new balance is{self.balance}"



    def withdraw(self,amount):
        if amount>0:
            return f" Dear {self.name} you have withdrawn{amount}"
        elif amount<=0:
                return f"The amount must be greater than zero"
        elif amount>self.balance:
                return f"the amount must be less than the balance"
        else:
                self.balance-=amount
                return f"{self.balance}"

    def borrow(self,amount):
        if amount>self.loan__Limit:
            return f"amount is greater than your limit"
        elif self.loan>0:
            return f"you have already an existing loan"
        else:
            self.loan+=1
            self.balance+=amount
            return "you have successfully borrowed"


    def get_statement(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            print(f'{time.strftime("%D")}date of transaction{narration},{amount} transacted, and now your balance is{balance}')






def repay_loan(self,amount):
        if amount<=0:
            return f"you are above your loan limit"
        elif amount<self.loan:
            self.loan-=amount
            return f"amount has been reduced"
        else:
            extra=amount-self.loan
            self.balance+=extra
            repay_loan={
                "amount":amount,
                "balance":self.balance,
                "time": now.strftime ("%D"),
                "narration":"Deposit"
                }
            self.transaction(repay_loan)
            return f"dear {self.name} you have repay your loan and your balance is {self.balance}"







