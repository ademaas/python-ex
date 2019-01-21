# Define the function "cuber" here.
def cuber(number):
    cube= number **3
    return cube

def main():
    input_number = int(input("Enter a number to cube:\n"))
    number_cubed = cuber(input_number)
    print("Your number cubed is", number_cubed)

main()

