first_list = input().split(", ")
second_list = input().split(", ")

result = []
for substr in first_list:
    for word in second_list:
        found_substr = substr in word
        if found_substr:
            result.append(substr)
            break

print(result)
