def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()
    
# balance : 잔액
def deposit(balance, money):
    print("입금이 완료됐습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money  

def withdraw(balance, money):
    if balance >= money:
        print("출금 완료. 잔액 {0}원".format(balance-money))
        return balance - money
    else:
        print("출금 완료 x. 잔액은 {0}원".format(balance))
        return balance
    
# commission : 수수료
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance,500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))