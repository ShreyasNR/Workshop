__author__ = 'jc451634'
Instruction = 'Welcome to our program.\ninput negetive number into number of item to quit '
print(Instruction)

numofitems =1
while numofitems > 0:
    numofitems = int(input('please input thr number of items:'))
    costperitem = float(input('the shipping cost of each item: $'))
    totalshipcost = numofitems * costperitem;
    if totalshipcost > 100:
       totalshipcost = totalshipcost  * 0.9
    print('the total cost for delivering your products is:' ,totalshipcost)
