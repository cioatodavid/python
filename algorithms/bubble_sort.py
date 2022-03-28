def bubble(bub_list):
    i_length = len(bub_list) - 1
    sorted = False
    num = 1#count
    while not sorted:
        sorted = True
        for i in range(i_length):
            if bub_list[i] > bub_list[i + 1]:
                sorted = False
                bub_list[i], bub_list[i + 1] = bub_list[i + 1], bub_list[i]
                print(bub_list)
                num += 1 #count
                print(num) #count  
               
    return bub_list


print(bubble([123, 3, 2, 4, 12, 5, 12, 2, 7, 9, 23, 634, 1213, 9, 43, 76, 1]))
