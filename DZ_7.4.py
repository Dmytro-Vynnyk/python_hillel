def common_elements():
    new_list = {i for i in range(100) if i % 3 == 0}
    new_list1 = {i for i in range(100) if i % 5 == 0}
    return new_list & new_list1

print(common_elements())
