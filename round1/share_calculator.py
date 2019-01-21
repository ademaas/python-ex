input1 = input('Enter the selling price of the shares (eur/share):\n')
x = float(input1)
input2 = input('Enter the number of the shares:\n')
y = int(input2)
number_month = input('How many months have you owned the shares?\n')
z= int(number_month)
selling_p = float(8.80)
brokerage_fee = float(7.50)
custody_fee = float(1.75)
profit =  (x*y) - (selling_p*y)- (2* brokerage_fee + custody_fee*z)


print ('Profit from selling the shares is',profit,' euros.')
