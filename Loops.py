def funcRange(num):
    result = []
    for i in range(num):
        result.append(i * i)
    return result

n = int(input("Enter a number: "))
index_list = funcRange(n)
print(index_list)