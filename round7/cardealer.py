def profit_calculator(purchase,sale):
    profit = sale - purchase
    return profit
def print_profit(profit_list): 
    print('Finished reading the file.') 
    print('Profits (eur)')  
    for i in profit_list:
        print('{:.2f}'.format(i))
def print_tot_prof(list_prof):
    sum =0
    for i in list_prof:
        sum += i

    print('-----------------------------')
         
    print('Total {:.2f} eur.'.format(sum))

    
def reading_contents_of_file(contents):
    prof_list = []
    #list_info2 = []
    for line in contents:
        line = line.rstrip()
        list_info= line.split(',')
        #list_info2.append(list_info[3])
        #list_info2.append(list_info[4])

        if len(list_info)!=5:
            print('ERROR: incorrect line:',line)
        
        else:
            try:
                purchase = float(list_info[3])
                sale= float(list_info[4])
                profit=profit_calculator(purchase,sale)                
                prof_list.append(profit)
            
            except ValueError:
                print('ERROR: incorrect price in line:',line)
    
    return prof_list


def main():
    name = input('Input the name of the file to be read:\n')   
    prof_list = [] 
    
    try:
        car_info = open(name,'r')
        prof_list = reading_contents_of_file(car_info)
        if(len(prof_list)==0):
            print('There was no information about sold cars in the file.\n')
        else:
            print_profit(prof_list)
            print_tot_prof(prof_list) 

    except OSError:
        print("ERROR in reading the file.")



main()
