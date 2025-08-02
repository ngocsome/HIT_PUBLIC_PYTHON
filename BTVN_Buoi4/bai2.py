''' Bài 2: Xử lý tập hợp đăng ký học
Khởi tạo hai tập hợp (set), trong đó tập A chứa các mã sinh viên đăng ký học tiếng Anh tại bàn tiếp nhận số 1, tập B là các mã sinh viên đăng ký học tại bàn tiếp nhận số 2. In thông tin hai tập hợp lên màn hình.

Cho biết có sinh viên nào đăng ký học tại cả hai bàn hay không.
Cho biết danh sách tổng hợp của các sinh viên đã đăng ký của cả hai bàn.
Cho biết danh sách các sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2''' 

A = { "SV01" , "SV02" ,"SV03" ,"SV04"} 
B = {"SV03" , "SV04" , "SV05" , "SV06"} 

print ( " Danh sách sinh viên đăng kí tại bàn 1 : " , A)
print ( " Danh sách sinh viên đăng kí tại bàn 2 : " , B)

both = A & B 
print ( " Sinh viên đăng kí tại cả 2 bàn : " , both if both else "Không có ")

union = A | B 
print ( " Sinh viên đăng kí của cả 2 bàn : " , union if union else "Không có ") 

only_A = A - B 
print ( " Sinh viên đăng kí tại bàn 1 mà không đăng kí tại bàn 2 : " , only_A)
