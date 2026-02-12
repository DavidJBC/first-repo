
def calc():

    Sales = float(input("Enter The Total Sales: "))

    CountryTax = float(input("Enter The Percentage of The Country Tax: "))
    SalesTax = float(input("Enter The Percentage of The Sales Tax: "))

    CountryTaxRate = CountryTax / 100
    SalesTaxRate = SalesTax / 100

    CountryTaxValue = Sales * CountryTaxRate
    SalesTaxValue = Sales * SalesTaxRate

    TotalTax = CountryTaxValue + SalesTaxValue

    SalesWithTax = Sales - TotalTax

    print("Total Sales Without Taxes " + str(Sales))
    print("The Country Tax is " + str(CountryTaxValue))
    print("The Sales Tax is " + str(SalesTaxValue))
    print("The Total Tax is " + str(TotalTax))
    print("Total Sales With Taxes " + str(SalesWithTax))

    
calc()