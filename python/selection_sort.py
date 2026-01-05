def selection_sort():
    list=[7,6,10,25,5]
    for i in range(len(list)) :
        min=i
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                min=j
        list[i],list[min]=list[min],list[i]
                
    return list

print(selection_sort())