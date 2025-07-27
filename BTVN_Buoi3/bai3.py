'''Bài 3:
Nhập 2 chuỗi s1, s2 từ bàn phím.
In ra đảo ngược của chuỗi s1.
Nhập vào 2 số nguyên a, b (1 <= a < b <= len(s2)). In ra chuỗi s2 sau khi đảo ngược chuỗi từ vị trí a đến b.
In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn.
Trả về chuỗi s4 là đan xen các kí tự của s1 và s2.
VD: s1 = “abc”, s2 = “123” -> s4 = “a1b2c3”.'''

s1 = input ( "Nhập chuỗi s1 : ") 
s2 = input ( "Nhập chuỗi s2 : ") 

print ( 'Đảo ngược chuỗi s1 : ' , s1[:: -1]) 

a = int ( input ( " Nhập a : ")) 
b = int ( input ( " Nhập b : ")) 

if 1 <= a < b <= len(s2) : 
    s2_new = s2[:a-1] + s2[a-1:b][::-1] + s2[b:] 
    print ( f'Chuỗi s2 sau khi đảo ngược từ {a} đến {b} : ' , s2_new) 
else : 
    print ( " a và b không hợp lệ ")

s3 = ''.join(s1[i] for i in range(len(s1)) if i % 2 != 0)
print("s3 (s1 sau khi xóa kí tự ở vị trí chẵn):", s3)

s4 = ''
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s4 += s1[i] + s2[i]
s4 += s1[min_len:] + s2[min_len:] 
print("s4 (đan xen s1 và s2):", s4)