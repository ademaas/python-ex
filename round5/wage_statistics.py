

def calculate_daily_pay(daily_hours, hourly_wages):


    if (daily_hours <= 8):
        single_emp_wage = daily_hours * hourly_wages
    elif(daily_hours > 8 and daily_hours <10):
        single_emp_wage = 8*hourly_wages + (daily_hours-8)*1.5*hourly_wages
    else:
        single_emp_wage = 8*hourly_wages + 2*1.5*hourly_wages + (daily_hours-10)*2*hourly_wages

    return single_emp_wage

def read_hours():
    hours = []
    print('Enter the working hours. Stop by giving a negative value.')
    inp = float(input('Enter the working hours of the 1st worker:\n'))
    if(inp < 0):
        print('No working hours were entered.')
        return 
    else:
        #hours.append(inp)
        while(inp>=0):
            hours.append(inp)
            inp = float(input('Enter the working hours of the next worker:\n'))
            
        return hours


def calculate_wages(hours, hourly_wages):

    daily_wage = []    
    for h in range(len(hours)):
        daily_wage.append(calculate_daily_pay(hours[h], hourly_wages))

    return daily_wage



def calculate_average(wages_list):
    sum =0
    
    for i in range(len(wages_list)):
        sum = sum + wages_list[i]
    average = sum/len(wages_list)
    
    return average
    


def wages_out_of_interval(wages_list, lower_limit, upper_limit):
    counter =0  
    
    
    for x in range(len(wages_list)):
        if(wages_list[x] <= lower_limit or wages_list[x] >= upper_limit):
            counter = counter +1
    return counter

def output_wages(wages_list):    

    print('Wages:')

    for i in range(len(wages_list)):
        print('{:.2f} eur'.format(wages_list[i]))
    

def main():

     hourly_wages = float(input('Enter the hourly wages in euros:\n'))
     hours = read_hours()
     if (hours):
         wages_list = calculate_wages(hours, hourly_wages)
         output_wages(wages_list)
         average = calculate_average(wages_list)
         print('The average wage is {:.2f} eur.'.format(average))
         counter = wages_out_of_interval(wages_list, 0.75*average, 1.25*average)
         print('The number of the wages that differs over 25 % from the average is {:d}.'.format(counter))






    

main()