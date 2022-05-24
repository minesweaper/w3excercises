# Write a Python program to filter the positive numbers from a list

nums = [34, 1, 0, -23, 12, -88]
print(f"Set of numbers: {nums}")
new_nums = list(filter(lambda x: x > 0, nums))
print(f"Positive numbers: {new_nums}")
