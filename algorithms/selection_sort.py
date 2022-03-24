def sel_sort(sort_list):
    i_length = range(0, len(sort_list) - 1)
    num = 1#count
    for i in i_length:
        min_value = i
        
        for j in range(i + 1, len(sort_list)):
            if sort_list[j] < sort_list[min_value]:
                min_value = j
                
        if min_value != i:
            sort_list[min_value], sort_list[i] = sort_list[i], sort_list[min_value]
        
        
        num += 1#count
        print(num) #count  
        print(sort_list)
    return sort_list

print(sel_sort([123, 3, 2, 4, 12, 5, 12, 2, 7, 9, 23, 634, 1213, 9, 43, 76, 1]))
