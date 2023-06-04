class Account:
    def __init__(self, accNo, accName, accBalance):
        self.accNo = accNo
        self.acctName = accName
        self.accBalance = accBalance


class AccountDemo(Account):
    def __init__(self):
        pass

    def depositAmnt(self, acnt, amount):
        acnt.accBalance += amount
        return acnt.accBalance

    def withdrawAmnt(self, acnt, amount):
        acnt.accBalance -= amount
        if acnt.accBalance >= 1000:
            return acnt.accBalance
        else:
            return "No Adequate balance"


# Sample main section.
# Do not remove the below portion of code.
if __name__ == '__main__':
    acno = int(input())
    acname = input()
    acntbal = int(input())
    depamnt = int(input())
    withamnt = int(input())

    acnt = Account(acno, acname, acntbal)
    acntdemoobj = AccountDemo()

    print(acntdemoobj.depositAmnt(acnt, depamnt))
    print(acntdemoobj.withdrawAmnt(acnt, withamnt))
