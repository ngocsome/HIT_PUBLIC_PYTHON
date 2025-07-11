Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?
Python là ngôn ngữ thông dịch.

Giải thích:

Khi viết mã Python,  không cần biên dịch nó thành mã máy như các ngôn ngữ như C hoặc C++.

Thay vào đó, mã nguồn .py được thông dịch bởi trình thông dịch Python (Python Interpreter).


Bài 2: Tìm hiểu trước kiến thức buổi 2
1. Các kiểu dữ liệu trong Python:
- Số học (Numeric):

int: số nguyên (e.g. 5, -10)

float: số thực (e.g. 3.14, -2.5)

complex: số phức (e.g. 3+5j)

- Chuỗi (String): str (e.g. "Hello", 'Python')

- Danh sách (List): có thể chứa nhiều kiểu dữ liệu khác nhau. Ví dụ: [1, "a", 3.5]

- Tuple: giống List nhưng không thể thay đổi. Ví dụ: (1, 2, 3)

- Set: tập hợp các giá trị không trùng lặp. Ví dụ: {1, 2, 3}

- Dict (Từ điển): lưu trữ theo dạng key: value. Ví dụ: {"name": "Ngọc", "age": 20}

- Bool (Boolean): gồm hai giá trị True và False

2. Các toán tử trong Python:
Toán tử số học: +, -, *, /, // (chia lấy phần nguyên), % (chia lấy dư), ** (lũy thừa)

Toán tử so sánh: ==, !=, >, <, >=, <=

Toán tử logic: and, or, not

Toán tử gán: =, +=, -=, *=, /=, //=, %=, **=

Toán tử thành viên: in, not in

Toán tử định danh: is, is not

3. Mệnh đề điều kiện và vòng lặp:
Điều kiện (if-elif-else)

if ( điều kiện ):
    // code 
elif ( điều kiện ):
   // code 
else:
    // code 
Vòng lặp for

for i in range( start , stop , step ):
    
Vòng lặp while

i = 0
while i < 5:
    print(i)
    i += 1
4. Kiểu dữ liệu True, False:
bool là kiểu dữ liệu logic trong Python với 2 giá trị:

True: đúng

False: sai

Một số giá trị được coi là False trong biểu thức điều kiện:

0, 0.0

None

"" (chuỗi rỗng)

[] (list rỗng), {} (dict rỗng), set() (set rỗng)