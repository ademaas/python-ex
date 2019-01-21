def main():
    input1= input('Enter the annual income (eur).\n')
    tax_inc = int(input1)

    if tax_inc >= 0 and tax_inc < 1500:
        tax = tax_inc * 0.085
       
    elif tax_inc >= 1500  and tax_inc < 29000:
        tax = tax_inc * 0.25
    elif tax_inc >= 29000  and tax_inc < 45000:
        tax = tax_inc * 0.35
    elif tax_inc >= 45000  and tax_inc < 60000:
        tax = tax_inc * 0.45
    else:
        tax = tax_inc * 0.60
    
    print('Amount of the tax is',tax,' euros.')


main()