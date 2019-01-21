def main():
    inp1 = input('Enter the height of the chessboard.\n')
    height = int(inp1)
    while(height< 1 or height >20):
        print('The height must be in the interval 1-20!\n')
        inp1 = input('Enter the height of the chessboard.\n')
        height = int(inp1)
    inp2 = input('Enter the width of the chessboard.\n')
    width = int(inp2)
    while(width<1 or width > 79 ):
        print('The width must be in the interval 1-79!\n')
        inp2 = input('Enter the width of the chessboard.\n')
        width = int(inp2)
    tmp=0
    for i in range(height):
        for w in range(width):
            #print (x,end='')
            if((i+w)%2==0 ):
                print('_',end='')
                       
            else:
                print('#',end='')
            #tmp += 1
        print('\n')
        #tmp-=1
            

   

main()
