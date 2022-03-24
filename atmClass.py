class ATM(object):
    def __init__(self,atmNumber,pinCode,balanceAmount):
        self.atmNumber = atmNumber
        self.pinCode = pinCode
        self.balanceAmount = balanceAmount

    def balanceEnquiry(self):
        print(self.balanceAmount)

    def cashWithdrawal(self, amount):
        self.balanceAmount = self.balanceAmount-amount
        print("The updated balance is:- "+str(self.balanceAmount))

p1 = ATM(9044738944849944, 8574, 123896)

p1.balanceEnquiry()
p1.cashWithdrawal(12434)