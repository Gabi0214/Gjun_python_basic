# N 個數字, 由小到大排序
# 共 N 輪
# 每一輪去比較手上的牌(已經排序好的部分), 比較大的就排後面

import numpy as np
N = 5
numbers = np.random.choice(100, N, replace=False)
print("Before: ", numbers)

sorted_numbers = list() # 排序好的部分

for round in range(N): # 共 N 輪
    if round == 0:
        sorted_numbers.append(numbers[0])
    else: # 手上有手牌了
        for index in range(len(sorted_numbers)-1, -1, -1): # 去比較要放在哪裡
            if numbers[round] > sorted_numbers[index]: # 如果比較大, 就放在後面
                front = sorted_numbers[:index+1] # 0 ~ index
                back = sorted_numbers[index+1:] # index+! ~ end
                sorted_numbers = front  + [numbers[round]] + back
                break
            if index == 0:
                sorted_numbers = [numbers[round]] + sorted_numbers

print("After: ",sorted_numbers)                