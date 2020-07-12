ounces = 1571
pints_in_gallon = 8
ounces_in_pint = 16
ounces_in_gallon = pints_in_gallon*ounces_in_pint
R_gallon = ounces//ounces_in_gallon
R_pint = (ounces%ounces_in_gallon)//ounces_in_pint
R_ounce = (ounces%ounces_in_gallon)%ounces_in_pint
print(ounces,"ounces is equivalent to:")
print(R_gallon,"gallons,",R_pint,"pints and",R_ounce,"ounces")
