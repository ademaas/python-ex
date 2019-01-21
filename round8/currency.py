
def reading_file(f_name):
    curre_dict = {}
    for line in f_name:
        line = line.rstrip()
        line_dic = line.split(',')
        if len(line_dic)!=2:
            print('ERROR in line: ',line)
            
        else:
            identifier = line_dic[0]
            try:
                currency = float(line_dic[1])
                if currency <=0:
                    print('ERROR: the currency rate is not positive: ',line)
                else:
                    curre_dict.update({identifier:currency})

            except ValueError:
                print('ERROR: the currency rate is not valid: ',line)
    return curre_dict
                
def calculate_euro_value(rate,amount):
    return amount/rate

def print_total(total):
    print('The sum is {:.2f} euros.'.format(total))

def main():
    f_name = input('Enter the name of the file containing the currency rates.\n')
    
    try:
        file_name = open(f_name,'r')
        curre_dict = reading_file(file_name)
        #print(curre_dict)
        name_cur = input('Enter the name of the currency (stop by an empty line).\n')
        while(name_cur!=''):
            for id in curre_dict:
                if id == name_cur:
                   
                    amount_cur = input('Enter the sum in that currency.\n')
                    try:
                        amount = float(amount_cur)
                        total = calculate_euro_value(curre_dict[id],amount)
                        print_total(total)
                                              
                    except ValueError:
                        while(True):
                            print('ERROR: give the sum as a decimal number!')
                            amount_cur = input('Enter the sum in that currency.\n')
                            try:
                                amount = float(amount_cur)
                                total = calculate_euro_value(curre_dict[id],amount)
                                print_total(total)
                                break
                            except ValueError:
                                pass

                       
                        

                        
                            
            if name_cur not in curre_dict:
                print('ERROR: unknown currency.')
            name_cur = input('Enter the name of the currency (stop by an empty line).\n')
        print('Program closing.\n')


    except OSError:
        print('ERROR in reading file. Program terminates.')

main()