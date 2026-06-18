friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
numbers = [1, 2, 3, 4, 5]

friends.append(numbers[2])
print(friends)

friends.extend(numbers)
print(friends)

numbers.insert(2 , 11)
print(numbers)