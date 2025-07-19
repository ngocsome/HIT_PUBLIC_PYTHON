import math 

while True : 
    try : 
        n = int ( input ( " Nhập n : ")) 
        if ( n > 0 ) : 
            break 
        else : 
            print ( " Nhập số không âm  ! ") 
    except ValueError : 
        print ( " Lỗi ! ")


chuoi = str ( n ) 

chu_so = len(chuoi) 

tong = sum ( int (ch) for ch in chuoi ) 

print ( " Số đã nhập : " , n ) 
print ( " Số chữ số : " , chu_so ) 
print ( " Tổng chữ số : " , tong )