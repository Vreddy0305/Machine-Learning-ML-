def common_elements(list1, list2):
    common_count = 0
    for elem in list1:
        if elem in list2:
            common_count += 1
            list2.remove(elem)
    return common_count
list1 = list(map(int, input("Enter element of list 1").split()))
list2 = list(map(int, input("Enter element of list 2").split()))
common_count = common_elements(list1, list2)
print(f"Common Elements: {common_count}")
