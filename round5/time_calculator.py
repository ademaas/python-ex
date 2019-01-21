
def read_time():
    time = []   
   
    h = int(input('Input the hours.\n'))
    while(h<0 or h> 23):
        h = int(input('Input the hours.\n'))

    time.append(h)    
    m= int(input('Input the minutes.\n'))
    while(m<0 or m>59):
        m= int(input('Input the minutes.\n'))
    time.append(m)   
    
    return time

def is_smaller_or_equal(time1, time2):
    if(time1[0]<= time2[0]):
        return True
    else:
        return False
def calculate_difference(first_time, second_time):
    if(is_smaller_or_equal(first_time, second_time)):
        t1 = first_time[0]*60 + first_time[1]
        t2= second_time[0]*60 + second_time[1]
        t_diff= t2 -t1
        minutes= t_diff%60
        hours = (t_diff - minutes)/60
        return hours, minutes
    else:
        t1 = first_time[0]*60 + first_time[1]
        t2 = 24*60 + second_time[0]*60 + second_time[1]
        t_diff = t2 -t1
        minutes = t_diff%60
        hours = (t_diff - minutes)/60
        return hours , minutes



    

def main():

    print('Input the first time.')
    time1 = read_time()

    print('Input the second time.')
    time2 = read_time()
    hours , minutes = calculate_difference(time1,time2)
    print('The difference is {:.0f} h {:.0f} min.'.format(hours, minutes))

main()