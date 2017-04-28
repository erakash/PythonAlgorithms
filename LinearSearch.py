array = [5,5,6,6,7,4,3,3,2,24,45,45,43,34,65,57,56]
searchvalue = 562
for i in range(len(array)):
    if(array[i] == searchvalue):
        print('value found at: ' + str(i))
        break
    else:
        if(i==len(array)-1):
            print('value not found')

