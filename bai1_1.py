n = int ( input(" Nhập số  : ")) 
print ( " Số đã nhập : " , n ) 
if n < 0 or n >= 10000 : 
    print ( " Số không hợp lệ ") 
else : 
    s = str ( n ) # tách n thành chuỗi 
    hang =  [" Ngàn " , " trăm " , " chục " , " đơn vị "] 
    s = s.zfill( 4 ) 
    for i in range(4) : 
        if s[i] != 0 : 
            print ( s[i] , hang[i]) # ghép với list/set 
