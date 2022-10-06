def divisor (num_tot, divisor):
    '''funtion to check wheter a number is a divisor of another
            INPUT: 2 numbers (first one is > 2nd one)
            OUTPUT: True or False depending if is divisor or not.'''

    if num_tot%divisor==0:
        return True
    else:
        return False


check =False
i = 20*19*17*13*11
while check ==False:
    i  +=1
    if divisor(i,20):
        if divisor(i,19):
            if divisor(i,18):
                if divisor(i,17):
                    if divisor(i,16):
                        if divisor(i,15):
                            if divisor(i,14):
                                if divisor(i,13):
                                    if divisor(i,12):                                        
                                        if divisor(i,11):
                                            check = True

print ('* ' *55,'\n')
print (f'The smallest number which is divisible by all numbers from 20 to 1 (both included) is {i}.\n')
print ('* ' *55,'\n')

