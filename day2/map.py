# hàm map : biến đổi phần tử trong iterable (tuple , list , ...) thành phần từ khác và trả về 1 map object hay 1 iterator
# dùng khi muốn thực hiện thao tác giống nhau trên mỗi phần tử của 1 interable

def square(x):
    return x ** 2


# map object chỉ cho phép duyệt qua phần tử 1 lần. Sau khi đã duyệt qua hết, không thể truy cập lại các phần tử trừ khi tạo lại iterator đó
# map object không hỗ trợ truy cập ngẫu nhiên (tức là không thể lấy phần tử tại 1 vị trí cụ thể mà không duyệt qua các phần tử trước đó). Khi cần truy cập 
# ngẫu nhiên hoặc duyệt nhiều lần, cần chuyển đổi thành danh sách hoặc các cấu trúc dữ liệu khác
# Để sử dụng lại dữ liệu hoặc duyệt nhiều lần,cần chuyển đổi nó sang cấu trúc dữ liệu khác như danh sách (list), bộ (tuple), hoặc tập hợp (set)
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(squared_numbers)
# for number in squared_numbers:
#     print(number) 
print(list(squared_numbers))  # cần chuyển kết quả về list hoặc các dạng khác
# print(tuple(squared_numbers))
# print(set(squared_numbers))

# sử dụng lambda để thay thế định nghĩa hàm
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # [1, 4, 9, 16, 25]

# nhiều iterable
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
combined = map(lambda name, score: f"{name}: {score}", names, scores)
print(list(combined))  # ['Alice: 85', 'Bob: 90', 'Charlie: 78']


# trả về map object
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

# Chuyển đổi thành tuple
squared_numbers_tuple = tuple(map(lambda x: x ** 2, numbers))
print(squared_numbers_tuple)  # (1, 4, 9, 16, 25)

# Chuyển đổi thành set
squared_numbers_set = set(map(lambda x: x ** 2, numbers))
print(squared_numbers_set)  # {1, 4, 9, 16, 25}

# áp dụng hàm str
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = map(str.upper, fruits)
print(list(uppercase_fruits))  # ['APPLE', 'BANANA', 'CHERRY']

# xử lý dict
data = {"a": 1, "b": 2, "c": 3}
keys = map(lambda kv: kv[0], data.items())
values = map(lambda kv: kv[1], data.items())
print(list(keys))   # ['a', 'b', 'c']
print(list(values))  # [1, 2, 3]
