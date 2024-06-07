for i in [1, 2, 3, 4, 5]:
    print(i)


for i in range(5):
    if i==1:
        continue
    if i == 3:
        break
    print(i)
else:
    print("Loop finished") # else sau for sẽ chạy vào khi for hoàn thành , nhưng nếu bị break thì sẽ không chạy vào


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


for character in 'Hello':
    print(character)


for integer in range(5):
    print(integer)


for i in range(2, 10, 2):  # Bắt đầu từ 2, kết thúc trước 10, bước nhảy là 2
    print(i)


fruits = ["apple", "banana", "cherry"]
for index in range(len(fruits)):
    print(index, fruits[index])


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# dict
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()  # Để xuống dòng sau mỗi hàng
