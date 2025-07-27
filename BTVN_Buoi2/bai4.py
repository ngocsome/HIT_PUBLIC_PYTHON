# Nhập số xu
while True:
    try:
        N = int(input("Nhập số xu bạn có: "))
        if N >= 28:
            break
        else:
            print("Bạn cần ít nhất 28 xu để mua 1 chai.")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

gia_chai = 28


so_chai = N // gia_chai


vo = so_chai

while vo >= 3:
    doi_duoc = vo // 3
    so_chai += doi_duoc
    vo = vo % 3 + doi_duoc  


print(f"Bạn có thể uống tối đa {so_chai} chai bia.")
