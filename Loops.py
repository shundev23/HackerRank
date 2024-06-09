def funcRange(num):
    result = []
    for i in range(num):
        result.append(i * i)
    return result

n = int(input())
index_list = funcRange(n)

for value in index_list:
    print(value)