class Atm:
    def __init__(self, cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print("Your balance is 50000000")
    def cash_withdrawl(self):
        print("I withdrawl 300000")
new_user = Atm(4100049761235, 1112)
new_user.check_balance()
new_user.cash_withdrawl()