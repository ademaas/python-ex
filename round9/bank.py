import bank_account

def read_account():
    ok = False
    while not ok:
        try:
            amount = float(input('Enter the amount to be deposited into the second account.\n'))
            ok = True
        except ValueError:
            print("ERROR: You did not enter a valid integer!")
            print("Try again!")
    return amount
        
        

def main():
    #account_num = input('Enter the id of the second bank account.\n')
    #owner = input('Enter the owner of the second bank account.\n')
    first_ba = bank_account.BankAccount('FI5511112222333344','Kari Kemisti')
    #amount = read_account()
    first_ba.deposit(112.50)
    print('The balance of the first account is {:.2f} eur.'.format(first_ba.get_balance()))
    amount_withd= first_ba.withdraw(90)
    print('The amount withdrawn from the first account was {:.2f} eur.'.format(amount_withd))
    account_num = input('Enter the id of the second bank account.\n')
    owner = input('Enter the owner of the second bank account.\n')
    second_ba = bank_account.BankAccount(account_num,owner)
    amount = float(input('Enter the amount to be deposited into the second account.\n'))
    second_ba.deposit(amount)
    print('The balance of the second account is {:.2f} eur.'.format(second_ba.get_balance()))
    secon_withd = float(input('Enter the amount to be withdrawn from the second account.\n'))
    second_withdr = second_ba.withdraw(secon_withd)
    print('The amount withdrawn was {:.2f} eur.'.format(second_withdr))
    print('The bank accounts:')
    print(first_ba)
    print(second_ba)

    transfer_amou = float(input('Enter the amount to be transferred\n'))
    if(first_ba.transfer(transfer_amou,second_ba)):
        print('Transfer from the first account into the second account was successful!')
    else:
        print('It was not possible to carry out the bank transfer!')
    print('Bank accounts at the end:')
    print(first_ba)
    print(second_ba)








main()

