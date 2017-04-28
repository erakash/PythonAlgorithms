#Insertion Sort

array = [3,4,2,1,7,5,8,4,9,7]


for i in range(1,len(array)):
    key = array[i]
    j = i-1
    while(j>=0 and array[j]>key) :
        array[j+1]=array[j]
        j=j-1
    array[j+1] = key

for k in range(0,len(array)):
    print(array[k])

# Insertion Sort Reverse
print("Reverse Order")
for i in range(1,len(array)):
    key = array[i]
    j = i-1
    while(array[j]<key and j >=0):
        array[j+1]=array[j]
        j= j-1
    array[j+1] = key
for k in range(0,len(array)):
    print(array[k])