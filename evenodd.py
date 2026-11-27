#even odd number

n=int(input('enter a number from 1to 10:  '))
if 1 <= n <=10:

    if n%2==0:
        print ('number is even')
    else:
        print ('number is odd')

else:
    print('invalid input')