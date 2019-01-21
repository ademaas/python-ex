def main():
    inp1 = input('Enter a positive integer to be tested:\n')
    number = int(inp1)
    if(number % 2 == 0):
        quetient = number/2
        while(quetient!=0 or quetient!=1):
            if(quetient%2==0):
                number = quetient
                quetient = number/2
                
            else:
                #print('The number is not a power of two.\n')
                break
        if(quetient==1):
            print('The number is a power of two.\n')
        else:
            print('The number is not a power of two.\n')

    elif(number==1):
        print('The number is a power of two.\n')
    else:
        print('The number is not a power of two.\n')


main()