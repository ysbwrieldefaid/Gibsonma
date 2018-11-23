def linear_search(alist, item_sought):
    index = -1
    i = 0
    found = False
    while i < len(alist) and not found:
        if alist[i] == item_sought:
            index = 1
            found = True
        i = i + 1
    return index

num_list = [7,6,3,1,18,23,2,100]
alpha_list = ["A","C","D","G","M","R","W","Z"]

index = linear_search(num_list, 1)
if index == 1:
    print("item has been found")
else:
    print("item not found")

index = linear_search(num_list, 4)
if index == 1:
    print("item has been found")
else:
    print("item not found")

index = linear_search(alpha_list, "M")
if index == 1:
    print("item has been found")
else:
    print("item not found")

index = linear_search(alpha_list, "N")
if index == 1:
    print("item has been found")
else:
    print("item not found")

