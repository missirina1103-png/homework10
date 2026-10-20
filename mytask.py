my_list = [1, "apple", 3.14, True, "banana", None, "cherry", [1, 2]]

string_count = 0

for item in my_list:
    if type(item) == str:
        string_count += 1

print("Count of str elements:", string_count)