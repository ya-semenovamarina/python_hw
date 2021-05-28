num_list = []
for num in range(1, 1001, 2):
    num_list.append(num ** 3)

sum_digits_1 = 0
for num in num_list:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
        if check_sum % 7 == 0:
            sum_digits_1 += num

sum_digits_2 = 0
for num in num_list:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
        if check_sum % 7 == 0:
            sum_digits_2 += num

print(sum_digits_1)
print(sum_digits_2)
