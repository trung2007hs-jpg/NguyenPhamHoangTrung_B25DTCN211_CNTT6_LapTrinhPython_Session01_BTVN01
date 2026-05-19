# Phân tích lỗi
# - Chương trình không crash vì đúng cú pháp Python.
# - Lỗi logic xảy ra ở phần xuất kết quả (`print`): Gọi sai tên biến hiển thị tương ứng với các nhãn thông tin bệnh nhân.

# khắc phục
# - Đưa các biến `name_patient`, `age`, `symptom` về đúng vị trí in ra màn hình.

print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ')

name_patient = input('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')

print(' --- PHIẾU KHÁM BỆNH --- ')
print('Tên bệnh nhân:', name_patient)
print('Tuổi:', age)
print('Triệu chứng:', symptom) 
