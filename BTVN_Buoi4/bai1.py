'''Bài 1: Chuyển đổi tuple và tính trung bình
Viết chương trình thực hiện các yêu cầu sau:

Cho một tuple chứa n phần tử là các xâu ký tự số (0-9)
Chuyển đổi thành tuple mới chứa các số tương ứng
Tính trung bình cộng các phần tử trong tuple kết quả '''

new_tuple = ( "1" , "3","5","7","9") 

change_tuple = tuple( map (int , new_tuple)) 

average = sum( change_tuple) / len ( change_tuple) 

print ( " Tuple ban đầu : " , new_tuple) 
print ( " Tuple đã thay đổi : " , change_tuple) 
print ( " Trung bình cộng tuple : " , average )