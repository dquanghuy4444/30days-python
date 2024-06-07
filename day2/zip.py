# hàm zip : kết hợp các phần tử từ các chuỗi có thể lặp thành các cặp tuple

names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 22]
cities = ["Hanoi", "HCMC", "Danang"]

pairs = zip(names, ages, cities)

for pair in pairs:
    print(f"{pair[0]} is {pair[1]} years old and lives in {pair[2]}")


# Tạo một danh sách các số bình phương từ 1 đến 10
squares = map(lambda x: x * x, range(1, 11))

# Kết hợp các số bình phương với các số từ 1 đến 10
pairs = zip(squares, range(1, 11))

# Lọc các cặp có số bình phương chẵn
even_pairs = filter(lambda pair: pair[0] % 2 == 0, pairs)

# In ra các cặp số bình phương chẵn và số tương ứng
for pair in even_pairs:
  print(f"{pair[0]} is the square of {pair[1]}")
