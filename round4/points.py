import math


def distance(x1, y1, x2, y2):
    x= x1-x2
    y= y1-y2
    length = math.sqrt(x**2 + y**2) 
    return length

def area(x1, y1, x2, y2):
    length = math.fabs(x2-x1)
    width = math.fabs(y2-y1)
    area = length * width
    return area

def main():
    x1 = float(input('Enter the x coordinate of the first point.\n'))
    y1 = float(input('Enter the y coordinate of the first point.\n'))
    x2 = float(input('Enter the x coordinate of the second point.\n'))
    y2 = float(input('Enter the y coordinate of the second point.\n'))

    distance_xy = distance(x1, y1, x2, y2)
    area_rec = area(x1, y1, x2, y2)

    print ('The distance of the points is {:.2f}.\n'.format(distance_xy))
    print('The area of the rectangle defined by the points is {:.2f}.'.format(area_rec))


main()

    

    
