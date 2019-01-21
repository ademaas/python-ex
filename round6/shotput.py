def user_input(shot):
    if(len(shot)!=0):
        maxim= shot.split(',')
        #max_num = float(shot)
        maxim= map(float,maxim)

        print('The best result is {:.2f} m.'.format(max(maxim)))
    else:

        print('No accepted results.')

def main():
    input_str = [0]
    input_str = input('Enter the lenghts of the throws (m) separated by commas.\n')
    user_input(input_str)

main()