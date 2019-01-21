def main():
    inp1 = input('Enter the number of one-zone trips:\n')
    no_in_tr = int(inp1)
    while(no_in_tr < 0):
        inp1 = input('Enter the number of one-zone trips:\n')
        no_in_tr = int(inp1)

    inp2 = input('Enter the number of regional trips:\n')
    no_reg = int(inp2)
    while(no_reg < 0):
        inp2 = input('Enter the number of regional trips:\n')
        no_reg = int(inp2)

    int_price = 1.10 * no_in_tr
    total_price = 1.10*no_in_tr + 2.10 * no_reg
    if(int_price >= 27.40 and total_price < 53.30):
        print('You should buy a one-zone season ticket.\n')
        print('The monthly price is {:.2f} euros.\n'.format(27.40 + no_reg*2.10))

    elif(total_price < 53.30):
          
        print('You should not buy a season ticket.\n')
        print('The monthly price is {:.2f} euros.\n'.format(total_price))
    else:
        print('You should buy a regional season ticket.\n')
        print('The monthly price is {:.2f} euros.\n'.format(53.30))


    

main()