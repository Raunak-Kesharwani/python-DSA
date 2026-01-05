def bub_sort():
    list=[ 7,12,9,11,3 ]
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]> list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
            
    return list
print(bub_sort())