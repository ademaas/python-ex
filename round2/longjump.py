def main():
    input1= input('Enter the length of the first jump (cm).\n')
    first_jump = int(input1)
    if(first_jump > 0):
       n= 1
       sum_of_jumps = first_jump
       longest_jump = first_jump
       while(True):
           inp2 = input('Enter the length of the next jump (cm).\n')
           next_jump = int(inp2)
           if(next_jump > 0):
               n = n+1
               sum_of_jumps = sum_of_jumps + next_jump
               if(next_jump > longest_jump):
                    longest_jump = next_jump
           else:
                break

       average = sum_of_jumps/n
       print('The longest jump was',longest_jump,'cm.')
       print('The average of the jumps was', average,'cm.')  
    else:
        print ('You did not enter any results.')


main()
    

       


