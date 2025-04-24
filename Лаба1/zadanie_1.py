# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
first_part = numbers[:4]
two_part = numbers[5:]
filtered_numbers = first_part + two_part
average = round(sum(filtered_numbers) / len(numbers), 2)
numbers[4]= average
print("Измененный список:", numbers)
