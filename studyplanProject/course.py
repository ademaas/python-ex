# The programme is mainly designed 
# for study plan of a student who is registerd for a certain course 
# the programe contains detail information about the course.
class Course:
    #initialize class attributes
    #The course class has three attributes the course code
    #name of the course and information of the the course time table
    #the course information contains period of the course(I-V),
    # week days and the time at which the course is taking place.
    def __init__(self, period):
        self.__course_period = period        
        self.__courseList = {}

    #returning the list of attributes
    #returning name of the course 
    def get_period(self):
        return self.__course_period    

    #returning the course information as a list
    def get_course_list(self,course_list):
        self.__courseList = course_list.copy()
        # for period_x in self.__courseList:
        #     print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(period_x[0],period_x[1],period_x[2],period_x[3],period_x[4]))
        return self.__courseList 


    #This method prints the list of courses a student added to his/her schedule in a single period.
    def print_period(self):
        for period_x in self.__courseList:
            print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(period_x[0],period_x[1],period_x[2],period_x[3],period_x[4]))



    def return_toCatalog(self):
        

        return self.__courseList

    