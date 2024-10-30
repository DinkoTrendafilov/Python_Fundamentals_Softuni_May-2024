def rectangle_area(width, height):
    result = width * height
    return result


width_value = int(input())
height_value = int(input())

result_func = rectangle_area(width_value, height_value)
print(result_func)
