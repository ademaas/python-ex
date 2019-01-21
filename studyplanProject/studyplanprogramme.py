#The programme creates student objects and course objects 
# and prints their functionality.
import  student
import  course
#Checks the validity of the input for a student ID
#It needs to be an integer
def input_cou():
    ok = False
    while(not ok):
        try:
            id = int(input('student ID:\n'))
            ok = True
        except ValueError:
            print('Value should be in  integer, please try again')
    return id
#checks if the schedule of two courses are over laped
def time_check(current_lis,added_list):
    ok=False
    while(not ok):
        if(current_lis==added_list):
            ok= True
    

def course_input(periodic_list):
    catalog = []       
    
    while(True):
        i=0
        
        course_name= input('Enter the name of the course from the available list?\n') 
        
        for cour in periodic_list:
            if (course_name == cour[0]):
                catalog.append(cour) 
                if(len(catalog) > 1):                                    
                    for x in catalog:
                        if (x[2]==cour[2] and x[3]==cour[3]):
                            del x
                                                                                               
                        
                                   
             
        cont = input('Do you want to add more courses (Y/N)')
        if cont =='N':
            break
        i= i+1
    return catalog

def select_option():

    print()      
    print('------------------------------------------')
    print("Choose period to add courses")
    print('-------------------------------------------')
    print("1: Add period I courses!")
    print("2: Add period II courses!")
    print("3: Add period III courses!")
    print("4: Add period IV courses!")
    print("5: Add period V courses!")
    print("6: Continue adding new student or Exit")
    selection = int(input())
    return selection

def add_student():
    
    ok = False
    print()
    print('Select "1" to add New student to the system, "2" to exit from the system\n')
    print("1: Add new student to the system")
    print("2: Exit from the system")
    while(not ok):
        int_opt = 0
        try:
            int_opt = int(input('Add options "1" OR "2":'))
            ok = True
        except ValueError:
            print('Error, Please enter integr value!')
    return int_opt

def print_periodic_courses(period,per_num):
    print('The list of  courses for period {:d} is:'.format(per_num))
    
    for period_x in period:
        print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(period_x[0],period_x[1],period_x[2],period_x[3],period_x[4]))




def main():
    #The programme asks the user to insert the name of the student object and his id number.
    print('================================================')
    print('**** Lis of Courses for academic year 2018-2019 *****') 
    print('================================================')
    file_name = input("Enter the name of the file which has list :\n")    
    period_I = []
    period_II = []
    period_III = []
    period_IV = []
    period_V = []
     
    try:
        resultfile = open(file_name, "r")
        for line in resultfile:
            line= line.rstrip()
            course_line = line.split(',') 
            if course_line[-1]=='I':
                period_I.append(course_line) 
            if course_line[-1]=='II':
                period_II.append(course_line) 
            if course_line[-1]=='III':
                period_III.append(course_line) 
            if course_line[-1]=='IV':
                period_IV.append(course_line) 
            if course_line[-1]=='V':
                period_V.append(course_line) 
                            
            print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(course_line[0],course_line[1],course_line[2],course_line[3],course_line[4]))
    
        resultfile.close()    
        option = add_student()
   
        periodic_catalog = []    
        ok = True
        counter = 1
        while(ok):
            if(option==1):            
                print('Add student {:d}'.format(counter))
                student_name = input('Please write the name of the student ?\n')
                student_id= input_cou()
                student1 = student.Student(student_name,student_id)    
                #course1 = course.Course(course_name,course_code)            
                #The programme also needs to create a course object
                print('Add courses to the course catalog for : ',student_name)
                select_opt= select_option()
                if(select_opt==1):
                    
                    print('Available courses for period I: ')
                    print('=====================================================================')
                    print(' Course Name       Code         Day       Time       Period')
                    print("=====================================================================")
                    for p in period_I:
                        print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(p[0],p[1],p[2],p[3],p[4]))                    

                    print('Add courses: ')
                    print('-------------------------------------------')
                    course1 = course.Course(select_opt)          
                    
                    course1.get_course_list(course_input(period_I)) 
                    print('Study plan for period I is:')
                    print('=====================================================================')
                    print(course1.print_period())                                 
                    periodic_catalog.append(course1.return_toCatalog())                
                    select_opt= select_option()
                if(select_opt==2):
                    print('Available courses for period II: ')
                    print('=====================================================================')
                    print(' Course Name       Code         Day       Time       Period')
                    print("=====================================================================")
                    for p in period_II:
                        print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(p[0],p[1],p[2],p[3],p[4])) 
                    print('Add courses: ')
                    print('-------------------------------------------')
                    course2 = course.Course(select_opt)                    
                    course2.get_course_list(course_input(period_II))
                    print('Study plan for period II is:')
                    print('=====================================================================')
                    print(course2.print_period())
                    periodic_catalog.append(course2.return_toCatalog())                                
                    select_opt= select_option()
                if(select_opt==3):
                    print('Available courses for period III: ')
                    print('=====================================================================')
                    print(' Course Name       Code         Day       Time       Period')
                    print("=====================================================================")
                    for p in period_III:
                        print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(p[0],p[1],p[2],p[3],p[4])) 
                    print('Add courses : ')
                    print('-------------------------------------------')
                    course3 = course.Course(select_opt)                    
                    course3.get_course_list(course_input(period_III))
                    print('study plan for period III is:')
                    print('=====================================================================')
                    print(course3.print_period())
                    periodic_catalog.append(course3.return_toCatalog())                                
                    select_opt= select_option()
                if(select_opt==4):
                    print('Available courses for period IV: ')
                    print('=====================================================================')
                    print(' Course Name       Code         Day       Time       Period')
                    print("=====================================================================")
                    for p in period_IV:
                        print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(p[0],p[1],p[2],p[3],p[4])) 
                    print('Add courses :')
                    print('-------------------------------------------')
                    course4 = course.Course(select_opt)                    
                    course4.get_course_list(course_input(period_IV))
                    print('Study plan for period IV is:')
                    print('=====================================================================')
                    print(course4.print_period())                     
                    periodic_catalog.append(course4.return_toCatalog())        
                
                    select_opt= select_option()
                if(select_opt==5):
                    print('Available courses for period I: ')
                    print('=====================================================================')
                    print(' Course Name       Code         Day       Time       Period')
                    print("=====================================================================")
                    for p in period_V:
                        print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(p[0],p[1],p[2],p[3],p[4])) 
                    print('Add courses for period V')
                    print('-------------------------------------------')
                    course5 = course.Course(select_opt)                   
                    course5.get_course_list(course_input(period_V))
                    print('Study plan for period V is:')
                    print('=====================================================================')
                    print(course5.print_period()) 
                    periodic_catalog.append(course5.return_toCatalog())          
                
                    select_opt= select_option()
                if(select_opt==6):
                    student1.course_catalog(periodic_catalog)
                    print('Study plan for the academic year:')            
                    print ('---------------------------------------------------------------------')                    
                    print(student1)
                    print ('---------------------------------------------------------------------')
                    print(student1.annual_course())
                    
                #option = input('Add new student or exit')
                periodic_catalog = []                                                                  
                option = add_student() 
                counter += 1                
           
            else:
                ok = False
                break
    
    except OSError:
        print("Error in reading file {:s}. Closing program.".format(file_name))
    


            
    #course_name = input('Please write the name of the course ?\n')
    #course_code = input('Please enter the course code ?\n')    
    #print(course1)





main()





