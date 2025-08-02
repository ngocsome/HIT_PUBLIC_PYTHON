# Nhập n và m
n, m = map(int, input("Nhập n và m (cách nhau bằng khoảng trắng): ").split())

# Nhập mảng gồm n phần tử
arr = list(map(int, input(f"Nhập {n} phần tử của mảng: ").split()))

# Nhập tập hợp A (số bạn thích)
A = set(map(int, input(f"Nhập {m} phần tử của tập A (bạn thích): ").split()))

# Nhập tập hợp B (số bạn không thích)
B = set(map(int, input(f"Nhập {m} phần tử của tập B (bạn không thích): ").split()))

# Khởi tạo mức độ hạnh phúc
happiness = 0

# Tính mức độ hạnh phúc
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

# In kết quả
print("Tổng mức độ hạnh phúc:", happiness)
