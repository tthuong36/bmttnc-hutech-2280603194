def chia_het_cho_5(so_nhi_phan):
  """
  Kiểm tra xem một số nhị phân có chia hết cho 5 hay không.

  Args:
    so_nhi_phan: Chuỗi biểu diễn số nhị phân.

  Returns:
    True nếu số nhị phân chia hết cho 5, False nếu không.
  """
  so_thap_phan = int(so_nhi_phan, 2)
  if so_thap_phan % 5 == 0:
    return True
  else:
    return False

# Nhập chuỗi số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (4 chữ số, phân tách bằng dấu phẩy): ")

# Tách chuỗi thành danh sách các số nhị phân
danh_sach_so_nhi_phan = chuoi_so_nhi_phan.split(',')

# Tạo danh sách các số nhị phân chia hết cho 5
ket_qua = []
for so_nhi_phan in danh_sach_so_nhi_phan:
  if chia_het_cho_5(so_nhi_phan):
    ket_qua.append(so_nhi_phan)

# In kết quả
print(','.join(ket_qua))