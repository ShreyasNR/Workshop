__author__ = 'jc451634'
num = 0
out_file = open('Number.txt','w')
while num >= 0:
    num = int(input('number:'))
    print(str(num),file=out_file)
out_file.close()