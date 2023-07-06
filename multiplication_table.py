def create_multiplication_table(n):
    multiplication_table = {}
    for i in range(1, n + 1):
        row = {}
        for j in range(1, n + 1):
            row[j] = i * j
        multiplication_table[i] = row
    return multiplication_table

# 建立一個九九乘法表，範圍為1到9
n = 9
table = create_multiplication_table(n)

# 顯示九九乘法表
for i in range(1, n + 1):
    row = ""
    for j in range(1, n + 1):
        row += f"{i} x {j} = {table[i][j]}\t"
    print(row)

# 查詢乘法結果

num1 = input("請輸入1~9的數字: ")
num1 = int(num1)
num2 = input("請輸入1~9的數字: ")
num2 = int(num2)
result = table[num1][num2]
print(f"{num1} x {num2} = {result}")