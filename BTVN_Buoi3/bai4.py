'''Bài 4: Chuẩn hóa định dạng họ tên
Bạn Chiến đang rất bận với sự kiện sinh nhật của câu lạc bộ và cần sự trợ giúp của các bạn để xử lý một bài toán nhỏ. Đề bài như sau:

Mô tả bài toán:
Bạn nhận được một chuỗi văn bản chứa họ và tên của một thành viên trong câu lạc bộ. Tuy nhiên, chuỗi này chưa được viết đúng chuẩn theo định dạng họ tên.

Yêu cầu:
Hãy viết một chương trình để chuẩn hóa chuỗi họ tên này theo định dạng chuẩn, tức là mỗi từ trong họ tên đều bắt đầu bằng chữ cái viết hoa và các chữ cái còn lại là chữ thường. Định dạng chuẩn của họ tên là: "Họ Tên đệm Tên", với mỗi phần đều bắt đầu bằng chữ cái viết hoa.

Input: Một chuỗi văn bản chứa họ và tên của một thành viên.
Output: Chuỗi văn bản đã được chuẩn hóa theo định dạng chuẩn.
Ví dụ: “lương Thái sơN” -> “Lương Thái Sơn”.''' 

def chuan_hoa ( ho_ten ) :  
    # xóa khỏag trống , đưa về chữ thường 
    ho_ten = ho_ten.strip().lower()  

    # tách từ 
    tu = ho_ten.split() 

    # viết hoa chữ đầu 
    chuan_hoa = ' '.join(word.capitalize() for word in tu)
    
    return chuan_hoa

input_name = input("Nhập họ tên cần chuẩn hóa: ")
output_name = chuan_hoa(input_name)

# In ra kết quả
print("Họ tên sau khi chuẩn hóa:", output_name)