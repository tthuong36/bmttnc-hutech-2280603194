
def tinh_dien_tich_hinh_tron(ban_kinh):
  """Tính diện tích hình tròn với bán kính cho trước.

  Args:
    ban_kinh: Bán kính của hình tròn.

  Returns:
    Diện tích của hình tròn.
  """

  pi = 3.14
  dien_tich = pi * ban_kinh**2
  return dien_tich

# Nhập bán kính từ người dùng
ban_kinh = float(input("Nhập bán kính hình tròn: "))

# Tính diện tích
dien_tich = tinh_dien_tich_hinh_tron(ban_kinh)

# In kết quả
print("Diện tích hình tròn là:", dien_tich)