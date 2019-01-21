
def calculate_vat(sales):
    for sale in sales:
        sale= sale.rstrip()

def main():
    name = input("Enter the name of the file containing selling prices.\n") 
    
    sum_vat =0
    try:
        sales_file = open(name, "r")
        print('{:>9s}       VAT    Price (incl. VAT)'.format('Price'))
        #print('{:>9}{:>9}{:>18}'.format('Prices','VAT','Price (incl. VAT)'))
        for line in sales_file:
            line = line.rstrip()
            sales = float(line)
            vat = sales*0.24
            sum_vat += vat
            inc_vat= sales + vat  
            print('{:9.2f} {:9.2f} {:9.2f}'.format(sales,vat,inc_vat))          
        sales_file.close()
        print('------------------------------------------')
        print('Total VAT {:.2f} eur.\n'.format(sum_vat))
        
    except OSError:
        print("Error in reading file {:s}. Closing program.".format(name))
    except ValueError:
        print("Incorrect line in file {:s}. Closing program.".format(name))


main()
