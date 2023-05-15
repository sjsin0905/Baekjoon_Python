def make_count():
    print("계좌 만들기 성공")


def deposit(balance, money):
    print("입금이 완료되었습니다. 남은 잔액{0}".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 남은 잔액{0}".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 남은 잔액{0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    if balance - commission >= money:
        print("출금이 완료되었습니다. 남은 잔액{0}".format(balance - commission - money))
        return commission, balance - money - commission
    else:
        print("잔액이 부족합니다. 남은 잔액{0}".format(balance))
        return commission, balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
print(str(commission) + "원")