input1 = input('Enter the amount of the alcoholic drink (l).\n')
x = float(input1)
input2 = input('Enter the alcohol content of the alcoholic drink (%)\n')
y = float(input2)
nonalcholic = input('How much non-alcoholic drink do you want to add (l)?\n')
z= float(nonalcholic)
Alchol_content = x*y/(x+z)

print('Alcohol content of the drink is',Alchol_content,'%.')