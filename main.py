print('Welcome, colleague!')
file = open("numbers.data")
file_with_lines = file.readlines()
file_with_lines = (file_with_lines[0].split())
list_1 = []
for line in file_with_lines:
    e = int(line)
    list_1.append(e)
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
