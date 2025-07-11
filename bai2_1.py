from math import*
def is_prime(n) : 
    if n < 2 : 
        return False 
    if n == 2 : 
        return True 
    if n % 2 == 0 : 
        return False 
    for i in range ( 3 , int(sqrt(n)) , 1 ) : 
        if n % i == 0 : 
            return False 
        else : 
            return True 


# đối xứng 
def is_palindrome(x) : 
    return str(x) == str(x)[::-1]

# check 
while True : 
    try : 
        S = int ( input("Nhập S : ")) 
        E = int ( input("Nhập E ")) 
        if S < E and E <= 999999999: 
            break 
        else : 
            print("Nhập lại S<E và E không quá 8 chữ số ") 
    except : 
        print ( " Nhập số nguyên hợp lệ ")        

tong = 0 
for i in range ( S , E + 1 , 1 ) : 
    if is_prime(i) and is_palindrome(i) : 
        tong += i 

print("Tổng các số nguyên tố và đối xứng trong đoạn [{} {}] là : {}".format(S , E , tong))
    
        