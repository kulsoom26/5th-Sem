array = [3,4,5,8,1]
small = array[0]
for i in range(5):
    if(small>array[i]):
        small=array[i]
print(small)