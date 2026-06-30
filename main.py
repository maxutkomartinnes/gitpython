from math_functions import calculate_rectangle_area, rectangle_perimeter
if __name__ == "__main__":
    width = 8
    height = 5
    area = calculate_rectangle_area(width, height)
    print(f"Площа прямокутника зі сторонами {width} і {height} дорівнює: {area}")
    perimeter = rectangle_perimeter(width, height)
    print(f"Периметр прямокутника зі сторонами {width} і {height} дорівнює: {perimeter}")