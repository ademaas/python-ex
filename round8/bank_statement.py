
def print_sum(sum,rep_name):
    print('The total sum paid to {:s} is {:.2f} eur.'.format(rep_name,sum))
def reading_contents_of_file(bankstatment,rep_name):
    total_sum =0
    for banks in bankstatment:
        banks = banks.rstrip()
        recipent_file = banks.split('\t')
        
        if len(recipent_file)<5:
            pass
        else:
            if(recipent_file[4]==rep_name):
                try:
                    forth_data= float(recipent_file[3])
                    if forth_data < 0:
                        total_sum += forth_data
                except ValueError:
                    pass
            else:
                total_sum += 0
    return abs(total_sum)                 
          
def main():

    name = input('Enter the name of the file containing the bank statement.\n')   
    rep_name = input('Enter the name of the recipient.\n')
    
    try:
        bank_stat = open(name,'r')
        reci_amount = reading_contents_of_file(bank_stat,rep_name)
        print_sum(reci_amount,rep_name)        

    except OSError:
        print("ERROR in reading file {:s}".format(name))



main()