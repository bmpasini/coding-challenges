# You have some money in your bank account, the only function to withdraw money is
# uint16 Withdraw(uint16 value), if the value is greater than the money you have it
# returns 0, otherwise it withdraws the requested amount and returns the "value" 
# Write a function that withdraws all your money.

class Bank(object):

    def __init__(self, total):
        self.total = total
        self.max = 1 << 15

    def withdraw(self, i):
        if i > self.total:
            return 0
        self.total -= i
        return i

    def withdraw_all(self):
        total = 0
        amount = self.max
        while amount > 0:
            total += self.withdraw(amount)
            amount >>= 1
        return total

if __name__ == "__main__":
    bank = Bank(500)
    bank.withdraw_all()
