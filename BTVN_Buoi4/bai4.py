# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    x = input(f"Nhập phần tử thứ {i+1}: ")
    a.append(x)


b = tuple(a)

# In tuple b
print("Tuple b:", b)


count = sum(1 for item in b if item.isdigit())

# In kết quả
print("Số phần tử có dạng số trong tuple:", count)
