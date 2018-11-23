def my_bubble_sort(num_list):
    swap_num = False
    while not swap_num:
        for j in range(len(num_list) - 1):
            for i in range(len(num_list) - 1):
                if num_list[i] > num_list[i + 1]:
                    num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                    swap_num = True
    print (num_list)

num_list = [9,5,4,15,3,8,11]
j = 0
i = 0

my_bubble_sort(num_list)
