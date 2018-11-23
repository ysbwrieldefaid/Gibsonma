def binary_search(test_list, user_guess):
    first = 0
    last = len(test_list) - 1
    success = False

    while not success and first <= last:
        middle = int((first + last)/2)
        if test_list[middle] == user_guess:
            success = True
        else:
            if user_guess > test_list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    return success

test_list = [4,13,22,27,39,42,50,56,73,88,99,191]

user_guess = int(input("\nenter something to look for: \n"))
print(binary_search(test_list,user_guess))
