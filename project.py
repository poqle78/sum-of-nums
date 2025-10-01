def f(trg, nums):
    checked = []
    flag1 = 1
    flag2 = 1
    if len(nums) > 1:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i not in checked and j not in checked:
                    if nums[i] + nums[j] == trg:
                        if flag1:
                            print('Minimum:', i, j)
                            checked.append(i)
                            checked.append(j)
                            flag1 = 0
                            print('Others:', end=' ')
                            flag2 = 0
                        else:
                            print(f'({i}, {j})', end=' ')
                            checked.append(i)
                            checked.append(j)
        if flag2:
            print('None')
    else:
        print('The list must contain more than 1 element!')


try:
    nums = [int(i) for i in input('Введите список (через пробел): ').split()]
    trg = int(input("Введите искомую сумму: "))
    f(trg, nums)
except ValueError:
    print('That was no valid number')
