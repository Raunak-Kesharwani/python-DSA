def insetion_sort():
    list=[10,6,7,5,9]
    for i in range(1,len(list)):
        in_index=i
        value=list[i]
        for j in range(i-1,-1,-1):
            if value<list[j]:
                list[j+1]=list[j]
                in_index=j
            else:
                break
        list[in_index]=value
    return list
print(insetion_sort())