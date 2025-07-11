def tinh_S( x , n ) : 
    if n % 2 != 0 : 
        return 0 
    S = 2016 * x 
    for i in range ( 2 , n + 1  , 1 ) : 
        S+= x** i / 3 **( i - 1 )
    return S 

x = int ( input(" Nhập x : "))
n = int ( input("Nhập n : "))

S = tinh_S( x , n ) 
print ( " Kết quả : " , S )

