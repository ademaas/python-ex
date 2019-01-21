
def calculate_average(group_list):
    
    ind_pay = []
    sum =0
    for i in range(group_list):
        x = float(input('Enter the sum (eur) paid by participant no {:d}.\n'.format(i+1)))
        ind_pay.append(x)
        sum=sum+x
    print('Total costs are {:.2f} eur.'.format(sum))
    average = sum/group_list
    for i in range(len(ind_pay)):
        if(ind_pay[i]>= average):
            print('Participant no ',i+1,' should receive {:.2f} eur.'.format(ind_pay[i]-average))
        else:
            print('Participant no ',i+1,' should pay {:.2f} eur.'.format(average-ind_pay[i]))






def main():
    group_list = int(input('Enter the number of the participants.\n'))

    while(group_list < 2):
        print('The number must be at least 2!\n')
        group_list = int(input('Enter the number of the participants.\n'))

    calculate_average(group_list)
    


    


main()