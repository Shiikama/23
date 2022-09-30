print('Welcome, colleague!')
list_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
c = 0  # permutation counter
for b in range(1, len(list_1)):
    for i in range(len(list_1) - 1, 1, -1):
        for x in range(len(list_1) - 1, 1, -1):
            while (i-x) >= 0:
                while list_1[i] < list_1[i - x]:
                    a = list_1[i]
                    list_1[i] = list_1[i - x]
                    list_1[i - x] = a
                    c += 1
                break
print(c)
print(f'List {list_1}')
