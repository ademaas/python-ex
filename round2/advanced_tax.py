def main():

    inp = input('Enter annual income (eur).\n')
    income = int(inp)
    if(income >0 and income <=15000):
        income_tax = income* 0.085
        tax_perc = (income_tax/income)*100
    elif(income >15000 and income <=29000):
        income_tax = (income-15000)* 0.25 + 15000*0.085
        tax_perc = (income_tax/income*100)
    elif(income >29000 and income <=45000):
        income_tax = (income-29000)* 0.35 + 14000*0.25 + 15000*0.085
        tax_perc = (income_tax/income*100)
    elif(income >45000 and income <=60000):
        income_tax = (income-45000)* 0.45 + 16000*0.35 + 14000*0.25 + 15000*0.085
        tax_perc = (income_tax/income) *100
    else:
        income_tax = (income-60000) * 0.6 + 15000*0.45 + 16000*0.35 + 14000*0.25 + 15000*0.085
        tax_perc = (income_tax/income)*100
    print('Total amount of the tax is ',income_tax,' euros.\n')

    print('The tax rate is ',tax_perc,' %.\n')  

    
    
main()  



        