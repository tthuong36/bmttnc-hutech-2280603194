def kiem_tra_nguyen_to():
  try:
    n = int(input("Nhập số: "))
    print("Nguyên tố" if n > 1 and all(n % i for i in range(2, int(n**0.5) + 1)) else "Không nguyên tố")
  except:
    print("Lỗi")

kiem_tra_nguyen_to()