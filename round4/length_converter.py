import math

# Define suitable constants for conversion here
ft_to_cm = 12*2.54


# Define the functions here

def to_imperial():
    length_cm = int(input('How tall are you in centimetres?\n'))
    length = length_cm/ft_to_cm
    ft_len = math.trunc(length)
    remainder = (length - ft_len)*12
    len_in = math.trunc(remainder)

    print('You are {:d} feet and {:d} inches tall.\n'.format(ft_len,len_in))


def to_metric():
    length_ft = int(input('How tall are you (in feet)?\n'))
    length_in = int(input('And how many inches on top of that?'))
    length_in_cm  =  ft_to_cm* length_ft + length_in*2.54
    print('You are {:.0f} centimetres tall.'.format(length_in_cm))

def main():
   print("1. Convert from the metric system")
   print("2. Convert to the metric system")
   print("3. End")
   choice = int(input("What do you want to do?\n"))
   while (choice != 3):
       if(choice ==1):
           to_imperial()
       if(choice ==2):
           to_metric()
       print("Do you want to continue?")
       print("1. Convert from the metric system")
       print("2. Convert to the metric system")
       print("3. End")
       choice = int(input("What do you want to do?\n"))
    
   print("Program terminating.")

main()

 
