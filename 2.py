input_list = [7, 4, 9, 2, 5, 1]
filtered_list = list(filter(lambda x: x % 2 == 0, input_list))
filtered_list.sort()

print(filtered_list)