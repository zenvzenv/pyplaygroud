import random

with open('prod_consumer.py', 'r', encoding='utf-8') as f:
    data = f.read()

factor = 0.14
size = len(data)
delete_count = size * factor
print(delete_count)
data_list = list(data)
print(len(data_list))
# 修改稿
for i in range(1, 6):
    for j in range(1, size):
        data_list[random.randint(0, size - 1)] = ''
    result = "".join(data_list)
    print(result.strip())
