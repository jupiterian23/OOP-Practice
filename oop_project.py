from bank_account import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposite(500)

Dave.withdraw(100)

Dave.transfer(100, Sara)

Jim = InterestRewwardsAcct(1000,"Jim")

Jim.getBalance()

Jim.deposite(100)

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposite(100)

Blaze.transfer(1000, Sara)