import course


class Student:

    #initialization of the class with
    #student name, student id and list of courses the student is taking.
    def __init__(self,name,student_no):
        self.__name = name
        self.__id = student_no
        self.__courseList = []
    # returns the  name of the student
    def get_name(self):
        return self.__name
    #returns the student id 
    def get_id(self):
        return self.__id

    #return the list of courses selected
    def get_course_list(self):
        
        return self.__courseList
    #get a list of courses from the course class and store them in course list

    def course_catalog(self,course_list):
        self.__courseList= course_list.copy()

    #This Method prints the annual study plan of a student 
    
    def annual_course(self):
        for period in self.__courseList:
            
            for p in period:
                print(' {:s} \t{:>10s}\t{:s}\t{:>2s}\t{:>s}\n'.format(p[0],p[1],p[2],p[3],p[4]))                    
          
              
    # prints the student object
    def __str__(self):
        str1 = "Student name: "+ self.__name + " ID: " + str(self.__id)

        return str1