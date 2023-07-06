def dot_product():
    data_list = []
    while True:
        data1 = input("Enter the x:")
        if data1 == "/":
            break
        data_list += [data1]
    print(data_list)
    a = len(data_list)
    list1 = 0
    for i in range(a):
        list1 += int(data_list[i])
    data_list2 = []
    while True:
        data2 = input("Enter the x:")
        if data2 == "/":
            break
        data_list2 += [data2]
    print(data_list2)
    list2 = 0
    for i in range(a):
        list2 += int(data_list2[i])
    print(list1 + list2)
dot_product()