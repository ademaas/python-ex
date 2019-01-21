def main():
    inp = input('Enter the number of courses.\n')
    courses = int(inp)
    count= 0
    average =0
    sum = 0
    if(courses <=0):
        print('The average cannot be calculated.\n')
    else:
        for i in range (courses):
            input1 = input('Enter the number of credits for the next course.\n')
            credits = float(input1)
            input2 = input('Enter the grade for this course.\n')
            grade = int(input2)
            if(credits <=0):                
                average = 0
                break
            sum = sum + credits* grade
            count = count + credits
            average = sum/count
        if(average ==0):
            print('The average cannot be calculated.\n')
        else:            
            print('The weighted average of the grades is{:3.2f}.\n'.format(average))


main()
