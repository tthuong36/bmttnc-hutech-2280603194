X, Y = map(int, input("Nhập X, Y (cách nhau bởi dấu phẩy): ").split(','))
matrix = [[i * j for j in range(Y)] for i in range(X)]
print(matrix)