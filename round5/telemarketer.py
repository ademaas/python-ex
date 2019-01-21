def calculate_profit(list_orders):
    sum= 0
    print('Payments of each day:\n')
    for x in list_orders:
        if x > LIMIT:
            profit = LIMIT*NORMAL_PAYMENT + (x-LIMIT)*HIGHER_PAYMENT
        else:
            profit = x* NORMAL_PAYMENT
        print_profit(profit)
        sum = sum + profit
    print('Total payment: {:.2f} eur\n'.format(sum))
    
def print_profit(profit):
    print('{:.2f} eur'.format(profit))





def main():
    count = int(input("Enter the number of the days.\n"))
    orders = [0.0] * count
    for i in range(count):
        no_of_orders = int(input("Enter the number of orders sold the next day.\n"))
        orders[i] = no_of_orders

    calculate_profit(orders)

    
    
LIMIT = 10
NORMAL_PAYMENT = 5.0
HIGHER_PAYMENT = 8.0

main()

# Write your own code below. It should iterate over the list orders,
# print the payment of each day and finally print the total payment.

# Do not forget to call the main function.