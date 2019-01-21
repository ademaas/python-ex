import math
def is_inside_circle(x1, y1, circle_x, circle_y, circle_r):
    pt_pos = distance(x1, y1, circle_x, circle_y)
    if pt_pos <=circle_r:
        return True
    else:
        return False

def is_inside_rectangle(x1, y1, left_x, lower_y, right_x, upper_y):

    left_x,lower_y = check_corners(left_x, lower_y, right_x, upper_y)
    x_pos = math.fabs(x1) - math.fabs(left_x)
    y_pos = math.fabs(y1) -math.fabs(lower_y)
    x_len = math.fabs(right_x) -math.fabs(left_x)
    y_len = math.fabs(upper_y) - math.fabs(lower_y)
    if(x_pos <= x_len and y_pos <= y_len):
        return True
    else:
        return False
  

def distance(x1, y1, x2, y2):
    x= x1-x2
    y= y1-y2
    length = math.sqrt(x**2 + y**2) 
    return length


def check_corners(corner1_x, corner1_y, corner2_x, corner2_y):
    # check the corners

    if math.fabs(corner1_x) < math.fabs(corner2_x) and math.fabs(corner1_y) < math.fabs(corner2_y):
        return corner1_x, corner1_y
    else:
        return corner2_x,corner2_y


def main():
    cir_counter = 0
    rec_counter = 0
    print('Enter the coordinates of the center of the circle.\n')
    circle_x = float(input('x coordinate:\n'))
    circle_y = float(input('y coordinate:\n'))
    radius = float(input('Enter the radius of the circle:\n'))
    while radius < 0:
        print('The radius cannot be negative!\n')
        radius = float(input('Enter the radius of the circle:\n'))
    print('Enter the coordinates of the first corner of the rectangle.\n')

    x1co_rec = float(input('x coordinate:\n'))
    y1co_rec = float(input('y coordinate:\n'))

    print('Enter the coordinates of the second corner of the rectangle.\n')

    x2co_rec = float(input('x coordinate:\n'))
    y2co_rec = float(input('y coordinate:\n'))

    no_pts = int(input('How many points are you going to input?\n'))

    for i in range(no_pts):
        print('Enter the coordinates of the next point.\n')
        xcor = float(input('x coordinate:\n'))
        ycor = float(input('y coordinate:\n'))
        if(is_inside_circle(xcor, ycor, circle_x, circle_y, radius)):
            cir_counter = cir_counter + 1

        if(is_inside_rectangle(xcor, ycor, x1co_rec, y1co_rec, x2co_rec, y2co_rec)):

            rec_counter= rec_counter +1


    print('{:d} points were inside the circle.\n'.format(cir_counter))
    print('{:d} points were inside the rectangle.\n'.format(rec_counter))



  

main()