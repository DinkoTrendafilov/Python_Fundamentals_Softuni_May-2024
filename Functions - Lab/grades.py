def solve(grade_value):
    result = ""
    if grade_value < 3:
        result = "Fail"
    elif grade_value < 3.5:
        result = "Poor"
    elif grade_value < 4.5:
        result = "Good"
    elif grade_value < 5.5:
        result = "Very Good"
    elif grade_value <= 6:
        result = "Excellent"

    return result


grade = float(input())

result_func = solve(grade)
print(result_func)
