__author__ = 'jc451634'
def tax_return(income):
    if income <= 16000:
        return ('Pay Nothing')
    else:
        return(income*.3)
print(tax_return(1500))


